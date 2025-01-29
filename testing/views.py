from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("dashboard inti")
# def absen_masuk(request):
#     return HttpResponse("absen masuk")
# def absen_keluar(request):
#     return HttpResponse("absen keluar")
# def data_rekapan(request):
#     return HttpResponse("data absen hari ini")