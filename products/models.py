from django.db import models
from django.utils.translation import ugettext_lazy
from tinymce.models import HTMLField
import datetime
import psutil
class ProductCategory(models.Model):
    name = models.CharField(ugettext_lazy('name'), max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Products categories'


class Product(models.Model):
    name = models.CharField(ugettext_lazy('name'), max_length=86)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    description = HTMLField(ugettext_lazy('description'))
    image = models.ImageField(default=None, upload_to='products_images/', blank=True, null=True)
    url = models.URLField(max_length=250, default=None, blank=True, null=True)

    # def image_img(self):
    #     if self.image:
    #         return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
    #     else:
    #         return '(Нет изображения)'
    #
    # image_img.short_description = 'Картинка'
    # image_img.allow_tags = True
    #
    # image_img.short_description = 'Thumb'
    # image_img.allow_tags = True

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')

    def image_img(self):
        if self.image:
            return u'< img src="%s" width="100px"/>' % self.image.url
        else:
            return '(none)'

    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)



    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Фотографія"
        verbose_name_plural = "Фотографії"

class News(models.Model):
    tittle = models.CharField(ugettext_lazy('tittle'), max_length=228)
    short_descr = HTMLField(ugettext_lazy('short_descr'))
    description = HTMLField(ugettext_lazy('description'))

    date = models.DateField(default=datetime.date.today)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.tittle, self.date)

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"

class GalleryImage(models.Model):
    tittle = models.CharField(ugettext_lazy('tittle'), max_length=228)
    description = HTMLField(ugettext_lazy('description'))
    image = models.ImageField(default=None, upload_to='products_images/', blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.tittle

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

