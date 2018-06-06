from django.db import models
from api.models import BaseModel


class LanguageModel(BaseModel):
    name = models.CharField(max_length=20)
    flavour = models.CharField(max_length=20, blank=True, null=True, help_text="For defining dialect or region")
    voice_support = models.BooleanField(default=True, help_text="Does a text to speech service like Amazon Polly exist")

    class Meta:
        db_table = "tbl_language"

    def __str__(self):
        return "{} {}".format(self.name, self.flavour)
