from django.db import models

class Xona(models.Model):
    nomi = models.CharField(max_length=120)
    sigimi = models.IntegerField(default=1)

    def __str__(self):
        return self.nomi

class Fani(models.Model):
    nomi = models.CharField(max_length=100)
    oqituvchisi = models.ForeignKey('Oqituvchi', on_delete=models.CASCADE)
    xonasi = models.ForeignKey(Xona, on_delete=models.CASCADE)
    darsBoshlanishVaqti = models.TimeField()
    davomEtadi = models.IntegerField()
    juftmi = models.BooleanField(default=True)
    kursNarxi = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nomi


class Oqituvchi(models.Model):
    ismi = models.CharField(max_length=120)
    familiyasi = models.CharField(max_length=120)
    oquvchiSoni = models.IntegerField(default=0)
    oyligi = models.DecimalField(max_digits=9, decimal_places=3, blank=True)
    foiz = models.IntegerField(blank=True)

    def __str__(self):
        return self.ismi


class Oquvchilar(models.Model):
    ismi = models.CharField(max_length=120)
    familiya = models.CharField(max_length=120)
    fani = models.ForeignKey(Fani, on_delete=models.CASCADE)
    parol = models.CharField(max_length=20)
    tugSana = models.DateField()

    def __str__(self):
        return self.ismi

