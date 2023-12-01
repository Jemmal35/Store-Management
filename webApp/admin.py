from django.contrib import admin
from . models import *
# Register your models here.

admin.site.site_header = 'Ajef store managmnet system'
admin.site.site_title = 'Ajef store'

admin.site.register(Product)
admin.site.register(Solled)
admin.site.register(DeletedProduct)
admin.site.register(Profile)