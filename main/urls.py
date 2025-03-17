from django.urls import path, URLPattern
from main import views
from main.views import AddNewPostView, GetPostView

app_name = 'main'
urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]

urlpatterns += [
    path('add-new-post/', AddNewPostView.as_view(), name='add-new-post'),
    path('get-posts/', GetPostView.as_view(), name='get-posts'),
]
