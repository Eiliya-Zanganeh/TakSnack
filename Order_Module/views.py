from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.http import HttpRequest, HttpResponse

from Food_Module.models import SandwichModel, DrinkModel
from Home_Module.models import SiteSettingModel
from Order_Module.models import OrderModel
from Order_Module.send_email import send_email

import numpy as np


class CartView(TemplateView):
    template_name = 'Order_Module/cart.html'

    def get_context_data(self, **kwargs):
        result = super(CartView, self).get_context_data(**kwargs)
        session_sandwiches = self.request.session.get('sandwiches')
        special_suggestions = self.request.session.get('special_suggestions')
        session_drinks = self.request.session.get('drinks')
        total_price = 0
        total_price_offer = 0
        if session_sandwiches:
            sandwiches, total, total_offer = self.get_products(session_sandwiches, SandwichModel, True)
            total_price += total
            total_price_offer += total_offer
            result['sandwiches'] = sandwiches
        if special_suggestions:
            special_suggestions, total, total_offer = self.get_products(special_suggestions, SandwichModel)
            total_price += total
            total_price_offer += total_offer
            result['special_suggestions'] = special_suggestions
        if session_drinks:
            drinks, total, total_offer = self.get_products(session_drinks, DrinkModel)
            total_price += total
            total_price_offer += total_offer
            result['drinks'] = drinks

        result['media_url'] = settings.MEDIA_URL
        result['total_price'] = total_price
        result['total_price_offer'] = total_price_offer

        # result['sauce'] = SauceModel.objects.filter(is_active=True)
        return result

    @staticmethod
    def get_products(session_products, model, is_sandwiches=False):
        session_products = np.array(session_products)
        products_id = set(session_products[:, 0])
        all_products = model.objects.filter(id__in=products_id).values('id', 'name', 'price', 'image', 'offer_price')
        cart = []
        i = 0
        total_price = 0
        total_price_offer = 0
        for session_product in session_products:
            for product in all_products:
                if session_product[0] == product['id']:
                    cart.append({
                        'id': i,
                        'product': product,
                        'count': session_product[1]
                    })
                    if product['offer_price']:
                        price_offer = product['offer_price']
                    else:
                        price_offer = product['price']
                    if is_sandwiches:
                        total_price += int(product['price']) + (8000 * (session_product[1] - 1))
                        total_price_offer += int(price_offer) + (8000 * (session_product[1] - 1))
                    else:
                        total_price += int(product['price']) * int(session_product[1])
                        total_price_offer += int(price_offer) * int(session_product[1])

            i += 1
        return cart, total_price, total_price_offer


class AddProductView(View):
    def get(self, request: HttpRequest, product_name, product_id):
        new_product = [product_id, 1]
        cart = request.session.get(product_name)
        if cart:
            cart = list(cart)
            is_found = False
            if product_name != 'sandwiches':
                for idx, product in enumerate(cart):
                    if product[0] == product_id:
                        is_found = True
                        cart[idx][1] += 1
            if not is_found:
                cart.append(new_product)
            request.session[product_name] = cart
        else:
            new_cart = [new_product]
            request.session[product_name] = new_cart

        return redirect(reverse('cart_url'))


class IncreaseCount(View):
    def get(self, request: HttpRequest):
        product_name = self.request.GET.get('product_name')
        product_id = int(self.request.GET.get('product_id'))
        cart = list(request.session.get(product_name))
        print(cart[product_id])
        cart[product_id][1] += 1
        print(cart[product_id])
        self.request.session[product_name] = cart
        return HttpResponse("OK")


class DecreaseCount(View):
    def get(self, request: HttpRequest):
        product_name = self.request.GET.get('product_name')
        product_id = int(self.request.GET.get('product_id'))
        cart = list(request.session.get(product_name))
        print(cart[product_id])
        cart[product_id][1] -= 1
        print(cart[product_id])
        self.request.session[product_name] = cart
        return HttpResponse("OK")


class RemoveProduct(View):
    def get(self, request: HttpRequest, product_name, product_id):
        cart = list(self.request.session.get(product_name))
        cart.pop(product_id)
        self.request.session[product_name] = cart
        return redirect(reverse('cart_url'))


class SubmitOrder(View):
    def get(self, request: HttpRequest):
        return redirect(reverse('home_url'))

    def post(self, request: HttpRequest):
        session_sandwiches = self.request.session.get('sandwiches')
        special_suggestions = self.request.session.get('special_suggestions')
        session_drinks = self.request.session.get('drinks')

        # print(session_sandwiches)
        # print(session_drinks)
        # print(special_suggestions)
        txt = ""

        total_price = 0
        total_price_offer = 0

        if session_sandwiches:
            sandwiches, total, total_offer = CartView.get_products(session_sandwiches, SandwichModel, True)
            total_price += total
            total_price_offer += total_offer
            for sandwich in sandwiches:
                txt += f"{sandwich['product']['name']} --- {sandwich['count']} \n"
            self.request.session.pop('sandwiches')

        if special_suggestions:
            special_suggestions, total, total_offer = CartView.get_products(special_suggestions, SandwichModel)
            total_price += total
            total_price_offer += total_offer
            if special_suggestions:
                for special in special_suggestions:
                    txt += f"{special['product']['name']} --- {special['count']} \n"
                self.request.session.pop('special_suggestions')

        if session_drinks:
            drinks, total, total_offer = CartView.get_products(session_drinks, DrinkModel)
            total_price += total
            total_price_offer += total_offer
            for drink in drinks:
                txt += f"{drink['product']['name']} --- {drink['count']} \n"
            self.request.session.pop('drinks')

        txt += "\n \n \n"
        txt += f"قیمت قبل از تخفیف --- {total_price} \n"
        txt += f"قیمت نهایی ( بعد از تخفیف ) --- {total_price_offer} \n"

        full_name = self.request.POST.get('full_name')
        phone = self.request.POST.get('phone')
        address = self.request.POST.get('address')

        new_order = OrderModel(
            full_name=full_name,
            phone_number=phone,
            address=address,
            description=txt,
        )
        new_order.save()

        setting = SiteSettingModel.objects.filter(is_active=True).values('email').first()

        context = {
            'full_name': full_name,
            'phone_number': phone,
            'address': address,
            'description': txt.replace('\n', '<br>'),
        }
        send_email('سفارش جدید', setting['email'], 'email.html', context)

        return HttpResponse(
            "<script>alert('سفارش شما با موفقیت ثبت شد. منتظر تماس ما باشید...');window.location.href = '/'</script>")
