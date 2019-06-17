from django.contrib import admin
from .models import Winery, Tour, Stop

# Register your models here.
admin.site.register(Winery)
admin.site.register(Tour)
admin.site.register(Stop)