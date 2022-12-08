from django.shortcuts import render, redirect
from .models import provedores, Productos, Entradas, Salidas
from .forms import ProductosForm, EntradasForm, ProvedoresForm, CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user.pk)
            return redirect('catalogo')

        else:
            messages.info(request, 'Usuario o contraseña incorrectas')
            
    return render(request, 'login.html', context)

def registrarse(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada ' + user)

            return redirect('catalogo')

    context = {'form':form}
    return render(request, 'registrarse.html', context)

@login_required(login_url='loginPage')
def catalogo(request):
    provedores_Productos = provedores.objects.all()
    productos_inventario = Productos.objects.all()
    form = ProductosForm
    context = {
        'provedor':provedores_Productos,
        'productos': productos_inventario,
        'form': form
    }
    
    if request.method == 'POST':
        busquedaProducto = request.POST['busquedaProducto']
        productouno = Productos.objects.filter(nombre_producto__contains=busquedaProducto)
        context['busquedaProducto'] = busquedaProducto
        context['productos'] = productouno

    return render(request, 'catalogo.html', context)
@login_required(login_url='loginPage')
def editarCatalogo(request, pk):
    producto = Productos.objects.get(pk=pk)
    form = ProductosForm(instance=producto)
    context = {
        'form': form
    }

    if request.method == 'GET':
            productos = Productos.objects.all()
            context['productos'] = productos

    if request.method == 'POST':
        form  = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            print("funciona")
            return redirect('catalogo')

    return render(request, 'editarCatalogo.html', context)

@login_required(login_url='loginPage')
def añadirNuevoProducto(request):
    productos = Productos.objects.all()
    inventarioForm = ProductosForm()
    
    context = {
        'productos': productos,
        'inventarioForm': inventarioForm,
    }

    if request.method == 'POST':
        form = ProductosForm(request.POST, request.FILES)
        if form.is_valid():
            inv = form.save()
            return render(request, 'catalogo.html', context)
    

    return render(request, 'nuevoProducto.html', context)

@login_required(login_url='loginPage')
def entradas(request):
    productos = Productos.objects.all()
    context = {
        'productos': productos
    }

    return render(request, 'entradas.html', context)

@login_required(login_url='loginPage')
def crearEntrada(request, pk):
    producto = Productos.objects.get(pk=pk)
    form = EntradasForm(instance=producto)
    context = {
        'form': form
    }

    if request.method == 'GET':
            productos = Productos.objects.all()
            context['productos'] = productos

    
    if request.method == 'POST':
        
        cantidadd = request.POST['cantidad']
        total = producto.unidadesEnStock + int(cantidadd)
        Productos.objects.filter(pk=pk).update(unidadesEnStock=total)
        Entradas.objects.create(
            producto = producto,
            cantidad = cantidadd,
            provedor = producto.provedor
        )
        return redirect('entradas')
        
        #if form.is_valid():
            #form.save()
            #print("funciona")
            #return redirect('entradas')

    return render(request, 'crearEntrada.html', context)
@login_required(login_url='loginPage')
def reporteEntradas(request):
    listaentradas = Entradas.objects.all()
    context = {
        'entradas': listaentradas
    }
    return render(request, 'reporteEntradas.html', context)

@login_required(login_url='loginPage')
def salidas(request):
    productos = Productos.objects.all()
    context = {
        'productos': productos
    }

    return render(request, 'salidas.html', context)

@login_required(login_url='loginPage')
def crearSalida(request, pk):
    producto = Productos.objects.get(pk=pk)
    form = EntradasForm(instance=producto)
    context = {
        'form': form
    }

    if request.method == 'GET':
            productos = Productos.objects.all()
            context['productos'] = productos

    
    if request.method == 'POST':
        
        cantidadd = request.POST['cantidad']
        total = producto.unidadesEnStock - int(cantidadd)
        Productos.objects.filter(pk=pk).update(unidadesEnStock=total)
        Salidas.objects.create(
            producto = producto,
            cantidad = cantidadd,
            
        )
        return redirect('salidas')
        
        #if form.is_valid():
            #form.save()
            #print("funciona")
            #return redirect('entradas')

    return render(request, 'crearSalida.html', context)
@login_required(login_url='loginPage')
def reporteSalidas(request):
    listasalidas = Salidas.objects.all()
    context = {
        'salidas': listasalidas
    }
    return render(request, 'reporteSalidas.html', context)


@login_required(login_url='loginPage')
def Provedores(request):
    
    provedores_Productos = provedores.objects.all()
    
    form = ProvedoresForm
    context = {
        'provedores':provedores_Productos,
        
        'form': form
    }
    
    if request.method == 'POST':
        busquedaProvedor = request.POST['busquedaProducto']
        proveuno= provedores.objects.filter(nombre_producto__contains=busquedaProvedor)
        context['busquedaProvedor'] = busquedaProvedor
        context['provedoruno'] = proveuno

    return render(request, 'Provedores.html', context)

@login_required(login_url='loginPage')
def añadirNuevoProvedor(request):
    provedoress = provedores.objects.all()
    provedoresForm = ProvedoresForm()
    
    context = {
        'provedores': provedoress,
        'provedoresForm': provedoresForm,
    }

    if request.method == 'POST':
        form = ProvedoresForm(request.POST, request.FILES)
        if form.is_valid():
            inv = form.save()
            return render(request, 'Provedores.html', context)
    

    return render(request, 'nuevoProvedor.html', context)

@login_required(login_url='loginPage')
def editarProvedor(request, pk):
    provedor = provedores.objects.get(pk=pk)
    form = ProvedoresForm(instance=provedor)
    context = {
        'form': form
    }

    if request.method == 'GET':
            provedoress = provedores.objects.all()
            context['provedores'] = provedoress

    if request.method == 'POST':
        form  = ProvedoresForm(request.POST, instance=provedor)
        if form.is_valid():
            form.save()
            print("funciona")
            return redirect('provedores')

    return render(request, 'editarProvedor.html', context)