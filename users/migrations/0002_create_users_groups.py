from django.db import migrations
from django.contrib.auth.models import Group, Permission


def create_users_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Create Staff Group
    staff_group, created = Group.objects.get_or_create(name='Staff')
    if created:
        permissions = Permission.objects.filter(codename__in=['view_user', 'add_user', 'change_user', 'delete_user'])
        staff_group.permissions.set(permissions)

    # Create Artists Group
    artists_group = Group.objects.get_or_create(name='Artists')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users_groups),
    ]