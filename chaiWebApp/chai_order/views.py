from django.shortcuts import render, redirect, get_object_or_404
from .models import ChaiVariety
from .forms import ChaiOrderForm

def your_orders(request):
    chais = ChaiVariety.objects.all
    return render(request, 'chai_order/your_orders.html', {'chai_orders': chais})

def order_chai(request):
    if request.method == 'POST':
        form = ChaiOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('your_orders')
    else:
        form = ChaiOrderForm()
    
    return render(request, 'chai_order/order.html', {'form': form})

def edit_chai(request, pk):
    chai = get_object_or_404(ChaiVariety, pk=pk)
    if request.method == "POST":
        form = ChaiOrderForm(request.POST, request.FILES, instance=chai)
        if form.is_valid():
            form.save()
            return redirect('your_orders')
    else:
        form = ChaiOrderForm(instance=chai)
    return render(request, 'chai_order/order.html', {'form': form})

def delete_chai(request, pk):
    chai = get_object_or_404(ChaiVariety, pk=pk)
    if request.method == 'POST':
        chai.delete()
        return redirect('your_orders')
    return render(request, 'chai_order/delete_confirmation.html', {'chai': chai})
 