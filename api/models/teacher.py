from django.db import models
from api.models import BaseModel, UserModel, LanguageModel, InstitutionModel


class TeacherModel(BaseModel):
    user = models.OneToOneField(UserModel)
    teaching_language = models.ForeignKey(LanguageModel)
    institution = models.ForeignKey(InstitutionModel, null=True, blank=True)

    class Meta:
        db_table = "tbl_teacher"

    def __str__(self):
        return "{}".format(self.user.username)
