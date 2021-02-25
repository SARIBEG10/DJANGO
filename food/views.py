from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


# def index(request):
#     item_list = Item.objects.all()
#     # template = loader.get_template('food/index.html')
#     context = {
#         'item_list': item_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    model = Item    # same as the function based views
    template_name = 'food/index.html'   # only mention the template
    context_object_name = 'item_list'   # only mention the context object name


def items(request):
    return HttpResponse('<h1> This is item view </h1>')


# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     return render(request, 'food/detail.html', {'item': item})


class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

#
# def create_item(request):
#     form = ItemForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request, 'food/item-form.html', {'form': form})


# class based view for creating item besides the

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item': item})