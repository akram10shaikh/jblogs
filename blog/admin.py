from django.contrib import admin
from blog.models import Category,Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','image')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)