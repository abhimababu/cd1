# from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import shop
from .forms import ModeForm


# Create your views here.
# def demo(request):
#   return render(request, "home.html")
# return HttpResponse("hello world")

def demo(request):
    product = shop.objects.all()
    return render(request, "home.html", {'products': product})


def detail(request, shop_id):
    product1 = shop.objects.get(id=shop_id)
    return render(request, 'details.html', {'product': product1})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        img = request.FILES['img']
        s = shop(name=name, desc=desc, img=img, price=price)
        s.save()
        print("product added")
    return render(request, "add_product.html")


def update(request, id):
    if form.is_valid():
        obj = shop.objects.get(id=id)
        form = ModeForm(request.POST or None)
        request.FILES.instance = obj
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'form': form, 'obj': obj})


def delete(request, id):
    if request.method == 'POST':
        obj = shop.oblects.get(id=id)
        obj.delete()
    else:
        return redirect('/')

    return render(request, 'delete.html')
