from django.contrib import admin

# Register your models here.

from .models import Author,Tag,Post,Comment



class PostAdmin(admin.ModelAdmin):
    list_filter = ['author','tag','date']
    list_display= ["title","date","author"]
    list_per_page = 5

    prepopulated_fields = {"slug":("title",)}


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ["first_name","last_name","email_address"]
    list_display = ["first_name","last_name","email_address"]
    list_per_page=5


class TagAdmin(admin.ModelAdmin):
    list_filter = ["caption"]
    list_display = ["caption"]
    list_per_page = 5

class CommentAdmin(admin.ModelAdmin):
    list_display = ["user_name","post"]
    list_per_page = 5

                            

admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)