from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, \
    PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, \
    UserTagListView, search, PostTableView, landing, PostListView2, PostListView3
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('search/', search, name='blog-search'),
    path('about/', views.about, name="blog-about"),
    path('', landing, name="landing"),
    path('calendar/', views.calendar, name="calendar"),
    path('archives/', views.archive, name="archive"),
    path('home/', PostListView.as_view(), name="blog-home"),
    path('home2/', PostListView2.as_view(), name="blog-home-2"),
    path('home3/', PostListView3.as_view(), name="blog-home-3"),
    path('post_table/', PostTableView.as_view(), name="post-table"),
    path('<str:tag>', UserTagListView.as_view(), name='user-posts'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name="password_reset_complete"),

    path('password_change/',
        auth_views.PasswordChangeView.as_view(template_name="accounts/password_change_form.html"),
        name="password_change"),

    path('password_change_done/',
        auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done_form.html"),
        name="password_change_done"),
]