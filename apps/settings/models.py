from django.db import models

# full_name = '' - змеинный регистр

# FullName = ''  - верблюжий регистр
# Create your models here.
class About(models.Model):
    photo = models.ImageField(
        upload_to='image/',
        verbose_name='Фото профиля'
    )
    fullname = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    direction = models.CharField(
        max_length=255,
        verbose_name='Направление'
    )
    
    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки профиля"