from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class RegionAdministrativeModels(models.Model):
    class Meta:
        verbose_name = 'Master Wilayah Administratif'
        verbose_name_plural = 'Master Wilayah Administratif'
    
    reg_code = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name="Kode Wilayah")
    reg_name = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Wilayah")

    def __str__(self):
        return f"{self.reg_code} - {self.reg_name}"

class RegionSLSModels(models.Model):

    class Meta:
        verbose_name = 'Master SLS/Non SLS'
        verbose_name_plural = 'Master SLS/Non SLS'

    reg_code = models.ForeignKey(RegionAdministrativeModels, on_delete=models.CASCADE, null=False, related_name='region_administrative', verbose_name="Kode Desa/Kelurahan")
    reg_sls_code = models.CharField(max_length=6, unique=True, blank=False, null=False, verbose_name="Kode SLS/Non SLS")
    reg_sls_name = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama SLS/Non SLS")

    def __str__(self):
        return f"{self.reg_sls_name}, Desa/Kel. {self.reg_code.reg_name}"


class FamiliesModels(models.Model):

    class Meta:
        verbose_name = 'Master Data Keluarga'
        verbose_name_plural = 'Master Data Keluarga'

   
    r104 = models.ForeignKey(RegionAdministrativeModels, on_delete=models.RESTRICT, null=False, related_name='families_location_by_region', verbose_name='Kode Desa/Kelurahan')
    r105 = models.ForeignKey(RegionSLSModels, on_delete=models.RESTRICT, null=False, related_name='families_location_by_sls', verbose_name='Kode SLS/Non SLS')
    r107 = models.TextField(max_length=256, blank=False, null=False, verbose_name="Alamat lengkap")
    r108 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Kepala Keluarga (KK)")
    r112 = models.IntegerField(blank=False, null=False, verbose_name="Jumlah Anggota Keluarga?")
    r115 = models.CharField(max_length=16, blank=False, null=False, verbose_name="Nomor Kartu Keluarga (KK)")

    r301a_choices = (
        ('1', 'Milik Sendiri'),
        ('2', 'Kontrak/Sewa'),
        ('3', 'Bebas Sewa'),
        ('4', 'Dinas'),
        ('5', 'Lainnya'),
    )

    r301b_choices = (
        ('1', 'SHM atas Nama Anggota Keluarga'),
        ('2', 'SHM bukan a.n Anggota Keluarga dengan Perjanjian Pemanfaatan Tertulis'),
        ('3', 'SHM bukan a.n Anggota Keluarga tanpa Perjanjian Pemanfaatan Tertulis'),
        ('4', 'Sertifikat selain SHM (SHGB, SHSRS)'),
        ('5', 'Surat Bukti Lainnya (Girik, Letter C, dll)'),
        ('6', 'Tidak punya'),
    )

    r301a = models.CharField(max_length=1, blank=False, null=False, choices=r301a_choices, verbose_name="Status kepemilikan bangunan tempat tinggal yang ditempati?")
    r301b = models.CharField(max_length=1, blank=True, null=True, choices=r301b_choices, verbose_name="Apa bukti kepemilikan tanah bangunan tempat tinggal saat ini?")

    r303_choices = (
        ('1', 'Marmer/Granit'),
        ('2', 'Keramik'),
        ('3', 'Parket/Vini/Karpet'),
        ('4', 'Ubin/Tegel/Teraso'),
        ('5', 'Kayu/Papan'),
        ('6', 'Semen/Bata Merah'),
        ('7', 'Bambu'),
        ('8', 'Tanah'),
        ('9', 'Lainnya')
    )

    r304_choices = (
        ('1', 'Tembok'),
        ('2', 'Plesteran Anyaman Bambu/Kawat'),
        ('3', 'Kayu/Papan/Gypsum/GRC/Calciboard'),
        ('4', 'Anyaman Bambu'),
        ('5', 'Batang Kayu'),
        ('6', 'Bambu'),
        ('7', 'Lainnya'),
    )

    r305_choices = (
        ('1', 'Beton'),
        ('2', 'Genteng'),
        ('3', 'Seng'),
        ('4', 'Asbes'),
        ('5', 'Bambu'),
        ('6', 'Kayu/Sirap'),
        ('7', 'Jerami/Ijuk/Daun-daunan/Numbia'),
        ('8', 'Lainnya'),
    )

    r302 = models.IntegerField(blank=False, null=False, verbose_name="Luas lantai bangunan tempat tinggal? ... m2")
    r303 = models.CharField(max_length=1, blank=False, null=False, choices=r303_choices, verbose_name="Apa jenis lantai terluas?")
    r304 = models.CharField(max_length=1, blank=False, null=False, choices=r304_choices, verbose_name="Apa jenis dinding terluas?")
    r305 = models.CharField(max_length=1, blank=False, null=False, choices=r305_choices, verbose_name="Apa jenis atap terluas?")
    
    r306a_choices = (
        ('1', 'Air Kemasan Bermerk'),
        ('2', 'Air Isi Ulang'),
        ('3', 'Leding'),
        ('4', 'Sumur Bor/Pompa'),
        ('5', 'Sumur Terlindung'),
        ('6', 'Sumur Tak Terlindung'),
        ('7', 'Mata Air Terlindung'),
        ('8', 'Mata Air Tak Terlindung'),
        ('9', 'Air Permukaan (Sungai/Danau/Waduk/Kolam/Irigasi)'),
        ('10', 'Air Hujan'),
        ('11', 'Lainnya'),
    )
    
    r306b_choices = (
        ('1', '< 10 Meter'),
        ('2', '>= 10 Meter'),
        ('8', 'Tidak Tahu')
    )

    r306a = models.CharField(max_length=2, blank=False, null=False, choices=r306a_choices, verbose_name="Apa sumber air minum utama?")
    r306b = models.CharField(max_length=1, blank=True, null=True, choices=r306b_choices, verbose_name="Seberapa jauh jarak sumber air minum utama ke tempat penampungan limbah/kotoran/tinja terdekat?")

    r307a_choices = (
        ('1', 'Listrik PLN dengan meteran'),
        ('2', 'Listrik PLN tanpa meteran'),
        ('3', 'Listrik Non-PLN'),
        ('4', 'Bukan Listrik'),
    )

    r307b_choices = (
        ('1', '450 Watt'),
        ('2', '900 Watt'),
        ('3', '1.300 Watt'),
        ('4', '2.200 Watt'),
        ('5', '> 2.200 Watt'),
    )

    r308_choices = (
        ('1', 'Listrik'),
        ('2', 'Gas Elpiji 5,5 Kg/Blue Gas'),
        ('3', 'Gas Elpiji 12 Kg'),
        ('4', 'Gas Elpiji 3 Kg'),
        ('5', 'Gas Kota'),
        ('6', 'Biogas'),
        ('7', 'Minyak Tanah'),
        ('8', 'Briket'),
        ('9', 'Arang'),
        ('10', 'Kayu Bakar'),
        ('11', 'Lainnya'),
        ('00', 'Tidak Memasak di Rumah'),
    )

    r307a = models.CharField(max_length=1, blank=False, null=False, choices=r307a_choices, verbose_name="Apa sumber penerangan utama?")
    r307b = models.CharField(max_length=1, blank=True, null=True, choices=r307b_choices, verbose_name="Berapa daya yang terpasang di rumah ini?")
    r308 = models.CharField(max_length=2, blank=False, null=False, choices=r308_choices, verbose_name="Bahan bakar/energi utama untuk memasak?")
    
    r309a_choices = (
        ('1', 'Ada, digunakan hanya Anggota Keluarga sendiri'),
        ('2', 'Ada, digunakan bersama Anggota Keluarga dari keluarga tertentu'),
        ('3', 'Ada, di MCK komunal'),
        ('4', 'Ada, di MCK umum/siapapun menggunakan'),
        ('5', 'Ada, Anggota Keluarga tidak menggunakan'),
        ('6', 'Tidak ada fasilitas'),
    )

    r309b_choices = (
        ('1', 'Leher Angsa'),
        ('2', 'Plengsengan dengan Tutup'),
        ('3', 'Plengsengan tanpa Tutup'),
        ('4', 'Cemplung/Cubluk')
    )

    r309a = models.CharField(max_length=1, blank=False, null=False, choices=r309a_choices, verbose_name="Kepemilikan dan penggunaan fasilitas tempat buang air besar?")
    r309b = models.CharField(max_length=1, blank=True, null=True, choices=r309b_choices, verbose_name="Jenis kloset?")

    r310_choices = (
        ('1', 'Tangki Septik'),
        ('2', 'IPAL'),
        ('3', 'Kolam/Sawah/Sungai/Danau/Laut'),
        ('4', 'Lubang Tanah'),
        ('5', 'Pantai/Tanah Lapang/Kebun'),
        ('6', 'Lainnya'),
    )
    r310 = models.CharField(max_length=1, blank=False, null=False, choices=r310_choices, verbose_name="Tempat pembuangan akhir tinja")

    state = (
        ('1', 'Ya'),
        ('2', 'Tidak')
    )
    r501a = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Penerima Program Bantuan Sosial Sembako/ BPNT?")
    r501a_date = models.DateField(blank=True, null=True, verbose_name="Periode Terakhir Mendapatkan Program")
    r501b = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Penerima Program Keluarga Harapan (PKH)?")
    r501b_date = models.DateField(blank=True, null=True, verbose_name="Periode Terakhir Mendapatkan Program")
    r501c = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Penerima Program Bantuan Langsung Tunai (BLT) Desa?")
    r501c_date = models.DateField(blank=True, null=True, verbose_name="Periode Terakhir Mendapatkan Program")
    r501d = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Penerima Program Subsidi Listrik (Gratis/Pemotongan Biaya)?")
    r501d_date = models.DateField(blank=True, null=True, verbose_name="Periode Terakhir Mendapatkan Program")
    r501e = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Penerima Program Bantuan Pemerintah Daerah?")
    r501e_date = models.DateField(blank=True, null=True, verbose_name="Periode Terakhir Mendapatkan Program")
    r501f = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Penerima Program Bantuan Subsidi Pupuk?")
    r501f_date = models.DateField(blank=True, null=True, verbose_name="Periode Terakhir Mendapatkan Program")
    r501g = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Penerima Program Subsidi LPG?")
    r501g_date = models.DateField(blank=True, null=True, verbose_name="Periode Terakhir Mendapatkan Program")


    r502a = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Tabung gas 5,5 kg atau lebih?")
    r502b = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Lemari Es/Kulkas?")
    r502c = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Air Conditioner (AC)?")
    r502d = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Pemanas Air (Water Heater)?")
    r502e = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Telepon Rumah (PSTN)?")
    r502f = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Televisi Layar Datar (Min. 30 Inci)?")
    r502g = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Emas/Perhiasan (Min. 10 gram)?")
    r502h = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Komputer/Laptop/Tablet?")
    r502i = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Sepeda Motor?")
    r502j = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Sepeda?")
    r502k = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Mobil?")
    r502l = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Perahu?")
    r502m = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Kapal/Perahu Motor?")
    r502n = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Smartphone?")

    r503a = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Keluarga Memiliki Aset Lahan (selain yang ditempati)?")
    r503b = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Keluarga Memiliki Aset Rumah/Bangunan di Tempat Lain?")

    r504a = models.IntegerField(blank=False, null=False, default=0, verbose_name="Jumlah ternak Sapi (ekor)?")
    r504b = models.IntegerField(blank=False, null=False, default=0, verbose_name="Jumlah ternak Kerbau (ekor)?")
    r504c = models.IntegerField(blank=False, null=False, default=0, verbose_name="Jumlah ternak Kuda (ekor)?")
    r504d = models.IntegerField(blank=False, null=False, default=0, verbose_name="Jumlah ternak Babi (ekor)?")
    r504e = models.IntegerField(blank=False, null=False, default=0, verbose_name="Jumlah ternak Kambing/Domba (ekor)?")

    r505_choices = (
        ('0', 'Tidak Menggunakan Internet'),
        ('1', 'Internet dan TV Digital Berlangganan'),
        ('2', 'WiFi'),
        ('3', 'Internet Handphone')
    )

    r506_choices = (
        ('1', 'Ya, untuk Usaha'),
        ('2', 'Ya, untuk Pribadi'),
        ('3', 'Ya, untuk usaha dan pribadi'),
        ('4', 'Tidak')
    )

    r505 = models.CharField(max_length=1 ,blank=False, null=False, choices=r505_choices, verbose_name="Jenis akses internet utama yang digunakan oleh keluarga?")
    r506 = models.CharField(max_length=1 ,blank=False, null=False, choices=r506_choices, verbose_name="Apakah keluarga ini memiliki rekening aktif atau dompet digital?")

    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
      return f"{self.pk}. {self.r108} | {self.r105.reg_sls_name} | Desa/Kel. {self.r104.reg_name}"
    

