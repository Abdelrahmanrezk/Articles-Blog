from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	context ={
		'posts': Post.objects.all()
	}
	return render(request, 'my_blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'my_blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
		
class PostDetialView(DetailView):
	model = Post
	template_name = 'my_blog/post_details.html'


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'my_blog/post_create.html'
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'my_blog/post_update.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self): # this func prevent other user to edit another user post
		post = self.get_object()
		if self.request.user == post.user:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'my_blog/post_delete.html'
	success_url = '/'
	def test_func(self): # this func prevent other user to delete another user post
		post = self.get_object()
		if self.request.user == post.user:
			return True
		else:
			return False

def about_us(request):
	return render(request, 'my_blog/about.html')




