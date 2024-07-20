from django.db import models


class SiteSettingModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام سایت')
    email = models.EmailField(verbose_name='ایمیل سایت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'تنظمات سایت'
        verbose_name_plural = 'تنظیمات های سایت'

    def __str__(self):
        return self.name


class SiteBannerModel(models.Model):
    image = models.ImageField(upload_to='banner', verbose_name='عکس بنر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'بنر سایت'
        verbose_name_plural = 'بنر های سایت'

    def __str__(self):
        return self.image.name
