from django.db import models
from api.models import BaseModel, UserModel, ClassroomModel


class UnitModel(BaseModel):
    user = models.ForeignKey(UserModel, related_name='unit')
    classroom = models.ForeignKey(ClassroomModel)
    score = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "tbl_unit"

    def __str__(self):
        return "{} in {}".format(self.user.username, self.classroom.name)
