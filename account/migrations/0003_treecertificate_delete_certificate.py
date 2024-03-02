# Generated by Django 4.2.3 on 2023-07-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_certificate_delete_certificateapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_type', models.CharField(choices=[('standart', 'Standart'), ('dugun_hediyesi', 'Düğün Hediyesi')], max_length=50)),
                ('tree_type', models.CharField(choices=[('zeytin', 'Zeytin Ağacı'), ('antep_fistik', 'Antep Fıstık Ağacı')], max_length=50)),
                ('tree_quantity', models.PositiveIntegerField()),
                ('planting_area', models.CharField(choices=[('kilis', 'Kilis'), ('mardin', 'Mardin'), ('sanliurfa', 'Şanlıurfa')], max_length=100)),
                ('recipient_name', models.CharField(max_length=200)),
                ('delivery_option', models.CharField(choices=[('kargo_50tl', 'Kargo (50 TL)'), ('ucretsiz', 'Ücretsiz Kargo')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
    ]
