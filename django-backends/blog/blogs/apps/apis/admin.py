from django.contrib import admin
from .models import Blog,BlogCatgory,BlogComment,Messages,FriendsLink,Music
import markdown2
# Register your models here.
admin.register(BlogCatgory)
admin.site.register(BlogCatgory)
admin.register(Messages)
admin.site.register(Messages)
admin.register(FriendsLink)
admin.site.register(FriendsLink)
admin.register(Music)
admin.site.register(Music)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.contents = markdown2.markdown(obj.contents, extras=['fenced-code-blocks'])
        super().save_model(request, obj, form, change)


@admin.register(BlogComment)
class BlogCommentsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.content = markdown2.markdown(obj.content, extras=['fenced-code-blocks'])
        super().save_model(request, obj, form, change)