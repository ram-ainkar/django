from django.shortcuts import  render, HttpResponse,HttpResponseRedirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def home(request):
    if request.method =="post":
        form = ProductForm(request.Post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        data =Product.objects.all()
        form = ProductForm()
        return render(request, 'electronics/home.html', {'data':data, 'form':form})
