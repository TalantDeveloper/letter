import os
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


def upload_file_check(instance, filename):
    now = datetime.now()
    year_month = now.strftime("%Y-%m")

    # Modify filename (example: adding timestamp)
    filename_without_ext, ext = os.path.splitext(filename)
    timestamp = now.strftime('%Y%m%d-%H-%M-%S')
    new_filename = f"{timestamp}{ext}"

    return os.path.join('xat/', year_month, new_filename)


def upload_file_control(instance, filename):
    now = datetime.now()
    year_month = now.strftime("%Y-%m")

    # Modify filename (example: adding timestamp)
    filename_without_ext, ext = os.path.splitext(filename)
    timestamp = now.strftime('%Y%m%d-%H-%M-%S')
    new_filename = f"{timestamp}{ext}"

    return os.path.join('javob/', year_month, new_filename)


class Center(models.Model):
    name = models.CharField(max_length=256, verbose_name="Markaz")
    short = models.CharField(max_length=255, verbose_name="Short Name", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Xodim")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.short} - {self.name} - Xodim({self.user.first_name} {self.user.last_name})."


class ControlCard(models.Model):
    name = models.CharField(max_length=256, verbose_name="Nazorat kartasi turi")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name="Guruhi")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.name}"


class Reporter(models.Model):  # Корреспондент Muhbir
    name = models.CharField(max_length=255, verbose_name="Muhbir")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.name}"


class DocumentType(models.Model):  # Тип документа Hujjat turi
    name = models.CharField(max_length=255, verbose_name="Hujjat turi")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.name}"


class AuthorResolution(models.Model):
    name = models.CharField(max_length=255, verbose_name="Qaror muallifi")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.name}"


class TypeSolution(models.Model): # Вид решения
    name = models.CharField(max_length=255, verbose_name="Yechim turi")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.name}"


class Letter(models.Model):
    control_card = models.ForeignKey(ControlCard, on_delete=models.SET_NULL, null=True, verbose_name="Nazorat Kartasi")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name="Guruh")
    reporter = models.ForeignKey(Reporter, on_delete=models.SET_NULL, null=True, verbose_name="Muxbir")
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True, verbose_name="Hujjat turi")
    registration_date = models.DateField(verbose_name="Ro'yhatga olingan sana")
    registration_number = models.CharField(max_length=150, verbose_name="Ro'yhatga olingan raqam")
    document_number = models.CharField(max_length=150, verbose_name="Hujjat raqami")
    document_date = models.DateField(verbose_name="Hujjat sanasi")
    summary = models.TextField(verbose_name="Xulosa", null=True, blank=True)
    control = models.BooleanField(default=False, verbose_name="Boshqaruv")
    # lifetime = models.DateField(verbose_name="Muddat")
    resolution = models.TextField(verbose_name="Rezolutsiya", null=True, blank=True)
    auth_resolution = models.ForeignKey(AuthorResolution, on_delete=models.SET_NULL, null=True,
                                        verbose_name="Qaror muallifi")
    type_solution = models.ForeignKey(TypeSolution, on_delete=models.SET_NULL, null=True, verbose_name="Yechim turi")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")


class CheckFile(models.Model):
    file = models.FileField(upload_to=upload_file_check, verbose_name="File")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.file.name} - {self.create_at.strftime('%Y-%m-%d %H:%M:%S')}"


class ControlFile(models.Model):
    file = models.FileField(upload_to=upload_file_control, verbose_name="")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    def __str__(self):
        return f"{self.file.name} - {self.create_at.strftime('%Y-%m-%d %H:%M:%S')}"


class Manager(models.Model):
    centers = models.ManyToManyField(Center, verbose_name="Markazlar")
    letter = models.ForeignKey(Letter, on_delete=models.SET_NULL, null=True, verbose_name="Xat")
    check_file = models.ForeignKey(CheckFile, on_delete=models.SET_NULL, null=True, verbose_name="So'rov file")
    control_file = models.ForeignKey(ControlFile, on_delete=models.SET_NULL, null=True, verbose_name="Javob file")
    lifetime = models.DateField(verbose_name="Muddat")

    control = models.BooleanField(default=False, verbose_name="Tasdiqlash")

    def time_on(self):
        if self.lifetime.strftime("%Y%m%d") >= datetime.now().strftime("%Y%m%d"):
            return True
        else:
            return False

    def time_off(self):
        if self.lifetime.strftime("%Y%m%d") < datetime.now().strftime("%Y%m%d"):
            return False
        else:
            return True

    def check_control(self):
        if self.control:
            return True
        else:
            return False

    @property
    def get_centers(self):
        center = [center.name for center in self.centers.all()]
        return center
