from django.contrib import admin
from comment_app.models import Comment



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


# @admin.register(ReplyComment)
# class ReplyCommentAdmin(admin.ModelAdmin):
#     pass


