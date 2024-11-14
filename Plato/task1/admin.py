from django.contrib import admin
from .models import Buyer, Game

# Админка для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited',)
    search_fields = ('title',)

# Админка для модели Buyer
@admin.register(Buyer)
class Buyer(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)

