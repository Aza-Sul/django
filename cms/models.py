from django.db import models


class CmsSlider(models.Model):
    cms_image = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField('Заголовок', max_length=200)
    cms_text = models.CharField('Текст', max_length=200)
    cms_active = models.CharField('Активный', max_length=200, null=True, default='-')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
