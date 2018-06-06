from django.db import models
from api.models import BaseModel, UserModel, TeacherModel, LanguageModel


class ClassroomModel(BaseModel):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(TeacherModel, null=True, help_text="If null, tandem model is applied")
    user = models.ManyToManyField(UserModel, through='UnitModel', related_name='classroom')
    medium_language = models.ForeignKey(LanguageModel)

    class Meta:
        db_table = "tbl_classroom"

    def __str__(self):
        return self.name
