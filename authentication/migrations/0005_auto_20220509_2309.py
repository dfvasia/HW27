# Generated by Django 4.0.4 on 2022-05-09 20:09
import datetime

from django.db import migrations


def forwards_func(apps, schema_editor):
    DATE = datetime.date.today()
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Person = apps.get_model("authentication", "User")
    db_alias = schema_editor.connection.alias
    for person in Person.objects.all():
        data = DATE
        person.birth_date = data.replace(year=data.year - int(person.age))
        person.birth_date = str(data - datetime.timedelta(days=(365*int(person.age))))
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_email'),
    ]

    operations = [
        migrations.RunPython(forwards_func, ),
    ]