from django.contrib import admin

from app.currency.models import Rate, ContactUs, Source


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        'created',
        'source',
    )
    search_fields = (
        'buy',
        'sell',
        'source',
    )

    readonly_fields = (  # для ограничения корректировки данных
        'buy',
        'sell',
    )

    def has_delete_permission(self, request, obj=None):  # Ограничения по удалению
        return True

    def has_add_permission(self, request):  # Ограничения по добавлению рейтов
        return True

    def has_change_permission(self, request, obj=None):  # Ограничения по изменению рейтов если добавить FALSE
        return True


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'subject',
        'message',
    )
    list_filter = ('email',)
    search_fields = (
        'email',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):  # Ограничения по удалению
        return False

    def has_add_permission(self, request):  # Ограничения по добавлению рейтов
        return False

    def has_change_permission(self, request, obj=None):  # Ограничения по изменению рейтов если добавить FALSE
        return False


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'source_name',
        'created',

    )
    list_filter = (
        'source_url',
        'source_name',
    )
    search_fields = (
        'source_url',
        'source_name',
    )

    def has_delete_permission(self, request, obj=None):  # Ограничения по удалению
        return True

    def has_add_permission(self, request):  # Ограничения по добавлению рейтов
        return True

    def has_change_permission(self, request, obj=None):  # Ограничения по изменению рейтов если добавить FALSE
        return True
