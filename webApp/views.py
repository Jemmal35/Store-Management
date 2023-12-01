from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .form import *
import json
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        pro = Product.objects.all()
        context = {'product':pro}
        return render(request,'store/index.html', context)


    else:
        return redirect('login')

class login(LoginView):
    template_name = 'store/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    


def search(request):
    if request.method == 'POST':
            search_input = request.POST.get('search_item_index') or ''
            context = {}
            if search_input:    
                searched = Product.objects.filter(Name__istartswith = search_input)
                
                if searched.count() > 0:
                    context['searched_item'] = searched
                else:
                    context['not_found'] = search_input + ': Not found.'
            if search_input == '':
                    context['none'] = 'No search keyword'
            # context['search_input'] = search_input
            return render(request,'store/index.html', context)
        
    else:
        return render(request,'store/index.html')


 
def newProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            Name = form.cleaned_data['Name']
            Price = abs(form.cleaned_data['Price']) 
            Quantity = abs(form.cleaned_data['Quantity'])
            # Entrance_Date = d
            # Expired_Date = form.cleaned_data['Expired_Date']
            Approved_By = str(request.user.first_name) +' ' + str(request.user.last_name)
            # Total_Price = form.cleaned_data['Total_Price']
            try:
                item1 = Product.objects.get(Name = Name)
                item = Product.objects.filter(Name = Name).update(Quantity = int(item1.Quantity)+ int(Quantity), Price = Price , Approved_By = Approved_By)
            except:
                item  = Product.objects.create(Name = Name, Price = Price, Quantity = Quantity, Approved_By = Approved_By , Total_Price = (float(Price)*float(Quantity)))
                
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'store/new_product.html',{'form' : form})


def update(request, id):
    if request.method == 'POST':
        # form = ProductForm(request.POST)
        name = request.POST.get('name')
        price = request.POST.get('price')
        quant = request.POST.get('quantity')
        price = float(price)
        quant = int(quant)

        print(name)
        print(price)
        Approved_By = str(request.user.first_name) +' ' + str(request.user.last_name)
            # Total_Price = form.cleaned_data['Total_Price']
        item  = Product.objects.filter(pk = id).update(Name = name, Price = price, Quantity = quant, Approved_By = Approved_By , Total_Price = (float(price)*float(quant)))
            
        return redirect('index')
    elif request.method == 'GET':
        item = Product.objects.get(pk = id)
        context = {'item': item}
        return render(request, 'store/update.html', context)
        

def solledProduct(request):
    if request.user.is_authenticated:
        context = {}
        
        if request.method == 'POST':
            form = SolledBy(request.POST)
            if form.is_valid():
                # item = form.cleaned_data['item']
                user = form.cleaned_data['user']

            prod = Solled.objects.filter(Solled_By = user)
            context['items'] = prod
        else:  
            product = Solled.objects.all()
            form = SolledBy()
            context['pro'] =  product
        context['form'] = form
    return render(request, 'store/solled_product.html', context)



def sellProduct(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SellForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                # price = form.cleaned_data['price']
                quan = form.cleaned_data['quantity']
                item = Product.objects.get(Name = name)
                price = item.Price
                total = float(quan * price)
                solled = str(request.user.first_name) +' ' + str(request.user.last_name)

                if item.Quantity == 1:
                    if quan > 1:
                        message = 'To much amount request.'
                        form = SellForm()
                        return render(request, 'store/sell_item.html', {'form': form, 'message':message})
                    else:
                        sell  = Solled.objects.create(Name = name, Price = price, Quantity = quan, Solled_By = solled , Total_Price = (float(price)*float(quan)))
                        item.delete()
                        return redirect('solled-item')
                elif  item.Quantity > 1:
                    if quan < item.Quantity:
                        sell  = Solled.objects.create(Name = name, Price = price, Quantity = quan, Solled_By = solled , Total_Price = (float(price)*float(quan)))
                        item = Product.objects.filter(Name = name).update(Quantity = item.Quantity - quan, Total_Price = item.Total_Price - total )
                        return redirect('solled-item')
                    else:
                        message = 'To much amount request.'
                        form = SellForm()
                        return render(request, 'store/sell_item.html', {'form': form, 'message':message})
                
        else:

            form = SellForm()
        return render(request, 'store/sell_item.html', {'form' :form})
    else:
        return render(request, 'store/login.html')


def sellItem(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            item = Product.objects.get(id = id)
            # print(item.Price)
            # name =  request.POST.get('name')
            #     # price = form.cleaned_data['price']
            quan = abs(int(request.POST.get('quant')))
            
            price = item.Price
            total = float(quan * price)
            solled = str(request.user.first_name) +' ' + str(request.user.last_name)

            if item.Quantity == 1:
                    if quan > 1:
                        message = 'To much amount request.'
                        form = SellForm()
                        return render(request, 'store/sell_item.html', {'form': form, 'message':message})
                    else:
                        sell  = Solled.objects.create(Name = item.Name, Price = item.Price, Quantity = quan, Solled_By = solled , Total_Price = (float(price)*quan))
                        item.delete()
                        return redirect('solled-item')
            elif  item.Quantity > 1:
                if quan < item.Quantity:
                    sell  = Solled.objects.create(Name = item.Name, Price = item.Price, Quantity = quan, Solled_By = solled , Total_Price = (float(price)*quan))
                    item = Product.objects.filter(id = id).update(Quantity = item.Quantity - quan, Total_Price = item.Total_Price - total)
                    return redirect('solled-item')
                else:
                    message = 'To much amount request.'
                    form = SellForm()
                    return render(request, 'store/sell_item.html', {'form': form, 'message':message})
        else:
            context = {}
            item = Product.objects.filter(id = id)
            context['item'] = item
            return render(request, 'store/sell_product.html', context)

            


def about(request):
    pro = Product.objects.all()
    context = {'product':pro}
    return render(request,'store/about.html', context)



class deleteProduct(DeleteView):
    # print(id)
    # def get(self, request):
    #     obj = Product.objects.get(id = request.id)
    #     name = obj.Name
    #     price = obj.Price
    #     quant = obj.Quantity
    #     user = request.user
    #     delete = DeletedProduct.objects.create(Name = name, Price = price, Quantity = quant, Total_Price = quant*price, Deleted_By = user)
        
        
    model = Product
    success_url = reverse_lazy('index')
    template_name = 'store/delete.html'
    context_object_name = 'item'

def deleteItem(request, id=None):
    if request.method == 'POST':
        item = Product.objects.get(pk = id)
        user = str(request.user.first_name) +' ' + str(request.user.last_name)
        tot = float(item.Price)  * float(item.Quantity)
        delt = DeletedProduct.objects.create(Name = item.Name, Price = item.Price, Quantity = item.Quantity, Deleted_By = user, Total_Price = tot)
        delt.save()
        item.delete()

        return redirect('index')
    else:
        return render(request, 'store/delete.html')

    
def Deleted(request):
    if request.user.is_authenticated:
        pro = DeletedProduct.objects.all()
        context = {'product':pro}
        return render(request,'store/deleted.html', context)


    else:
        return redirect('login')