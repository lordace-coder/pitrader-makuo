from django.db import models

# Create your models here.

class passpharse(models.Model):
    pharse = models.TextField('passpharse input', max_length=20000, blank=True, null=True)
    is_checked = models.BooleanField('if the passpharse is checked', default=False)
    status = models.CharField('checed status', default='check',max_length=50)


    def __str__(self):
        if self.is_checked == False:
            self.status = 'check'
            return '---check'
        else:
            self.status = 'checked'
            return '---checked'

    
        