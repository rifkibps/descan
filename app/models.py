from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime
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
    
class OfficerModels(models.Model):

    class Meta:
        verbose_name = 'Daftar Petugas'
        verbose_name_plural = 'Daftar Petugas'
    
    roles = (
        ('1', 'Petugas Pendataan'),
        ('2', 'Petugas Pemeriksaan'),
    )

    name = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Petugas")
    role = models.CharField(max_length=1, blank=False, null=False, choices=roles, verbose_name="Role Petugas")

    def __str__(self):
        return f"{self.id}. {self.name} ({self.role})"

class FamiliesModels(models.Model):

    class Meta:
        verbose_name = 'Master Data Keluarga'
        verbose_name_plural = 'Master Data Keluarga'
    
    r104 = models.ForeignKey(RegionAdministrativeModels, on_delete=models.RESTRICT, null=False, related_name='families_location_by_region', verbose_name='Kode Desa/Kelurahan')
    r105 = models.ForeignKey(RegionSLSModels, on_delete=models.RESTRICT, null=False, related_name='families_location_by_sls', verbose_name='Nama Dusun')
    r106 = models.TextField(max_length=256, blank=False, null=False, verbose_name="Alamat Lengkap")
    r107 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Kepala Keluarga")
    r108 = models.CharField(max_length=16, blank=False, null=False, unique=False, validators=[MinLengthValidator(16)], verbose_name="Nomor Kartu Keluarga (KK)")
    r109 = models.IntegerField(blank=False, null=False, verbose_name="Jumlah Anggota Keluarga")
    r110 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Pemberi Informasi")

    r206_choices = (
        ('1', 'Terisi Lengkap'),
        ('2', 'Tidak Terisi Lengkap'),
    )

    # r201 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Pencacah")
    r201 = models.ForeignKey(OfficerModels, on_delete=models.RESTRICT, blank=False, null=False, related_name='petugas_pencacah', verbose_name='Nama Pencacah')
    r202 = models.DateField(blank=False, null=False, verbose_name="Tgl Kunjungan Pertama")
    r203 = models.DateField(blank=False, null=False, verbose_name="Tgl Kunjungan Terakhir")
    # r204 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Pemeriksa")
    r204 = models.ForeignKey(OfficerModels, on_delete=models.RESTRICT, blank=False, null=False, related_name='petugas_pemeriksa', verbose_name='Nama Pemeriksa')
    r205 = models.DateField(blank=False, null=False, verbose_name="Tanggal Pemeriksaan")
    r206 = models.CharField(max_length=1, blank=False, null=False, choices=r206_choices, verbose_name="Hasil Pencacahan")

    r301_choices = (
        ('1', 'Milik Sendiri'),
        ('2', 'Kontrak/Sewa'),
        ('3', 'Bebas Sewa'),
        ('4', 'Dipinjami'),
        ('5', 'Dinas'),
        ('6', 'Lainnya'),
    )
    r301 = models.CharField(max_length=1, blank=False, null=False, choices=r301_choices, verbose_name="Status penguasan bangunan tempat tinggal yang ditempati")

    r302_choices = (
        ('1', 'Milik Sendiri'),
        ('2', 'Milik Orang Lain'),
        ('3', 'Tanah Negara'),
        ('4', 'Lainnya'),
    )
    r302 = models.CharField(max_length=1, blank=True, null=True, choices=r302_choices, verbose_name="Status lahan tempat tinggal yang ditempati")

    r303_choices = (
        ('1', 'Marmer/Granit'),
        ('2', 'Keramik'),
        ('3', 'Parket/Vini/Karpet'),
        ('4', 'Ubin/Tegel/Teraso'),
        ('5', 'Kayu/Papan'),
        ('6', 'Semen/Bata Merah'),
        ('7', 'Bambu'),
        ('8', 'Kayu/Papan Kualitas Rendah'),
        ('9', 'Tanah'),
        ('10', 'Lainnya')
    )
    r303 = models.CharField(max_length=2, blank=False, null=False, choices=r303_choices, verbose_name="Jenis lantai tempat tinggal terluas")

    r304_choices = (
        ('1', 'Tembok'),
        ('2', 'Plesteran Anyaman Bambu/Kawat'),
        ('3', 'Kayu/Papan/Gypsum/GRC/Calciboard'),
        ('4', 'Anyaman Bambu'),
        ('5', 'Batang Kayu'),
        ('6', 'Bambu'),
        ('7', 'Lainnya'),
    )
    r304 = models.CharField(max_length=1, blank=False, null=False, choices=r304_choices, verbose_name="Jenis dinding terluas")

    r305_choices = (
        ('1', 'Ada, Berfungsi'),
        ('2', 'Ada, Tidak Berfungsi'),
        ('3', 'Tidak Ada'),
    )
    r305 = models.CharField(max_length=1, blank=False, null=False, choices=r305_choices, verbose_name="Keberadaan jendela")
    
    r306_choices = (
        ('1', 'Beton/Genteng Beton'),
        ('2', 'Genteng Keramik'),
        ('3', 'Genteng Metal'),
        ('4', 'Genteng Tanah Liat'),
        ('5', 'Asbes'),
        ('6', 'Seng'),
        ('7', 'Sirap'),
        ('8', 'Bambu'),
        ('9', 'Jerami/Ijuk/Daun-daunan/Rumbia'),
        ('10', 'Lainnya')
    )
    r306 = models.CharField(max_length=2, blank=False, null=False, choices=r306_choices, verbose_name="Jenis atap terluas")
    
    r307_choices = (
        ('1', 'Listrik PLN dengan Meteran'),
        ('2', 'Listrik PLN tanpa Meteran'),
        ('3', 'Lampu Minyak/Lilin'),
        ('4', 'Sumber Penerangan Lainnya'),
    )
    r307 = models.CharField(max_length=1, blank=False, null=False, choices=r307_choices, verbose_name="Sumber penerangan utama")

    r308_choices = (
        ('1', 'Tidak Ada'),
        ('2', 'Kebun/Sungai/Drainase'),
        ('3', 'Dibakar'),
        ('4', 'Tempat Sampah'),
        ('5', 'Tempat Sampah dan Diangkat Reguler'),
    )
    r308 = models.CharField(max_length=1, blank=False, null=False, choices=r308_choices, verbose_name="Tempat pembuangan sampah")

    r309_choices = (
        ('1', 'Sendiri'),
        ('2', 'Bersama/Berkelompok'),
        ('3', 'MCK Umum'),
        ('4', 'Tidak Ada')
    )
    r309 = models.CharField(max_length=1, blank=False, null=False, choices=r309_choices, verbose_name="Fasilitas MCK")

    r310_choices = (
        ('1', 'Air Kemasan Bermerk'),
        ('2', 'Air Isi Ulang'),
        ('3', 'Leding Meteran'),
        ('4', 'Leding Eceran'),
        ('5', 'Sumur Terlindung'),
        ('6', 'Sumur Tak Terlindung'),
        ('7', 'Mata Air Terlindung'),
        ('8', 'Mata Air Tak Terlindung'),
        ('9', 'Air Hujan'),
        ('10', 'Lainnya'),
    )
    r310 = models.CharField(max_length=2, blank=False, null=False, choices=r310_choices, verbose_name="Sumber air minum utama")
    
    state = (
        ('1', 'Ya'),
        ('2', 'Tidak')
    )

    r401a = models.CharField(max_length=1, blank=False, null=False, choices=state, verbose_name="Kepemilikan Tanah/Lahan Pertanian")
    r401b = models.IntegerField(blank=True, null=True, verbose_name="Luas Lahan")

    r402a = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Sapi")
    r402b = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Kerbau")
    r402c = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Kuda")
    r402d = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Babi")
    r402e = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Kambing/Domba")
    r402f = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Domba")
    r402g = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Ayam Buras")
    r402h = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Ayam Ras Pedaging")
    r402i = models.IntegerField(blank=True, null=True, default=0, verbose_name="Jumlah Ayam Ras Petelur")

    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
      return f"{self.pk}. KRT {self.r107} | {self.r105.reg_sls_name} | Desa/Kel. {self.r104.reg_name}"
    

