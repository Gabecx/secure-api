from django.db import models
from django.contrib.auth.models import User
from .utils import encrypt_data, decrypt_data


class StudentRecord(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.TextField()
    course = models.TextField()
    year_level = models.IntegerField()

    def save(self, *args, **kwargs):
        # Encrypt before saving
        self.full_name = encrypt_data(self.full_name).decode()
        self.course = encrypt_data(self.course).decode()
        super().save(*args, **kwargs)

    def get_full_name(self):
        return decrypt_data(self.full_name.encode())

    def get_course(self):
        return decrypt_data(self.course.encode())

    def __str__(self):
        return self.full_name