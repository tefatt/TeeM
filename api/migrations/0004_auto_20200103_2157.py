# Generated by Django 3.0 on 2020-01-03 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180507_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommodel',
            name='medium_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.LanguageModel'),
        ),
        migrations.AlterField(
            model_name='classroommodel',
            name='teacher',
            field=models.ForeignKey(help_text='If null, tandem model is applied', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.TeacherModel'),
        ),
        migrations.AlterField(
            model_name='exercisemodel',
            name='test_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.TestSheetModel'),
        ),
        migrations.AlterField(
            model_name='exerciseusermodel',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.ExerciseModel'),
        ),
        migrations.AlterField(
            model_name='exerciseusermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='exercise_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languageusermodel',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.LanguageModel'),
        ),
        migrations.AlterField(
            model_name='languageusermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.InstitutionModel'),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='teaching_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.LanguageModel'),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testsheetmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testsheetmodel',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.ClassroomModel'),
        ),
        migrations.AlterField(
            model_name='tutorialmodel',
            name='test_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.TestSheetModel'),
        ),
        migrations.AlterField(
            model_name='unitmodel',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.ClassroomModel'),
        ),
        migrations.AlterField(
            model_name='unitmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='native_language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.LanguageModel'),
        ),
    ]