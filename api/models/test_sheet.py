from django.db import models
from api.models import BaseModel, UserModel, ClassroomModel

VERY_EASY = 0
EASY = 1
MEDIUM = 2
DIFFICULT = 3
VERY_DIFFICULT = 4
DIFFICULTY_TYPES = (
    (VERY_EASY, 'Very Easy'),
    (EASY, 'Easy'),
    (MEDIUM, 'Medium'),
    (DIFFICULT, 'Difficult'),
    (VERY_DIFFICULT, 'Very Difficult')
)


class TestSheetModel(BaseModel):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(UserModel)
    classroom = models.ForeignKey(ClassroomModel)
    difficulty = models.IntegerField(choices=DIFFICULTY_TYPES, default=MEDIUM)

    class Meta:
        db_table = "tbl_test_sheet"

    def __str__(self):
        return "{} in {}".format(self.name, self.classroom.name)
