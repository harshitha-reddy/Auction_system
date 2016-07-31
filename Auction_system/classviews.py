from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.conf.urls import url
from models import *
from django.views.generic.edit import UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from Auction_system.forms import *
from django.http import *
from django.contrib.auth import authenticate, login, logout
from forms import UserCreateForm

class View(ListView):
    model=product
    #template_name = 'good_list.html'

class CreateProductView(CreateView):
    model=product
    fields=["name","createdby","price","category","noitem","purdate","image"]

    def form_valid(self,form):
        object=Seller(username=self.request.user,product_id=form.save())
        object.save()
        return super(CreateProductView,self).form_valid(form)
    def get_success_url(self):
        return reverse('product_view')

class ProductDetailView(DetailView):
    model=product
    context_object_name = 'product_list'

    def get_context_data(self,**kwargs):
        context=super(ProductDetailView,self).get_context_data(**kwargs)
        context["Seller"] = Seller.objects.get(product_id=self.kwargs['pk'])
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm

    def get_success_url(self):
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password1'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return reverse('product_view')
        return reverse('register')


class BuyerListView(ListView):
    model=Buyer
    def get_queryset(self):
        return Buyer.objects.filter(product_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(BuyerListView, self).get_context_data(**kwargs)
        context["product_id"] = self.kwargs['pk']
        return context
#class add_product(request):
#	 name=request.POSTS.objects.all()
#	 if request.method=='GET':
#		form=ProductForm()
#	 else:
#		user=User.objects.get(pk=request.user.id)
#		form=ProductForm(request.POST,request.FILES)
#		p=Good(pname=request.POST.get("pame"),desription

class ProductDelete(DeleteView):
    model = product

    def get_context_data(self, **kwargs):
        context = super(ProductDelete, self).get_context_data(**kwargs)
        context["product_id"] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('product_view')