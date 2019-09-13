from django.db import models


class Core(models.Model):
    title = models.CharField('عنوان وب سایت', max_length=200)
    desc = models.CharField('توضیح کوتاه', max_length=200)
    address = models.TextField('آدرس', blank=True)

    about = models.TextField('درباره ما')
    contact = models.TextField('تماس با ما')

    location = models.TextField('آدرس نقشه گوگل', help_text='در صورت داشتن مکان فیزیکی می توانید آدرس گوگل خود را وارد نمایید', blank=True)

    class Meta:
        verbose_name = 'اطلاعات وب سایت'
        verbose_name_plural = 'مشخصات وب سایت'

    def __str__(self):
        return self.title