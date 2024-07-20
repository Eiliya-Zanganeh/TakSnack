from django.db import models


class OrderModel(models.Model):
    full_name = models.CharField(max_length=500, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=15, verbose_name='شماره تماس')
    address = models.TextField(verbose_name='آدرس')
    description = models.TextField(verbose_name='سفارش')
    date = models.DateField(verbose_name='زمان', auto_now_add=True)
    is_ordered = models.BooleanField(default=False, verbose_name='انجام شده / انجام نشده')

    def __str__(self):
        return f'{self.full_name} - {self.date}'

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'