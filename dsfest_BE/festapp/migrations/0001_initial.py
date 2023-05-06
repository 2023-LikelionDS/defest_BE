# Generated by Django 4.2.1 on 2023-05-06 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pinned_order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-pinned_order', '-created'],
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='media/blog/default_image.jpg', upload_to='blog')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festapp.blog')),
            ],
        ),
    ]
