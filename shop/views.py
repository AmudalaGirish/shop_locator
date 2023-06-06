from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Shop
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Shop
from .forms import ShopForm, QueryForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop_list')
        else:
            return render(request, 'shop/login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'shop/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'shop/home.html')


def shop_list(request):
    # list of all shops
    shops = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {'shops':shops})

def shop_detail(request, id):
    # detail view of shop w.r.t id
    shop = Shop.objects.get(id=id)
    # shop = get_object_or_404(Shop, pk=id)
    return render(request, 'shop/shop_detail.html', {'shop':shop})

@login_required
def shop_create(request):
    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            # getting the user provided data
            name = form.cleaned_data['name']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            # check if a shop with same name and coordinates already exists
            # if Shop.objects.filter(name=name, latitude=latitude, longitude=longitude).exists():
            if Shop.objects.filter(name=name).exists():
                return render(request, 'shop/shop_create.html', {'form':form, 'error_message':'Shop Already exists please provide new shop details'})
            
            form.save()
            return redirect('shop_list')
    return render(request, 'shop/shop_create.html', {'form':form})

@login_required
@permission_required('shop.change_shop')
def shop_update(request, id):
    # shop detail view w.r.t id
    shop = get_object_or_404(Shop, id=id)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_detail', id=id)
    else:
        form = ShopForm(instance=shop)

    return render(request, 'shop/shop_update.html', {'form': form})


def shops_query_view(request):
    form = QueryForm()

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            distance = form.cleaned_data['distance']

            # calculate the latitude range for filtering shops
            latitude_min = latitude - distance 
            latitude_max = latitude + distance

            # calculate the longitude range for filtering shops
            longitude_min = longitude - distance
            longitude_max = longitude + distance

            # retrive the shops within specified distance
            nearby_shops = Shop.objects.filter(
                latitude__range=(latitude_min, latitude_max), 
                longitude__range=(longitude_min, longitude_max)
                )
            return render(request, 'shop/shop_list.html', {'shops':nearby_shops})
        
    return render(request, 'shop/query_form.html', {'form':form})