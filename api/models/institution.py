from django.db import models
from api.models import BaseModel


class InstitutionModel(BaseModel):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    web_address = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "tbl_institution"

    def __str__(self):
        return self.name
