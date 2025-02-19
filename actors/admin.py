from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    lsit_display = (
        'id',
        'name',
        'birthday',
        'nationality'   
    )