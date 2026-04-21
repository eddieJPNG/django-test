from django.http import HttpResponse

def test_view(request):
    return HttpResponse("<h1>TESTE OLÁ</h1>")


def index_view(request):
    return HttpResponse("<h1>WELCOME TO THE HOME PAGE</h1>")
