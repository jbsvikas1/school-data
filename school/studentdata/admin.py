from django.contrib import admin

# Register your models here.
from studentdata.models import classdetails,student
admin.site.register(classdetails)
admin.site.register(student)
