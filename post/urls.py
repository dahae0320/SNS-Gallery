from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('post_update/<int:post_id>', views.post_update, name='post_update'),
    path('post_delete/<int:post_id>', views.post_delete, name='post_delete'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)