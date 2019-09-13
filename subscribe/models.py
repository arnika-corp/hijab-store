from django.db import models
from django.utils import timezone


class Subscribe(models.Model):
    email = models.EmailField('پست الکترونیک')
    created_at = models.DateTimeField('تاریخ ثبت', default=timezone.now)

    class Meta:
        verbose_name = 'عضو خبرنامه'
        verbose_name_plural = 'اعضا خبرنامه'
    
    def __str__(self):
        return self.email