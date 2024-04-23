from django.contrib import admin

# Register your models here.
from ecrpg.models import WikiCategory, WikiPost


class PostAdmin (admin.ModelAdmin):
    pass

class CategoryAdmin (admin.ModelAdmin):
    pass

admin.site.register(WikiPost, PostAdmin)
admin.site.register(WikiCategory, CategoryAdmin)