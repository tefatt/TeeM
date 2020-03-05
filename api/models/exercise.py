from django.db import models
from django.contrib.postgres.fields import ArrayField
from api.models import BaseModel, TestSheetModel

TEXT = 0
AUDIO = 1
VIDEO = 2
MEDIA_FORMATS = (
    (TEXT, 'Textual question'),
    (AUDIO, 'Audio type question'),
    (VIDEO, 'Video type question')
)

TRUE_FALSE = 0
MATCHING = 1
ORDERING = 2
EXERCISE_TYPES = (
    (TRUE_FALSE, 'TRUE_FALSE'),
    (MATCHING, 'MATCHING'),
    (ORDERING, 'ORDERING')
)

GRAMMAR = 0
VOCABULARY = 1
SPELLING = 2
OTHER = 3
NATURE_TYPES = (
    (GRAMMAR, 'Grammar focused exercise'),
    (VOCABULARY, 'Vocabulary focused exercise'),
    (SPELLING, 'Spelling focused exercise'),
    (OTHER, 'Other type of exercise')
)


class ExerciseModel(BaseModel):
    # def user_directory_path(self, filename):
    #     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #     return 'user_{0}/{1}'.format(self.test_sheet.author.id, filename)

    name = models.CharField(max_length=30)
    test_sheet = models.ForeignKey(TestSheetModel, on_delete=models.DO_NOTHING, related_name='exercise')
    media = models.IntegerField(choices=MEDIA_FORMATS, default=TEXT)
    type = models.IntegerField(choices=EXERCISE_TYPES, default=TRUE_FALSE)
    # questions = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    # questions = ArrayField(base_field=models.CharField(max_length=500))
    # answers = models.ForeignKey(AnswerModel, on_delete=models.CASCADE)
    # answers = ArrayField(base_field=models.CharField(max_length=200))
    # conjunction = ArrayField(base_field=models.PositiveSmallIntegerField(),
    #                          help_text="Connection between questions and answers")
    # pauses = ArrayField(base_field=models.FloatField(), null=True, blank=True,
    #                     help_text="Time points in it, that specify when to display a question, if the media is a video")
    # max_score = models.PositiveSmallIntegerField()
    # mp3 = models.FileField(upload_to=user_directory_path)
    material_url = models.URLField(null=True, blank=True, help_text="If user provides a link to an audio or video file")
    nature = models.IntegerField(choices=NATURE_TYPES, default=GRAMMAR)
    public = models.BooleanField(default=False, help_text="Does the author want this object to be publicly accessible")

    class Meta:
        db_table = "tbl_exercises"

    def __str__(self):
        return "{} in {}".format(self.name, self.test_sheet.name)
