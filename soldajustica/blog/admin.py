from django.contrib import admin
from .forms import PostForm
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    fields = (
        'title',
        'author',
        'content',
        'published',
    )
    readonly_fields = ('pub_date', 'date_created', 'last_update',)
    list_display = ('title', 'author', 'published',)
    list_editable = ('published',)