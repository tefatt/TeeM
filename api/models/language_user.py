from django.db import models
from api.models import BaseModel, UserModel, LanguageModel

A1 = 0
A2 = 1
B1 = 2
B2 = 3
C1 = 4
C2 = 5
PROFICIENCY_LEVELS = (
    (A1, 'A1'),
    (A2, 'A2'),
    (B1, 'B1'),
    (B2, 'B2'),
    (C1, 'C1'),
    (C2, 'C2')
)


class LanguageUserModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(LanguageModel, on_delete=models.DO_NOTHING)
    level = models.IntegerField(choices=PROFICIENCY_LEVELS)

    class Meta:
        db_table = "tbl_language_user"

    def __str__(self):
        return "{} at {}".format(self.user.username, self.language.name)
