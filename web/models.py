from __future__ import unicode_literals
import uuid
from django.db import models
from web.variables import phone_regex


TIME =(
    ("","Time"),
    ("Anytime","Anytime"),
    ("Morning","Morning"),
    ("Afternoon","Afternoon"),
)

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, )
    phone = models.CharField(validators=[phone_regex],max_length=255, )
    email = models.EmailField()
    message = models.CharField(max_length=128)
    date = models.DateField()
    time = models.CharField(max_length=128,choices=TIME)
    vehicle_number = models.CharField(max_length=20)
    kms_driven=models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)

    class Meta:
        db_table = 'service'
        verbose_name = ('Service')
        verbose_name_plural = ('Services')
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.name)