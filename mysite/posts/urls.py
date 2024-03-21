from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('add-post', views.add_post, name="add-post"),
    path('update/<int:p_id>', views.update_post, name="update-post"),
    path('delete/<int:p_id>', views.delete_post, name="delete-post"),
]
