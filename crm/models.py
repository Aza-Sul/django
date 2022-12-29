from django.db import models


class StatusCrm(models.Model):
    status_name = models.CharField('Название статуса', max_length=200)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField('Имя', max_length=200)
    order_phone = models.CharField('Телефон', max_length=200)
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_bindings = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заявка")
    comment_text = models.TextField('Текст комментария')
    comment_dt = models.DateTimeField('Дата создания', auto_now=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
