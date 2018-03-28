from Documents.models import User, CountUploadFile
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group


class TeachingUserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'access')
    list_filter = ('name', )
    search_fields = ['name', ]
    readonly_fields = ['regID', ]



admin.site.unregister(Site)
admin.site.register(User, TeachingUserModelAdmin)
admin.site.register(CountUploadFile)
admin.site.unregister(Group)

# Admin change logo text
admin.site.site_header = "Directory NNR"
admin.site.site_title = "Directory NNR"

