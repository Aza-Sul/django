from django.db import models


class PriceCard(models.Model):
    pc_value = models.CharField('Цена', max_length=20)
    pc_description = models.CharField('Описсание', max_length=200)

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = "Цены"


class PriceTable(models.Model):
    pt_title = models.CharField('Услуга', max_length=200)
    pt_old_price = models.CharField('Старая цена', max_length=200)
    pt_new_price = models.CharField('Новая цена', max_length=200)

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = "Услуги"
