from django.contrib import admin
from .models import appvaraity,appreview,appCertificate,Store



class appReviewInLine(admin.TabularInline):
  model = appreview
  extra = 1

class appvarityAdmin(admin.ModelAdmin):
  list_display = ('name','type','date_added')
  inlines = [appReviewInLine]

class StoreAdmin(admin.ModelAdmin):
  list_display = ('name','location')
  filter_horizontal = ('app_varieties', )
class appCertificateAdmin(admin.ModelAdmin):
  list_display = ('app', 'certificate_number')


# Register your models here.
admin.site.register(appvaraity, appvarityAdmin)
admin.site.register(appCertificate, appCertificateAdmin)
admin.site.register(Store,StoreAdmin)
