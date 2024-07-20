from django.views.generic import TemplateView

from Home_Module.models import SiteSettingModel, SiteBannerModel
from Food_Module.models import SandwichModel, DrinkModel


class HomeView(TemplateView):
    template_name = 'Home_Module/home.html'

    def get_context_data(self, **kwargs):
        result = super(HomeView, self).get_context_data(**kwargs)
        result['site_setting'] = SiteSettingModel.objects.filter(is_active=True).first()
        result['site_banners'] = SiteBannerModel.objects.filter(is_active=True)

        result['special_sandwiches'] = SandwichModel.objects.filter(is_active=True, offer__gt=0, is_special=False)
        result['special_suggestions'] = SandwichModel.objects.filter(is_active=True, is_special=True)
        result['drinks'] = DrinkModel.objects.filter(is_active=True)
        result['best_selling_sandwiches'] = SandwichModel.objects.filter(is_active=True, is_special=False).order_by('-buy_count')[:10]
        result['all_sandwiches'] = SandwichModel.objects.filter(is_active=True, is_special=False)
        return result
