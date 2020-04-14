
from django.db import models
from django.utils import timezone


# Create your models here.
class CrochetHook(models.Model):
    crochethook_size = models.CharField(max_length=5)
    material = models.CharField(max_length=10)
    count = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.crochethook_size)


class Yarn(models.Model):
    crochethook_size = models.ForeignKey(CrochetHook, on_delete=models.CASCADE, related_name='yarns')
    yarn_color = models.CharField(max_length=100)
    yarn_texture = models.TextField()
    yarn_amount = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.crochethook_size)


class Gift(models.Model):
    crochethook_size = models.ForeignKey(CrochetHook, on_delete=models.CASCADE, related_name='gifts')
    yarn_color = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100)
    p_description = models.TextField()
    gift_size = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.crochethook_size)

