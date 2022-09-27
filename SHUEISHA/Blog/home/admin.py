from django.contrib import admin

# Register your models here.
from .models import BlogModel, Profile, Comment


admin.site.register(BlogModel)
admin.site.register(Profile)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post',
                    'approved_comment', 'created_date')
    list_display_links = ('id', 'author', 'post')
    list_filter = ('author', 'created_date')
    list_editable = ('approved_comment', )
    search_fields = ('author', 'post')
    list_per_page = 20


admin.site.register(Comment, CommentAdmin)
