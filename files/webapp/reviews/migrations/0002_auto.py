from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from reviews.models import User

        DJANGO_SU_NAME = "dseadmin"
        DJANGO_SU_EMAIL = "dse@dse.com"
        DJANGO_SU_PASSWORD = "totti</3blasi"

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]

