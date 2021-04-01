from django.contrib import admin
from .models import Guitar
from .models import Maintenance

# Register your models here.
admin.site.register(Guitar)
admin.site.register(Maintenance)