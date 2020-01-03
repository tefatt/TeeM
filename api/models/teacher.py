from django.db import models
from api.models import BaseModel, UserModel, LanguageModel, InstitutionModel


class TeacherModel(BaseModel):
    user = models.OneToOneField(UserModel, on_delete=models.DO_NOTHING)
    teaching_language = models.ForeignKey(LanguageModel, on_delete=models.DO_NOTHING)
    institution = models.ForeignKey(InstitutionModel, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "tbl_teacher"

    def __str__(self):
        return "{}".format(self.user.username)
