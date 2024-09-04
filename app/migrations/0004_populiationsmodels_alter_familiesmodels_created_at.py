# Generated by Django 5.1 on 2024-08-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_familiesmodels_r504a_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopuliationsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r401', models.IntegerField(verbose_name='Nomor Urut ART')),
                ('r402', models.CharField(max_length=128, verbose_name='Nama ART')),
                ('r403', models.CharField(blank=True, max_length=16, null=True, verbose_name='Nomor Induk Kependudukan (NIK)')),
                ('r404', models.CharField(choices=[('1', 'Tinggal Bersama Keluarga'), ('2', 'Meninggal'), ('3', 'Tidak Tinggal Bersama Keluarga/Pindah ke Wilayah (Daerah) Lain di Indonesia'), ('4', 'Tidak Tinggal Bersama Keluarga/Pindah ke Luar Negeri'), ('5', 'Anggota Keluarga Baru'), ('6', 'Tidak Ditemukan')], max_length=1, verbose_name='Keberadaan anggota keluarga')),
                ('r405', models.CharField(blank=True, choices=[('1', 'Laki-laki'), ('2', 'Perempuan')], max_length=1, null=True, verbose_name='Jenis Kelamin')),
                ('r406', models.DateField(blank=True, null=True, verbose_name='Tanggal Lahir')),
                ('r408', models.CharField(blank=True, choices=[('1', 'Belum Kawin'), ('2', 'Kawin/Nikah'), ('3', 'Cerai Hidup'), ('4', 'Cerai Mati')], max_length=1, null=True, verbose_name='Status Perkawinan')),
                ('r409', models.CharField(blank=True, choices=[('1', 'Kepala keluarga'), ('2', 'Istri/suami'), ('3', 'Anak'), ('4', 'Menantu'), ('5', 'Cucu'), ('6', 'Orangtua/mertua'), ('7', 'Pembantu/sopir'), ('8', 'Lainnya')], max_length=1, null=True, verbose_name='Status hubungan dengan kepala keluarga')),
                ('r411', models.CharField(blank=True, choices=[('1', 'Tidak Memiliki'), ('2', 'Akta Kelahiran'), ('3', 'KIA'), ('4', 'KTP')], max_length=1, null=True, verbose_name='Apakah memiliki kartu identitas?')),
                ('r412', models.CharField(blank=True, choices=[('1', 'Tidak/belum pernah sekolah'), ('2', 'Masih sekolah'), ('3', 'Tidak bersekolah lagi')], max_length=1, null=True, verbose_name='Partisipasi sekolah')),
                ('r415', models.CharField(blank=True, choices=[('1', 'Paket A'), ('2', 'SDLB'), ('3', 'SD'), ('4', 'MI'), ('5', 'SPM/PDF Ula'), ('6', 'Paket B'), ('7', 'SMP LB'), ('8', 'SMP'), ('9', 'MTs'), ('10', 'SPM/PDF Wustha'), ('11', 'Paket C'), ('12', 'SMLB'), ('13', 'SMA'), ('14', 'MA'), ('15', 'SMK'), ('16', 'MAK'), ('17', 'SPM/PDF Ulya'), ('18', 'D1/D2/D3'), ('19', 'DV/S1'), ('20', 'Profesi'), ('21', 'S2'), ('22', 'S3'), ('23', 'Tidak Punya Ijazah SD')], max_length=2, null=True, verbose_name='Ijazah/STTB tertinggi yang dimiliki')),
                ('r416a', models.CharField(blank=True, choices=[('1', 'Ya'), ('2', 'Tidak')], max_length=1, null=True, verbose_name='Apakah bekerja/membantu bekerja selama seminggu yang lalu?')),
                ('r416b', models.IntegerField(blank=True, null=True, verbose_name='Jumlah Jam (Per Minggu)')),
                ('r417', models.CharField(blank=True, choices=[('01', 'Pertanian tanaman padi & palawija'), ('02', 'Hortikultura'), ('03', 'Perkebunan'), ('04', 'Perikanan'), ('05', 'Peternakan'), ('06', 'Kehutanan & pertanian lainnya'), ('07', 'Pertambangan/penggalian'), ('08', 'Industri pengolahan'), ('09', 'Pengadaan listrik, gas, uap/air panas, dan udara dingin'), ('10', 'Pengelolaan air, pengelolaan air limbah, pengelolaan dan daur ulang sampah, dan aktivitas remediasi'), ('11', 'Konstruksi'), ('12', 'Perdagangan besar dan eceran, reparasi dan perawatan mobil dan sepeda motor'), ('13', 'Pengangkutan dan pergudangan'), ('14', 'Penyediaan akomodasi & makan minum'), ('15', 'Informasi & komunikasi'), ('16', 'Keuangan & asuransi'), ('17', 'Real estate'), ('18', 'Aktivitas profesional, ilmiah, dan teknis'), ('19', 'Aktivitas penyewaan dan sewa guna tanpa hak opsi, ketenagakerjaan, agen perjalanan, dan penunjang usaha lainnya'), ('20', 'Administrasi pemerintahan, pertahanan, dan jaminan sosial wajib'), ('21', 'Pendidikan'), ('22', 'Aktivitas kesehatan manusia dan aktivitas sosial'), ('23', 'Kesenian, hiburan, dan rekreasi'), ('24', 'Aktivitas jasa lainnya'), ('25', 'Aktivitas keluarga sebagai pemberi kerja'), ('26', 'Aktivitas badan internasional dan badan ekstra internasional lainnya')], max_length=2, null=True, verbose_name='Lapangan usaha dari pekerjaan utama')),
                ('r418', models.CharField(blank=True, choices=[('1', 'Berusaha sendiri'), ('2', 'Berusaha dibantu buruh tidak tetap/tidak dibayar'), ('3', 'Berusaha dibantu buruh tetap/buruh dibayar'), ('4', 'Buruh/karyawan/pegawai swasta'), ('5', 'PNS/TNI/Polri/ BUMN/BUMD/pejabat negara'), ('6', 'Pekerja bebas pertanian'), ('7', 'Pekerja bebas non pertanian'), ('8', 'Pekerja keluarga/tidak dibayar')], max_length=1, null=True, verbose_name='Status dalam pekerjaan utama')),
                ('r420a', models.CharField(blank=True, choices=[('1', 'Ya'), ('2', 'Tidak')], max_length=1, null=True, verbose_name='Apakah memiliki usaha sendiri/bersama?')),
                ('r421', models.CharField(blank=True, choices=[('01', 'Pertanian tanaman padi & palawija'), ('02', 'Hortikultura'), ('03', 'Perkebunan'), ('04', 'Perikanan'), ('05', 'Peternakan'), ('06', 'Kehutanan & pertanian lainnya'), ('07', 'Pertambangan/penggalian'), ('08', 'Industri pengolahan'), ('09', 'Pengadaan listrik, gas, uap/air panas, dan udara dingin'), ('10', 'Pengelolaan air, pengelolaan air limbah, pengelolaan dan daur ulang sampah, dan aktivitas remediasi'), ('11', 'Konstruksi'), ('12', 'Perdagangan besar dan eceran, reparasi dan perawatan mobil dan sepeda motor'), ('13', 'Pengangkutan dan pergudangan'), ('14', 'Penyediaan akomodasi & makan minum'), ('15', 'Informasi & komunikasi'), ('16', 'Keuangan & asuransi'), ('17', 'Real estate'), ('18', 'Aktivitas profesional, ilmiah, dan teknis'), ('19', 'Aktivitas penyewaan dan sewa guna tanpa hak opsi, ketenagakerjaan, agen perjalanan, dan penunjang usaha lainnya'), ('20', 'Administrasi pemerintahan, pertahanan, dan jaminan sosial wajib'), ('21', 'Pendidikan'), ('22', 'Aktivitas kesehatan manusia dan aktivitas sosial'), ('23', 'Kesenian, hiburan, dan rekreasi'), ('24', 'Aktivitas jasa lainnya'), ('25', 'Aktivitas keluarga sebagai pemberi kerja'), ('26', 'Aktivitas badan internasional dan badan ekstra internasional lainnya')], max_length=2, null=True, verbose_name='Lapangan usaha dari usaha utama')),
                ('r422_23', models.IntegerField(blank=True, null=True, verbose_name='Jumlah pekerja pada usaha utama')),
                ('r425', models.CharField(blank=True, choices=[('1', '< 5 Juta (Ultra Mikro)'), ('2', '5 s.d. < 15 Juta (Ultra Mikro)'), ('3', '15 s.d. < 25 Juta (Ultra Mikro)'), ('4', '25 s.d. < 167 Juta (Mikro)'), ('5', '167 s.d. < 1.250 Juta (Kecil)'), ('6', '1.250 s.d. < 4.167 Juta (Menengah)'), ('7', '≥ 4.167 Juta (Besar)')], max_length=1, null=True, verbose_name='Omzet usaha utama perbulan (Rupiah)')),
                ('r427', models.CharField(choices=[('1', 'Kurang Gizi (Wasting)'), ('2', 'Kerdil (Stunting)'), ('3', 'Tidak Ada Catatan'), ('4', 'Tidak Tahu')], max_length=1, verbose_name='Kondisi gizi anak dari pemeriksaan 3 bulan terakhir di posyandu/puskesmas/rumah sakit dengan mengacu pada buku kontrol (Umur 0-4)')),
                ('r430', models.CharField(choices=[('01', 'Tidak Ada'), ('02', 'Hipertensi (darah tinggi)'), ('03', 'Rematik'), ('04', 'Asma'), ('05', 'Masalah jantung'), ('06', 'Diabetes (kencing manis)'), ('07', 'Tuberculosis (TBC)'), ('08', 'Stroke'), ('09', 'Kanker atau tumor ganas'), ('10', 'Gagal ginjal'), ('11', 'Haemophilia'), ('12', 'HIV/AIDS'), ('13', 'Kolesterol'), ('14', 'Sirosis Hati'), ('15', 'Thalasemia'), ('16', 'Leukimia'), ('17', 'Alzheimer'), ('18', 'Lainnya')], max_length=2, verbose_name='Memiliki keluhan kesehatan kronis/menahun?')),
                ('r431a', models.CharField(choices=[('0', 'Tidak memiliki'), ('1', 'PBI JKN'), ('2', 'JKN Mandiri'), ('4', 'JKN Pemberi kerja'), ('8', 'Jamkes lainnya'), ('99', 'Tidak Tahu')], max_length=2, verbose_name='Dalam satu tahun terakhir, apakah memiliki jaminan kesehatan?')),
                ('r431f', models.CharField(choices=[('0', 'Tidak memiliki'), ('1', 'BPJS Jaminan Kecelakaan Kerja'), ('2', 'BPJS Jaminan Kematian'), ('4', 'BPJS Jaminan Hari Tua'), ('8', 'BPJS Jaminan Pensiun'), ('16', 'Pensiun/Jaminan hari tua lainnya (Taspen/Program Pensiun Swasta)'), ('99', 'Tidak Tahu')], max_length=2, verbose_name='Dalam satu tahun terakhir, apakah (Nama) memiliki jaminan ketenagakerjaan?')),
            ],
            options={
                'verbose_name': 'Master Data Penduduk',
                'verbose_name_plural': 'Master Data Penduduk',
            },
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]