from django.contrib import admin
from .models import Post

# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ["title","created_at","modified"]

#     class Meta:
#         model = Post


admin.site.register(Post)