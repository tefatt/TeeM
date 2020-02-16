from django.db import models
from api.models import BaseModel, QuestionModel


class AnswerModel(BaseModel):
    name = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(QuestionModel, related_name='answer', on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_answers"

    def __str__(self):
        return "{} for {}".format(self.name, self.question.name)
