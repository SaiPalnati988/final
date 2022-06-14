from django.shortcuts import render
from .models import CustomerDetails


def main_view(request):
    return render(request,'main.html')

def register_view(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else :
        CustomerDetails(
        name = request.POST.get('name'),
        email = request.POST.get('email_id'),
        mobile_number = request.POST.get('mobile'),
        unique_id = request.POST.get('unique_id'),
        password = request.POST.get('password'),
        re_enter_password = request.POST.get('re_password'),
        address_line_1 = request.POST.get('address1'),
        address_line_2 = request.POST.get('address2')
        ).save()
        return render(request,'register.html')

# Create your views here.
