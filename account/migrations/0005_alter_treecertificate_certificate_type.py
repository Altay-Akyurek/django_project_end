# Generated by Django 4.2.3 on 2023-07-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_treecertificate_certificate_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treecertificate',
            name='certificate_type',
            field=models.CharField(choices=[('standart', 'Standart'), ('dugun_hediyesi', 'Düğün Hediyesi'), ('adima_bagis_yapmak_istiyorum', 'Adıma Bağış Yapmak İstiyorum'), ('kalkinma_yatirim_bankasi_gelir_getirici_fidan_dikim_projesi', 'Kalkınma Yatırım Bankası Gelir Getirici Fidan Dikim Projesi'), ('mezuniyet', 'Mezuniyet'), ('köklerimiz_bu_topraklarda', 'Köklerimiz Bu Topraklarda'), ('Yetimler_için_fidan_bağişi', 'Yetimler İçin Fidan Bağışı'), ('hoşgeldin_bebek', 'Hoşgeldin Bebek '), ('bebek_hediyesi', 'Bebek Hediyesi (Bebeğimizin size hediyesi) '), ('sünnet_merasimi', 'Sünnet Merasimi '), ('doğum_günü', 'Doğum Günü - DAV '), ('bayram', 'Bayram  '), ('doğum_günü_kutlamasına_katılım', 'Doğum Günü Kutlamasına Katılım '), ('baş_sağliği', 'Baş Sağlığı (Merhum) '), ('baş_sağlığı', 'Baş Sağlığı (Merhume) '), ('geçmiş_olsun', 'Geçmiş Olsun '), ('teşekkür', 'Teşekkür '), ('yeni_iş_tebriği', 'Yeni İş Tebriği '), ('yeni_unvan', 'Yeni Unvan '), ('açılış', 'Açılış '), ('yeni_görev', 'Yeni Görev '), ('turkey_korea_friendship_forest', 'Turkey - Korea Friendship Forest '), ('yil_hatira_ormanlari', 'İTÜ 250. Yıl Hatıra Ormanları (3. kişiler için hediye) '), ('yil_hatira_ormanlari', 'İTÜ 250. Yıl Hatıra Ormanları '), ('çanakkale_mahmud_esad_coşan_hatira_ormani', 'Çanakkale Mahmud Esad Coşan Hatıra Ormanı '), ('TİF_Hatıra_OrmanıKendi_Adıma', 'TİF Hatıra Ormanı - Kendi Adıma '), ('dugun', 'Düğün '), ('dugun', 'Düğün '), ('dugun', 'Düğün '), ('dugun', 'Düğün '), ('dugun', 'Düğün '), ('dugun', 'Düğün '), ('dugun', 'Düğün ')], max_length=200),
        ),
    ]
