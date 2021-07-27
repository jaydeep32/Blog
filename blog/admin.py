from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'content', 'user', )
        }),
    )
    
    save_as = True
    pass
