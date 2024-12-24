from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from smart.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(label='Сообщение', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    save_on_top = True


class PricesAdminForm(forms.ModelForm):
    content = forms.CharField(label='Инфоромация о ценах', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Prices
        fields = '__all__'


class PricesAdmin(admin.ModelAdmin):
    form = PricesAdminForm
    list_display = ('id', 'title', 'service', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'service')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


class ExtraAdminForm(forms.ModelForm):
    content = forms.CharField(label='Дополнительная информация ', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Extra
        fields = '__all__'


class ExtraAdmin(admin.ModelAdmin):
    form = ExtraAdminForm
    list_display = ('id', 'title','extraContent','getHtmlPhoto', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title','extraContent',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def getHtmlPhoto(self, picture):
        if picture.extra_image:
            return mark_safe(f"<img src='{picture.extra_image.url}' width=50>")

    getHtmlPhoto.short_description = 'миниатюра'


class NavAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'gethtmlPhoto', 'annotations1', 'annotations2')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=50>")
    gethtmlPhoto.short_description = 'миниатюра'


class ServicesAdminForm(forms.ModelForm):
    annotation = forms.CharField(label='Рекламное описание ', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Services
        fields = '__all__'


class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm
    list_display = ('id', 'title', 'getHtmlPhoto', 'cat', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def getHtmlPhoto(self, picture):
        if picture.menu_image:
            return mark_safe(f"<img src='{picture.menu_image.url}' width=50>")

    getHtmlPhoto.short_description = 'миниатюра'

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'galleryLink', 'getHtmlPhoto', 'is_published')
    list_display_links = ('id','getHtmlPhoto' )
    search_fields = ('galleryLink',)
    list_editable = ('is_published',)
    list_filter = ('is_published', )
    save_on_top = True

    def getHtmlPhoto(self, picture):
        if picture.gallery_image:
            return mark_safe(f"<img src='{picture.gallery_image.url}' width=50>")

    getHtmlPhoto.short_description = 'миниатюра'


@admin.register(PrintBasePrice)
class PrintBasePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'base_price')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True

@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'size', 'density', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True


@admin.register(TonerConsumption)
class TonerConsumptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price_plus') 
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True


admin.site.register(Services, ServicesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Prices, PricesAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Gallery, GalleryAdmin)

admin.site.site_header = 'СМАРТ ФОТО'