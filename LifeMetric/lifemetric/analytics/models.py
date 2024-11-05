from django.db import models

CONDITION_CHOICES = [
    ('new', 'Novo'),
    ('good', 'Em bom estado'),
    ('worn', 'Com desgaste leve'),
    ('repair', 'Necessita reparo'),
    ('damaged', 'Danificado'),
]

class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    date_acquired = models.DateField()
    date_manufactured = models.DateField(blank=True, null=True)
    date_expiration = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    current_location = models.CharField(max_length=100)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

class AssetPhoto(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='asset_photos/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo of {self.asset.name} uploaded on {self.date_uploaded}"

from django.contrib.auth.models import User

class AssetTracking(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateField()
    date_returned = models.DateField(blank=True, null=True)
    condition_at_return = models.CharField(max_length=50, choices=CONDITION_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.asset.name} tracking by {self.user.username}"
