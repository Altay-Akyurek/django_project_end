# Generated by Django 4.2.3 on 2023-08-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_treecertificate_planting_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treecertificate',
            name='planting_area',
            field=models.CharField(choices=[('adana', 'Adana'), ('adiyaman', 'Adıyaman'), ('afyonkarahisar', 'Afyonkarahisar'), ('agri', 'Ağrı'), ('amasya', 'Amasya'), ('ankara', 'Ankara'), ('antalya', 'Antalya'), ('artvin', 'Artvin'), ('aydin', 'Aydın'), ('balikesir', 'Balıkesir'), ('bilecik', 'Bilecik'), ('bingol', 'Bingöl'), ('bitlis', 'Bitlis'), ('bolu', 'Bolu'), ('burdur', 'Burdur'), ('bursa', 'Bursa'), ('canakkale', 'Çanakkale'), ('cankiri', 'Çankırı'), ('corum', 'Çorum'), ('denizli', 'Denizli'), ('diyarbakir', 'Diyarbakır'), ('edirne', 'Edirne'), ('elazig', 'Elazığ'), ('erzincan', 'Erzincan'), ('erzurum', 'Erzurum'), ('eskisehir', 'Eskişehir'), ('gaziantep', 'Gaziantep'), ('giresun', 'Giresun'), ('gumushane', 'Gümüşhane'), ('hakkari', 'Hakkâri'), ('hatay', 'Hatay'), ('isparta', 'Isparta'), ('mersin', 'Mersin'), ('istanbul', 'İstanbul'), ('izmir', 'İzmir'), ('kars', 'Kars'), ('kastamonu', 'Kastamonu'), ('kayseri', 'Kayseri'), ('kirklareli', 'Kırklareli'), ('kirsehir', 'Kırşehir'), ('kocaeli', 'Kocaeli'), ('konya', 'Konya'), ('kutahya', 'Kütahya'), ('malatya', 'Malatya'), ('manisa', 'Manisa'), ('kahramanmaras', 'Kahramanmaraş'), ('mardin', 'Mardin'), ('mugla', 'Muğla'), ('mus', 'Muş'), ('nevsehir', 'Nevşehir'), ('nigde', 'Niğde'), ('ordu', 'Ordu'), ('rize', 'Rize'), ('sakarya', 'Sakarya'), ('samsun', 'Samsun'), ('siirt', 'Siirt'), ('sinop', 'Sinop'), ('sivas', 'Sivas'), ('tekirdag', 'Tekirdağ'), ('tokat', 'Tokat'), ('trabzon', 'Trabzon'), ('tunceli', 'Tunceli'), ('sanliurfa', 'Şanlıurfa'), ('usak', 'Uşak'), ('van', 'Van'), ('yozgat', 'Yozgat'), ('zonguldak', 'Zonguldak'), ('aksaray', 'Aksaray'), ('bayburt', 'Bayburt'), ('karaman', 'Karaman'), ('kirikkale', 'Kırıkkale'), ('batman', 'Batman'), ('sirnak', 'Şırnak'), ('bartin', 'Bartın'), ('ardahan', 'Ardahan'), ('igdir', 'Iğdır'), ('yalova', 'Yalova'), ('karabuk', 'Karabük'), ('kilis', 'Kilis'), ('osmaniye', 'Osmaniye'), ('duzce', 'Düzce')], max_length=100),
        ),
    ]