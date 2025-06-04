from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import album_data
# Create your views here.
def index(request):
  data = album_data.objects.all()
  paginator = Paginator(data, 6)
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request,'index.html',{'data':page_obj})

def add(request):
  return render(request,'add.html')

def addrec(request):
    if request.method == 'POST':
        img = request.FILES.POST('phto')
        if img:
            album_data.objects.create(album_image=img)
        return redirect('/')
    return redirect('/')