class PopulationsModels(models.Model):
    class Meta:
        verbose_name = 'Master Data Penduduk'
        verbose_name_plural = 'Master Data Penduduk'
    
    family_id = models.ForeignKey(FamiliesModels, on_delete=models.CASCADE, blank=False, null=False, related_name='families_members', verbose_name='ID Keluarga')
    r401 = models.IntegerField(blank=False, null=False, verbose_name="Nomor Urut ART")
    r402 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama ART")
    r403 = models.CharField(max_length=16, blank=True, null=True, verbose_name="Nomor Induk Kependudukan (NIK)")

    r404_choices = (
        ('1', 'Tinggal Bersama Keluarga'),
        ('2', 'Meninggal'),
        ('3', 'Tidak Tinggal Bersama Keluarga/Pindah ke Wilayah (Daerah) Lain di Indonesia'),
        ('4', 'Tidak Tinggal Bersama Keluarga/Pindah ke Luar Negeri'),
        ('5', 'Anggota Keluarga Baru'),
        ('6', 'Tidak Ditemukan'),
    )

    r405_choices = (
        ('1', 'Laki-laki'),
        ('2', 'Perempuan')
    )

    r404 = models.CharField(max_length=1, blank=False, null=False, choices=r404_choices, verbose_name="Keberadaan anggota keluarga")
    r405 = models.CharField(max_length=1, blank=True, null=True, choices=r405_choices, verbose_name="Jenis Kelamin")
    r406 = models.DateField(blank=True, null=True, verbose_name="Tanggal Lahir")
    r407 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(99)], verbose_name="Umur")

    r408_choices = (
        ('1', 'Belum Kawin'),
        ('2', 'Kawin/Nikah'),
        ('3', 'Cerai Hidup'),
        ('4', 'Cerai Mati'),
    )

    r409_choices = (
        ('1', 'Kepala keluarga'),
        ('2', 'Istri/suami'),
        ('3', 'Anak'),
        ('4', 'Menantu'),
        ('5', 'Cucu'),
        ('6', 'Orangtua/mertua'),
        ('7', 'Pembantu/sopir'),
        ('8', 'Lainnya'),
    )

    r408 = models.CharField(max_length=1, blank=True, null=True, choices=r408_choices, verbose_name="Status Perkawinan")
    r409 = models.CharField(max_length=1, blank=True, null=True, choices=r409_choices, verbose_name="Status hubungan dengan kepala keluarga")

    r411_choices = (
        ('1', 'Tidak Memiliki'),
        ('2', 'Akta Kelahiran'),
        ('3', 'KIA'),
        ('4', 'KTP')
    )

    r412_choices = (
        ('1', 'Tidak/belum pernah sekolah'),
        ('2', 'Masih sekolah'),
        ('3', 'Tidak bersekolah lagi'),
    )

    r415_choices = (
        ('1', 'Paket A'),
        ('2', 'SDLB'),
        ('3', 'SD'),
        ('4', 'MI'),
        ('5', 'SPM/PDF Ula'),
        ('6', 'Paket B'),
        ('7', 'SMP LB'),
        ('8', 'SMP'),
        ('9', 'MTs'),
        ('10', 'SPM/PDF Wustha'),
        ('11', 'Paket C'),
        ('12', 'SMLB'),
        ('13', 'SMA'),
        ('14', 'MA'),
        
        ('15', 'SMK'),
        ('16', 'MAK'),
        ('17', 'SPM/PDF Ulya'),
        ('18', 'D1/D2/D3'),

        ('19', 'DV/S1'),
        ('20', 'Profesi'),
        ('21', 'S2'),
        ('22', 'S3'),
        ('23', 'Tidak Punya Ijazah SD'),
    )

    r411 = models.CharField(max_length=1, blank=True, null=True, choices=r411_choices, verbose_name="Apakah memiliki kartu identitas?")
    r412 = models.CharField(max_length=1, blank=True, null=True, choices=r412_choices, verbose_name="Partisipasi sekolah")
    r415 = models.CharField(max_length=2, blank=True, null=True, choices=r415_choices, verbose_name="Ijazah/STTB tertinggi yang dimiliki")
    
    state = (
        ('1', 'Ya'),
        ('2', 'Tidak')
    )
    r416a = models.CharField(max_length=1, blank=True, null=True, choices=state, verbose_name="Apakah bekerja/membantu bekerja selama seminggu yang lalu?")
    r416b = models.IntegerField(blank=True, null=True, verbose_name="Jumlah Jam (Per Minggu)")

    r417_choices = (
        ('01', 'Pertanian tanaman padi & palawija'),
        ('02', 'Hortikultura'),
        ('03', 'Perkebunan'),
        ('04', 'Perikanan'),
        ('05', 'Peternakan'),
        ('06', 'Kehutanan & pertanian lainnya'),

        ('07', 'Pertambangan/penggalian'),
        ('08', 'Industri pengolahan'),
        ('09', 'Pengadaan listrik, gas, uap/air panas, dan udara dingin'),
        ('10', 'Pengelolaan air, pengelolaan air limbah, pengelolaan dan daur ulang sampah, dan aktivitas remediasi'),

        ('11', 'Konstruksi'),
        ('12', 'Perdagangan besar dan eceran, reparasi dan perawatan mobil dan sepeda motor'),
        ('13', 'Pengangkutan dan pergudangan'),
        ('14', 'Penyediaan akomodasi & makan minum'),
        ('15', 'Informasi & komunikasi'),
        ('16', 'Keuangan & asuransi'),
        ('17', 'Real estate'),
        ('18', 'Aktivitas profesional, ilmiah, dan teknis'),
        ('19', 'Aktivitas penyewaan dan sewa guna tanpa hak opsi, ketenagakerjaan, agen perjalanan, dan penunjang usaha lainnya'),
        ('20', 'Administrasi pemerintahan, pertahanan, dan jaminan sosial wajib'),
        ('21', 'Pendidikan'),
        ('22', 'Aktivitas kesehatan manusia dan aktivitas sosial'),
        ('23', 'Kesenian, hiburan, dan rekreasi'),
        ('24', 'Aktivitas jasa lainnya'),
        ('25', 'Aktivitas keluarga sebagai pemberi kerja'),
        ('26', 'Aktivitas badan internasional dan badan ekstra internasional lainnya')
    )


    r418_choices = (
        ('1', 'Berusaha sendiri'),
        ('2', 'Berusaha dibantu buruh tidak tetap/tidak dibayar'),
        ('3', 'Berusaha dibantu buruh tetap/buruh dibayar'),
        ('4', 'Buruh/karyawan/pegawai swasta'),
        ('5', 'PNS/TNI/Polri/ BUMN/BUMD/pejabat negara'),
        ('6', 'Pekerja bebas pertanian'),
        ('7', 'Pekerja bebas non pertanian'),
        ('8', 'Pekerja keluarga/tidak dibayar'),
    )

    r417 = models.CharField(max_length=2, blank=True, null=True, choices=r417_choices, verbose_name="Lapangan usaha dari pekerjaan utama")
    r418 = models.CharField(max_length=1, blank=True, null=True, choices=r418_choices, verbose_name="Status dalam pekerjaan utama")
    r420a = models.CharField(max_length=1, blank=True, null=True, choices=state, verbose_name="Apakah memiliki usaha sendiri/bersama?")
    r421 = models.CharField(max_length=2, blank=True, null=True, choices=r417_choices, verbose_name="Lapangan usaha dari usaha utama")
    r422_23 = models.IntegerField(blank=True, null=True, verbose_name="Jumlah pekerja pada usaha utama")

    r425_choices = (
        ('1', '< 5 Juta (Ultra Mikro)'),
        ('2', '5 s.d. < 15 Juta (Ultra Mikro)'),
        ('3', '15 s.d. < 25 Juta (Ultra Mikro)'),
        ('4', '25 s.d. < 167 Juta (Mikro)'),
        ('5', '167 s.d. < 1.250 Juta (Kecil)'),
        ('6', '1.250 s.d. < 4.167 Juta (Menengah)'),
        ('7', '≥ 4.167 Juta (Besar)')
    )

    r425 = models.CharField(max_length=1, blank=True, null=True, choices=r425_choices, verbose_name="Omzet usaha utama perbulan (Rupiah)")
    r427_choices = (
        ('1', 'Kurang Gizi (Wasting)'),
        ('2', 'Kerdil (Stunting)'),
        ('3', 'Tidak Ada Catatan'),
        ('4', 'Tidak Tahu')
    )

    r430_choices = (
        ('01', 'Tidak Ada'),
        ('02', 'Hipertensi (darah tinggi)'),
        ('03', 'Rematik'),
        ('04', 'Asma'),
        ('05', 'Masalah jantung'),
        ('06', 'Diabetes (kencing manis)'),
        ('07', 'Tuberculosis (TBC)'),
        ('08', 'Stroke'),
        ('09', 'Kanker atau tumor ganas'),
        ('10', 'Gagal ginjal'),
        ('11', 'Haemophilia'),
        ('12', 'HIV/AIDS'),
        ('13', 'Kolesterol'),
        ('14', 'Sirosis Hati'),
        ('15', 'Thalasemia'),
        ('16', 'Leukimia'),
        ('17', 'Alzheimer'),
        ('18', 'Lainnya'),
        
    )
    r431a_choices = (
        ('0', 'Tidak memiliki'),
        ('1', 'PBI JKN'),
        ('2', 'JKN Mandiri'),
        ('4', 'JKN Pemberi kerja'),
        ('8', 'Jamkes lainnya'),
        ('99', 'Tidak Tahu'),
    )

    r431f_choices = (
        ('0', 'Tidak memiliki'),
        ('1', 'BPJS Jaminan Kecelakaan Kerja'),
        ('2', 'BPJS Jaminan Kematian'),
        ('4', 'BPJS Jaminan Hari Tua'),
        ('8', 'BPJS Jaminan Pensiun'),
        ('16', 'Pensiun/Jaminan hari tua lainnya (Taspen/Program Pensiun Swasta)'),
        ('99', 'Tidak Tahu'),
    )

    r427 = models.CharField(max_length=1, blank=True, null=True, choices=r427_choices, verbose_name="Kondisi gizi anak dari pemeriksaan 3 bulan terakhir di posyandu/puskesmas/rumah sakit dengan mengacu pada buku kontrol (Umur 0-4)")
    r430 = models.CharField(max_length=2, blank=False, null=False, choices=r430_choices, verbose_name="Memiliki keluhan kesehatan kronis/menahun?")
    r431a = models.CharField(max_length=2, blank=False, null=False, choices=r431a_choices, verbose_name="Dalam satu tahun terakhir, apakah memiliki jaminan kesehatan?")
    r431f = models.CharField(max_length=2, blank=False, null=False, choices=r431f_choices, verbose_name="Dalam satu tahun terakhir, apakah (Nama) memiliki jaminan ketenagakerjaan?")
    
