(function () {
    'use strict';

    var sitePlusMinus = function () {

        var value,
            quantity = document.getElementsByClassName('quantity-container');

        function createBindings(quantityContainer) {
            var quantityAmount = quantityContainer.getElementsByClassName('quantity-amount')[0];
            var increase = quantityContainer.getElementsByClassName('increase')[0];
            var decrease = quantityContainer.getElementsByClassName('decrease')[0];
            increase.addEventListener('click', function (e) {
                increaseValue(e, quantityAmount);
            });
            decrease.addEventListener('click', function (e) {
                decreaseValue(e, quantityAmount);
            });
        }

        function init() {
            for (var i = 0; i < quantity.length; i++) {
                createBindings(quantity[i]);
            }
        };

        function increaseValue(event, quantityAmount) {
            value = parseInt(quantityAmount.value, 10);

            // console.log(quantityAmount, quantityAmount.value);

            value = isNaN(value) ? 0 : value;
            const productName = quantityAmount.name;
            const productId = quantityAmount.id;
            if (productName === 'sandwiches') {
                if (value < 2) {
                    var question = confirm("آیا یک نان اضافه می خواهید؟")
                    if (question) {
                        $.ajax({
                            url: "/cart/increase-count/",
                            method: "get",
                            data: {product_name: productName, product_id: productId}
                        }).done(function (res) {
                            console.log(res)
                            value++;
                            quantityAmount.value = value;
                            getPrices()
                        });
                    }
                } else {
                    alert("حداکثر تعداد نان در هر ساندویچ 2 نام است.")
                }
            } else {
                $.ajax({
                    url: "/cart/increase-count/",
                    method: "get",
                    data: {product_name: productName, product_id: productId}
                }).done(function (res) {
                    console.log(res)
                    value++;
                    quantityAmount.value = value;
                    getPrices()
                });
            }
        }

        function decreaseValue(event, quantityAmount) {
            value = parseInt(quantityAmount.value, 10);

            value = isNaN(value) ? 0 : value;
            const productName = quantityAmount.name;
            const productId = quantityAmount.id;
            if (value > 1) {
                $.ajax({
                    url: "/cart/decrease-count/",
                    method: "get",
                    data: {product_name: productName, product_id: productId}
                }).done(function (res) {
                    console.log(res)
                    value--;
                    quantityAmount.value = value;
                    getPrices()
                });
            } else {
                if (productName === 'sandwiches') {
                    alert("هر ساندویچ حداقل یک نان دارد.")
                }
            }
            quantityAmount.value = value;
        }

        init();

    };
    sitePlusMinus();
})()


new Swiper('.testimonials-slider', {
    speed: 600,
    // loop: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false
    },
    direction_rl: true,
    slidesPerView: 'auto',
    pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
    },
    breakpoints: {
        100: {
            slidesPerView: 2,
            spaceBetween: 0
        },
        750: {
            slidesPerView: 2,
            spaceBetween: 0
        },
        1000: {
            slidesPerView: 4,
            spaceBetween: 0
        },
        1200: {
            slidesPerView: 6,
            spaceBetween: 0
        }
    }
});


function getPrices() {
    var total_price = 0
    var total_offer_price = 0
    const items = document.querySelectorAll('.total-price')
    items.forEach((item) => {
        var offerPrice = item.querySelector('.offer-price')
        const price = item.querySelector('.price')
        const count = Number(item.querySelector('.price-count').value)

        if (!offerPrice) {
            offerPrice = price
        }

        if (item.querySelector('.price-count').name === 'sandwiches') {
            const cleand_price = (cleanPrice(price)) + (8000 * (count - 1))
            const cleand_offer_price = (cleanPrice(offerPrice)) + (8000 * (count - 1))
            total_price += cleand_price
            total_offer_price += cleand_offer_price
        } else {
            const cleand_price = cleanPrice(price) * count
            const cleand_offer_price = cleanPrice(offerPrice) * count
            total_price += cleand_price
            total_offer_price += cleand_offer_price
        }

    })
    const priceLabel = document.querySelector('.price-label')
    priceLabel.textContent = total_price.toLocaleString('fa-IR') + ' تومان'

    const offerLabel = document.querySelector('.offer-label')
    offerLabel.textContent = total_offer_price.toLocaleString('fa-IR') + ' تومان'
}

function cleanPrice(text) {
    var price = text.innerHTML
    price = price.split("تومان")[0]
    price = price.split(",")
    price = Number(price[0] + price[1])
    return price
}

const form = document.querySelector('#form');
const submitBottom = document.querySelector('.submit-bottom');

submitBottom.addEventListener('click', function (event) {
    event.preventDefault();

    const firstName = document.getElementById('full_name').value.trim();
    const address = document.getElementById('address').value.trim();
    const phoneNumber = document.getElementById('phone').value.trim();

    if (firstName === '' || address === '' || phoneNumber === '') {
        alert('لطفا تمام فیلدها را پر کنید.');
        return;
    }

    if (!/^\d{11}$/.test(phoneNumber)) {
        alert('شماره تلفن باید 11 رقم باشد و فقط شامل اعداد باشد.');
        return;
    }
    form.submit()
})