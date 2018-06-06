from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import BaseModel, LanguageModel
from django.core.validators import RegexValidator

MALE = 0
FEMALE = 1
UNDECIDED = 2
GENDER_TYPES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (UNDECIDED, 'Undecided')
)

HIGH_SCHOOL = 0
BSC = 1
MSC = 2
PHD = 3
OTHER = 4
EDUCATION_TYPES = (
    (HIGH_SCHOOL, 'High School'),
    (BSC, 'Bch'),
    (MSC, 'Msc'),
    (PHD, 'Phd'),
    (OTHER, 'Other Education Level')
)


class UserModel(BaseModel, AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?\d{9,15}$',
                                 message="Phone number format is e.g.: '+999999999'. Up to 15 digits allowed.")
    id = models.AutoField(primary_key=True)
    native_language = models.ForeignKey(LanguageModel, null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_TYPES, default=MALE)
    other_languages = models.ManyToManyField(LanguageModel, through='LanguageUserModel', related_name='user_lang')
    educations = models.IntegerField(choices=EDUCATION_TYPES, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        db_table = "tbl_user"

    def __str__(self):
        return "{}".format(self.username)
