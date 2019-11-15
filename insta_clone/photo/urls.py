from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from .views import PhotoCreate, PhotoDelete, PhotoDetail, PhotoList, PhotoUpdate

app_name = "photo"
urlpatterns = [
    path("create/", PhotoCreate.as_view(), name="create"),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name="detail"),
    path("", PhotoList.as_view(), name="index"),
    url(r'tmptag/(?P<id>\d+)$', views.createTag, name='createtag'),
    path("delete/(?P<id>\d+)$", views.delete_photo, name="delete"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
