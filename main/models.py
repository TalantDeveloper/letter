from django.db import models








class Letter(models.Model):
    nazorat_kartasi = models.CharField(max_length=255, verbose_name="Nazorat Kartasi")
    guruh = models.CharField(max_length=255, verbose_name="Guruh")
    muxbir = models.CharField(max_length=255, verbose_name="Muxbir")
    hujjat_turi = models.CharField(max_length=255, verbose_name="Hujjat turi")
    royhatga_olingan_sanat = models.CharField(max_length=255, verbose_name="Royhatga olingan sanat")
    royhatga_olingan_raqam = models.CharField(max_length=255, verbose_name="Royhatga olingan raqam")
    hujjat_sanasi = models.CharField(max_length=255, verbose_name="Hujjat sanasi")
    hujjat_raqami = models.CharField(max_length=255, verbose_name="Hujjat raqami")
    xulosa = models.CharField(max_length=255, verbose_name="Xulosa")
    muddat = models.CharField(max_length=255, verbose_name="Muddat")
    rezolutsiya = models.CharField(max_length=255, verbose_name="Rezolutsiya")
    qaror_muallifi = models.CharField(max_length=255, verbose_name="Qaror muallifi")
    yechim_turi = models.CharField(max_length=255, verbose_name="Yechim turi")
