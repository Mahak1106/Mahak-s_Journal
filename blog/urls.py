from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("journal/", views.journal, name="journal"),
    path("journal/<slug:slug>/", views.post_detail, name="post_detail"),

    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    path("login/", views.login_page, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_user, name="logout"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("new-post/", views.new_post, name="new_post"),
    path("my-posts/", views.my_posts, name="my_posts"),

    path("edit-post/<int:pk>/", views.edit_post, name="edit_post"),
    path("delete-post/<int:pk>/", views.delete_post, name="delete_post"),
]