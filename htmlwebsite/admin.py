from django.contrib import admin
from htmlwebsite.models import Classical_Song, Devotional_Song, Trending_Song

# Register your models here.
admin.site.register(Classical_Song)
admin.site.register(Trending_Song)
admin.site.register(Devotional_Song)
