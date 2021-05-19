from django.db import models

class Document(models.Model):

    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    file = models.FileField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_expired = models.DateField()
    status = models.CharField(choices=(
        ('active', 'active'),
        ('dead', 'dead')
    ), max_length=50, default='active')
    document_root = models.CharField(choices=(
        ('public', 'public'),
        ('private', 'private'),
        ('secret', 'secret'),
        ('top-secret', 'top-secret')
    ),max_length=50)

    def __str__(self):
        return self.title