class PopulationsModels(models.Model):
    class Meta:
        verbose_name = 'Master Data Penduduk'
        verbose_name_plural = 'Master Data Penduduk'
    
    family_id = models.ForeignKey(FamiliesModels, on_delete=models.CASCADE, blank=False, null=False, related_name='families_members', verbose_name='ID Keluarga')
    r501 = models.IntegerField(blank=False, null=False, verbose_name="Nomor Urut")
    r502 = models.CharField(max_length=16, blank=False, null=False, unique=False, validators=[MinLengthValidator(16)], verbose_name="NIK")
    r503 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Nama Lengkap")

    r504_choices = (
        ('1', 'Kepala keluarga'),
        ('2', 'Istri/suami'),
        ('3', 'Anak'),
        ('4', 'Menantu'),
        ('5', 'Cucu'),
        ('6', 'Orangtua/mertua'),
        ('7', 'Lainnya'),
    )
    
    r504 = models.CharField(max_length=1, blank=False, null=False, choices=r504_choices, verbose_name="Hubungan dengan KK")

    r505_choices = (
        ('1', 'Tinggal Bersama Keluarga'),
        ('2', 'Meninggal'),
        ('3', 'Tidak Tinggal Bersama Keluarga/Pindah'),
        ('4', 'Anggota Keluarga Baru'),
        ('5', 'Tidak Ditemukan'),
    )
    r505 = models.CharField(max_length=1, blank=False, null=False, choices=r505_choices, verbose_name="Keberadaan anggota keluarga")

    r506_choices = (
        ('1', 'Laki-laki'),
        ('2', 'Perempuan')
    )

    # Null Values
    r506 = models.CharField(max_length=1, blank=False, null=False, choices=r506_choices, verbose_name="Jenis kelamin")
    r507 = models.CharField(max_length=128, blank=False, null=False, verbose_name="Tempat lahir")
    r508 = models.DateField(blank=False, null=False, verbose_name="Tanggal lahir")

    r510_choices = (
        ('1', 'Belum Kawin'),
        ('2', 'Kawin/Nikah'),
        ('3', 'Cerai Hidup'),
        ('4', 'Cerai Mati'),
    )
    r510 = models.CharField(max_length=1, blank=False, null=False, choices=r510_choices, verbose_name="Status pernikahan")


    r511_choices = (
        ('1', 'Islam'),
        ('2', 'Kristen'),
        ('3', 'Katolik'),
        ('4', 'Hindu'),
        ('5', 'Budha'),
        ('6', 'Konghuchu'),
    )
    r511 = models.CharField(max_length=1, blank=False, null=False, choices=r511_choices, verbose_name="Agama")

    r512_choices = (
        ('1', 'Muna'),
        ('2', 'Lainnya'),
    )
    r512 = models.CharField(max_length=1, blank=False, null=False, choices=r512_choices, verbose_name="Suku")

    r513_choices = (
        ('1', 'Bersekolah'),
        ('2', 'Mengurus Rumah Tangga'),
        ('3', 'Tidak Bekerja'),
        ('4', 'Sedang Mencari Pekerjaan'),
        ('5', 'Bekerja'),
    )
    r513 = models.CharField(max_length=1, blank=True, null=True, choices=r513_choices, verbose_name="Kegiatan utama")
    r514 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Pekerjaan utama")
    r515_choices = (
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
    r515 = models.CharField(max_length=2, blank=True, null=True, choices=r515_choices, verbose_name="Lapangan usaha")
    r516 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Komoditas utama")

    r517_choices = (
        ('1', 'Tidak/belum pernah sekolah'),
        ('2', 'Masih sekolah'),
        ('3', 'Tidak bersekolah lagi'),
    )
    r517 = models.CharField(max_length=1, blank=True, null=True, choices=r517_choices, verbose_name="Partisipasi sekolah")

    r518_choices = (
        ('1', 'Tidak/Belum Tamat SD'),
        ('2', 'SD/Sederajat'),
        ('3', 'SMP/Sederajat'),
        ('4', 'SMA/Sederajat'),
        ('5', 'D1/D2/D3'),
        ('6', 'S1/S2/S3'),
    )
    r518 = models.CharField(max_length=1, blank=True, null=True, choices=r518_choices, verbose_name="Pendidikan tertinggi yang ditamatkan")

    r519_choices = (
        ('0', 'Tidak memiliki'),
        ('1', 'BPJS PBI'),
        ('2', 'BPJS Non PBI'),
        ('3', 'Jamkes lainnya'),
    )
    r519 = models.CharField(max_length=2, blank=True, null=True, choices=r519_choices, verbose_name="Jaminan kesehatan")

    state = (
        ('1', 'Ya'),
        ('2', 'Tidak')
    )

    r520a = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Tunanetra/buta")
    r520b = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Tunarungu/tuli")
    r520c = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Tunawicara/bisu")
    r520d = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Tunarungu–wicara/tuli–bisu")
    r520e = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Tunadaksa/cacat tubuh")
    r520f = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Tunagrahita")
    r520g = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Tunalaras")
    r520h = models.CharField(max_length=1, blank=True, null=True, default='2', choices=state, verbose_name="Cacat Ganda")

    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    @property
    def age(self):
        return int((datetime.now().date() - self.r508).days / 365.25)
    
    def __str__(self):
      return f"{self.pk}. {self.r502} | {self.r503}"