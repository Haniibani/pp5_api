from django.db import migrations

def add_predefined_tags(apps, schema_editor):
    Tag = apps.get_model('tags', 'Tag')
    predefined_tags = [
        'Technology', 'Travel', 'Food', 'Fashion', 'Art',
        'Science', 'Health', 'Music', 'Sports', 'Nature',
        'Business', 'Education', 'Photography', 'History',
        'Literature', 'Movies', 'Gaming', 'Cooking', 'Fitness'
    ]
    for tag_name in predefined_tags:
        Tag.objects.get_or_create(name=tag_name)

class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_predefined_tags),
    ]