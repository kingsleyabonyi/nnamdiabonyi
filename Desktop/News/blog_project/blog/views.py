from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
   model = Post
   template_name = 'home.html'



class BlogDetailView(DetailView):
   model = Post
   template_name = 'post_detail.html'
#    def home(request):
#        return HttpResponse('Home')


class BlogCreateView(CreateView):
   model = Post
   template_name = 'post_new.html'

   fields = '__all__'

class BlogUpdateView(UpdateView):
   model = Post
   template_name = 'edit.html'

   fields = '__all__'


class BlogDeleteView(DeleteView):
   model = Post
   template_name = 'post_delete.html'
   success_url = reverse_lazy('home')

   fields = '__all__'

# class BlogLoginView(LoginView):
#    model = Post
#    template_name = 'login.html'
