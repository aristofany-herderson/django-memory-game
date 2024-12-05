from django.contrib import admin
from .models import Player

class PlayerModel(admin.ModelAdmin):
  list_display = ["username", "flips_quantity", "used_time", "has_completed"]
  list_filter = ["flips_quantity"]
  search_fields = ["username"]

admin.site.register(Player, PlayerModel)