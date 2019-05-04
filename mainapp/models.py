from django.db import models

# Create your models here.


class ImageCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.CharField(verbose_name='описание', max_length=128, blank=True)
    is_active = models.BooleanField(verbose_name='активная категория', default=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    short_desc = models.CharField(verbose_name='короткое описание', max_length=128, blank=True)
    description = models.CharField(verbose_name='описание', max_length=256, blank=True)
    is_active = models.BooleanField(verbose_name='активная картинка', default=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)

