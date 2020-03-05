from django.db import models
from api.models import BaseModel, TestSheetModel


class TutorialModel(BaseModel):
    # def user_directory_path(self, filename):
    #     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #     return 'user_{0}/{1}'.format(self.test_sheet.author.id, filename)

    name = models.CharField(max_length=30)
    test_sheet = models.ForeignKey(TestSheetModel, on_delete=models.DO_NOTHING, related_name='tutorial')
    content = models.TextField()
    # mp3 = models.FileField(upload_to=user_directory_path)
    public = models.BooleanField(default=False, help_text="Does the author want this object to be publicly accessible")

    class Meta:
        db_table = "tbl_tutorial"

    def __str__(self):
        return "{} in {}".format(self.name, self.test_sheet.name)
