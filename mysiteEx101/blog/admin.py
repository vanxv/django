from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','status')
	list_filter = ('status', 'created', 'publish', 'author') #启动筛选列表
	search_fields = ('title', 'body') #搜索列表
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = ('publish')
	ordering = ['status', 'publish']
admin.site.register(Post, PostAdmin)
# Register your models here.
