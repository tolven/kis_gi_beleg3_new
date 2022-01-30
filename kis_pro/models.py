from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Main Class Person
class Person(models.Model):
    title = models.CharField(max_length=50)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def user_print(self):
        return self.title + ' ' + self.firstname + ' ' + self.lastname

    def get_all_objects(self):
        return self.objects.all()

    def __str__(self):
        return self.user_print()

    class Meta:
        abstract = True


# Roles
class Role(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def print_role_name(self):
        return self.name


class User(Person):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def role_to_name(self):
        return self.role.print_role_name()

    # def role_to_url(self):
    #     return 'kis_pro_' + self.role_to_name().lower()
    #
    # def role_to_html(self):
    #     return self.role_to_url() + '.html'


class Doctor(Person):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def role_to_name(self):
        return self.role.print_role_name()

    def role_to_url(self):
        return 'kis_pro_' + self.role_to_name().lower()

    def show_cases(self):
        return self.cases

    def __str__(self):
        return super().__str__() + ' ' + self.role_to_name()


class Patient(Person):
    birthdate = models.DateField()
    attending_doctor = models.ManyToManyField(Doctor)

    def getAge(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))


class Cases(models.Model):
    timestamp = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class TNM(Cases):
    tumor = models.CharField(max_length=2)
    nodes = models.CharField(max_length=2)
    metastases = models.CharField(max_length=2)
    report_text = models.TextField(max_length=500)

