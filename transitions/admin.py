from django.contrib import admin

from django.contrib import admin
from .models import Hakkimda, Haber, SonBagislar, SSS, Iletisim,Uyelik
from ckeditor.widgets import CKEditorWidget
from django.db import models

class HakkimdaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class HaberAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class SonBagislarAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class SSSAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class IletisimAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
class UyelikAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Uyelik, UyelikAdmin)
admin.site.register(Hakkimda, HakkimdaAdmin)
admin.site.register(Haber, HaberAdmin)
admin.site.register(SonBagislar, SonBagislarAdmin)
admin.site.register(SSS, SSSAdmin)
admin.site.register(Iletisim, IletisimAdmin)

