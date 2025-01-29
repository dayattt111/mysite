from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("absen_masuk/", views.absen_masuk, name="absen_masuk"),
    # path("absen_keluar/", views.absen_keluar, name="absen_masuk"),
    # path("data/", views.data_rekapan, name="data_rekapan"),
]