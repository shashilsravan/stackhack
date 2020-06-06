from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from django.conf import settings
import datetime
from calendar import monthrange
from django.http import HttpResponse
from .tasks import send_email_task
from django.core.mail import send_mail

def mail(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['shashilsravan.ss.ss@gmail.com'],
                  fail_silently=False)
    return render(request, 'blog/mail.html')

def home(request):
    context = {
        'posts': Post.objects.all(),
        'colors':['red','green'],
    }
    # mail(request)
    return render(request, "blog/home.html", context)

def landing(request):
    context = {
    }
    return render(request, "blog/landing.html", context)

def calendar(request):
    context = {
        'posts': Post.objects.all(),
        'hi': [str(i) for i in range(1, monthrange(int(datetime.datetime.now().year), int(datetime.datetime.now().month))[1]+1)]
    }
    return render(request, "blog/calendar.html", context)

def archive(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "blog/notifications.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # ordering = ['deadline']
    # paginate_by = 2

class PostListView2(ListView):
    model = Post
    template_name = 'blog/created.html'
    context_object_name = 'posts'


class PostListView3(ListView):
    model = Post
    template_name = 'blog/tagwise.html'
    context_object_name = 'posts'

class PostTableView(ListView):
    model = Post
    template_name = 'blog/post_table.html'
    context_object_name = 'posts'
    ordering = ['deadline']

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # paginate_by = 2
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class UserTagListView(ListView):
    model = Post
    template_name = 'blog/user_tags.html'
    context_object_name = 'posts'


    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #
    #     return Post.objects.filter(author = user, tag = tag).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'deadline', 'tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'status', 'deadline', 'tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {})

def search(request):
    template = 'blog/post_list.html'
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains = query) | Q(content__icontains = query) | Q(tag__icontains = query))
    context = {
        'items':results
    }
    return render(request, template, context)