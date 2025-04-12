from django.urls import path
from .views import CommentViewSet


comment_list = CommentViewSet.as_view({
    'get' : "list",

})

urlpatterns = [
    path('posts/<int:post_id>/comments/', comment_list, name='post-comments-list'),

]
