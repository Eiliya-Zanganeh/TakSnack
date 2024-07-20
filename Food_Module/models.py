from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class SandwichModel(models.Model):
    # if change field, change query in Order_Module . views . CartView
    name = models.CharField(max_length=100, verbose_name='نام ساندویچ')
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت ساندویچ')
    image = models.ImageField(upload_to='sandwich')
    offer_price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت پس از تخفیف', null=True,
                                      blank=True)
    offer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='درصد تخفیف',
                                null=True, blank=True)
    is_special = models.BooleanField(default=False, verbose_name='پیشنهاد ویژه')
    buy_count = models.IntegerField(default=0, verbose_name='تعداد فروش')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'ساندویچ'
        verbose_name_plural = 'ساندویچ ها'

    def save(self, *args, **kwargs):
        if not self.offer and not self.offer_price:
            ...
        elif self.offer and self.offer_price:
            ...
        else:
            if (self.offer == '') or (self.offer is None):
                self.offer = 100 - (round(self.offer_price * 100 / self.price))
            elif self.offer_price == '' or self.offer_price is None:
                self.offer_price = self.price - (self.price * self.offer / 100)
        return super().save(args, kwargs)

    def __str__(self):
        return self.name


class DrinkModel(models.Model):
    # if change field, change query in Order_Module . views . CartView
    name = models.CharField(max_length=100, verbose_name='نام نوشیدنی')
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت نوشیدنی')
    image = models.ImageField(upload_to='drink')
    offer_price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت پس از تخفیف', null=True,
                                      blank=True)
    offer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='درصد تخفیف',
                                null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'نوشیدنی'
        verbose_name_plural = 'نوشیدنی ها'

    def save(self, *args, **kwargs):
        if not self.offer and not self.offer_price:
            ...
        elif self.offer and self.offer_price:
            ...
        else:
            if (self.offer == '') or (self.offer is None):
                self.offer = 100 - (round(self.offer_price * 100 / self.price))
            elif self.offer_price == '' or self.offer_price is None:
                self.offer_price = self.price - (self.price * self.offer / 100)
        return super().save(args, kwargs)

    def __str__(self):
        return self.name


class SauceModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام سس')
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت سس')
    image = models.ImageField(upload_to='sauce')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'سس'
        verbose_name_plural = 'سس ها'

    def __str__(self):
        return self.name
