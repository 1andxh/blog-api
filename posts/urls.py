from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('', post_view),
    path('create/', post_create, name='create'),
    path('<int:id>/', post_detail),
    path('update/<int:id>/', post_update),
    path('delete/<int:id>/', post_delete),
    path('tags/', view_by_tags),
]