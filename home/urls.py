#urls
from django.urls import path
from .views import * 
urlpatterns = [
    path('',                            index,      name="home"),
    path('create/',                     create,     name="create_article"),
    path('detail/<slug:slug>/',         detail,     name="article_detail"),
    path('update/<int:id>/',            update,     name="update_article"),
    path('delete/<int:id>/',            delete,     name="delete_article"),
    path('accounts/login/',              login_view, name="login")

]