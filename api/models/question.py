from django.db import models
from api.models import BaseModel, ExerciseModel


class QuestionModel(BaseModel):
    name = models.CharField(max_length=200)
    time_point = models.FloatField(null=True, blank=True)
    max_score = models.PositiveSmallIntegerField()
    exercise = models.ForeignKey(ExerciseModel, related_name='questions', on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_questions"

    def __str__(self):
        return "{} in {}".format(self.name, self.exercise.name)
