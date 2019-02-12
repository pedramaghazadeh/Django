from django.db import models
import PIL
# Create your models here.
class Product(models.Model):
    img         = models.ImageField()
    crop_up     = models.IntegerField(blank=True ,null=True)
    crop_left   = models.IntegerField(blank=True ,null=True)
    crop_low    = models.IntegerField(blank=True ,null=True)
    crop_right  = models.IntegerField(blank=True ,null=True)
    resize_x    = models.IntegerField(blank=True ,null=True)
    resize_y    = models.IntegerField(blank=True ,null=True)
    rotate      = models.DecimalField(decimal_places=2, max_digits=10000, blank=True ,null=True)
    bw          = models.BooleanField(default=False)
    share       = models.BooleanField(default=True)
    Admin_share = models.BooleanField(default=True)

