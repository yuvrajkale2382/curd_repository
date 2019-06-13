from django.shortcuts import render
from .models import ProductData
from .forms import CreateForm,UpdateForm,DeleteForm
from django.http.response import HttpResponse
# Create your views here.


def HomeView(request):
    return render(request,'home.html')

def CreateView(request):
    if request.method=='POST':
        cform=CreateForm(request.POST)
        if cform.is_valid():
            pid=request.POST.get('product_id','')
            pname=request.POST.get('product_name','')
            pcost=request.POST.get('product_cost','')
            pcolor=request.POST.get('product_color','')
            pclass=request.POST.get('product_class','')
            cname=request.POST.get('customer_name','')
            cmobile=request.POST.get('customer_mobile','')
            cemail=request.POST.get('customer_email','')

            data=ProductData(
                product_id=pid,
                product_name=pname,
                product_cost=pcost,
                product_color=pcolor,
                product_class=pclass,
                customer_name=cname,
                customer_mobile=cmobile,
                customer_email=cemail
            )

            data.save()
            cform=CreateForm()
            return render(request,'create_form.html',{'cform':cform})
    else:
        cform=CreateForm()
        return render(request,'create_form.html',{'cform':cform})
def RetrieveView(request):
    pdata=ProductData.objects.all()
    return render(request,'retrieve_details.html',{'pdata':pdata})


def UpdateView(request):
    if request.method=='POST':
        uform=UpdateForm(request.POST)
        if uform.is_valid():
             product_id=request.POST.get('product_id','')
             product_cost=request.POST.get('product_cost','')
             pid=ProductData.objects.filter(product_id=product_id)
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
        if not pid:
            return HttpResponse('<h1>Invalid Product ID</h1>')
        else:
            pid.update(product_cost=product_cost)
            uform=UpdateForm()
            return render(request,'update_form.html',{'uform':uform})
    else:
        uform = UpdateForm()
        return render(request, 'update_form.html', {'uform': uform})

def DeleteView(request):
    if request.method=="POST":
        dform=DeleteForm(request.POST)
        if dform.is_valid():
            product_id=request.POST.get('product_id','')
            pid=ProductData.objects.filter(product_id=product_id)
            if not pid:
                return HttpResponse('<h1>Invalid Product ID</h1>')
            else:
                pid.delete()
                dform=DeleteForm()
                return render(request,'delete_form.html',{'dform':dform})
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    else:
        dform = DeleteForm()
        return render(request, 'delete_form.html', {'dform': dform})

