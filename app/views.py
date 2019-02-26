from django.views.generic.base import TemplateView
from django.views.generic import ListView
from groceries.models import GroceryItem
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name='dispatch')
class GroceryListView(ListView):
    template_name = 'groceries.html'
    model = GroceryItem
    context_object_name = 'grocery_list'


@method_decorator(login_required, name='dispatch')
class GorceryItemCreate(CreateView):
    model = GroceryItem
    fields = ['name', 'amount', 'msg']
    template_name = 'add_item_form.html'

    def get_success_url(self):
        return reverse('add_grocery_item')


@method_decorator(login_required, name='dispatch')
class GorceryItemEdit(UpdateView):
    model = GroceryItem
    fields = ['name', 'amount', 'msg']
    template_name = 'edit_item_form.html'

    def get_success_url(self):
        return reverse('edit_grocery_item',
                       kwargs={'pk': self.get_object().pk})
