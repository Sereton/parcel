from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'Home'})
def customer_page(request):
    return render(request, 'customer_page.html', {'name': 'Home'})
def courier_page(request):
    return render(request, 'courier_page.html', {'name': 'Home'})