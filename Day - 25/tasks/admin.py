from django.contrib import admin
from tasks.models import *

# Register your models here.
admin.site.register(CreateInfoModel)
admin.site.register(TaskModel)
admin.site.register(ProfileModel)
admin.site.register(ProductModel)

