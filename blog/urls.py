from django.urls import path
from .views import index_view, about_view, blog_view, blog_detail_view

urlpatterns = [
    path('', index_view),
    path('about/', about_view),
    path('blog/', blog_view),
    path('blog/<int:pk>/', blog_detail_view),
]
