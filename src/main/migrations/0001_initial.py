# Generated by Django 2.2.16 on 2021-01-13 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_data', models.CharField(default=None, max_length=256, null=True)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ItemMenu')),
            ],
        ),
        migrations.CreateModel(
            name='ItemName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('leng', models.PositiveSmallIntegerField(choices=[(2, 'en'), (1, 'ru')])),
                ('item_menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ItemMenu')),
            ],
        ),
    ]
