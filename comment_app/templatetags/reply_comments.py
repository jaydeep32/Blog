from django import template

register = template.Library()



@register.inclusion_tag('comment_app/reply_comment.html', takes_context=True)
def reply_comment_tag(context, comment):
    return {
        'comment': comment,
        'form': context.get('form'),
        }
    

