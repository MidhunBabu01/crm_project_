from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import CompaniForm, ClientForm
from crm_app.models import Companies, Client

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'Midhun' and password == '123':
            return redirect("crm_app:index")
        else:
            return redirect("crm_app:login") 
    return render(request,"login.html")



def index(request):
    client = Client.objects.all()
    return render(request,"index.html",{"clients":client})



def companies(request):
    company = Companies.objects.all()
    return render(request,"companies.html",{'company':company})


def add_company(request):
    if request.method == 'POST':
        form = CompaniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm_app:companies')
    else:
        form = CompaniForm()
    return render(request,"add_company.html",{'form':form})


def clients(request):
    client = Client.objects.all()
    return render(request,"client.html",{'clients':client})




def add_clients(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm_app:clients')
    else:
        form = ClientForm()
    return render(request,"add_clients.html",{'form':form})



def delete_client(request,client_id):
    client = Client.objects.filter(id=client_id)
    client.delete()
    return redirect('crm_app:clients')

def edit_client(request,client_id):
    if request.method == 'POST':
        update  = Client.objects.get(id=client_id)
        fm = ClientForm(request.POST,instance=update)
        if fm.is_valid():
            fm.save()
            return redirect("crm_app:clients")
    else:
        update  = Client.objects.get(id=client_id)
        fm = ClientForm(instance=update)
    return render(request,"edit_client.html",{'form':fm})