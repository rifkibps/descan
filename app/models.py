from django.db import models

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
    r310 = models.CharField(max_length=1, blank=False, null=False, choices=r310_choices, verbose_name="Tempat pembuangan akhir tinja")

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