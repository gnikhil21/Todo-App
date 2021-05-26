from django.test import TestCase
from django.contrib import admin
from .models import todoform
# Create your tests here.
admin.site.register(todoform)