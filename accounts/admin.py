from django.contrib import admin

from accounts.models import Appointment, Doctor, User,GenderModel,BloodModel

# Register your models here.

admin.site.register(User)
admin.site.register(GenderModel)
admin.site.register(BloodModel)
admin.site.register(Doctor)
admin.site.register(Appointment)
