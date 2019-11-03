# Generated by Django 2.1.8 on 2019-11-03 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/image')),
                ('price', models.FloatField()),
                ('is_delete', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Goods_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='goods_type',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.Type'),
        ),
    ]
