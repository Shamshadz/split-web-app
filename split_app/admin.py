from django.contrib import admin
from split_app.models import bill,payee

# Register your models here.
admin.site.register([bill,payee])