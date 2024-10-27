from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achatenligne', '0004_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.PositiveIntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achatenligne.product')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='WebsiteFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.PositiveIntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
