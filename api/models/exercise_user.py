from django.db import models
from api.models import BaseModel, UserModel, ExerciseModel


class ExerciseUserModel(BaseModel):
    exercise = models.ForeignKey(ExerciseModel, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserModel, related_name='exercise_user', on_delete=models.DO_NOTHING)
    achieved_score = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "tbl_exercise_user"

    def __str__(self):
        return "{} for {}".format(self.exercise.name, self.user.username)
