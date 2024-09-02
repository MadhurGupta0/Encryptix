from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,detail,signup,new,delete,edit,item,lout
from django.contrib.auth import views as auth_views
from .form import LoginForm

urlpatterns = [
    path('index/',index,name="index"),
    path('item/',item,name='items'),
    path('new/',new, name="new"),
    path('signup/',signup, name="signup"),
    path('',auth_views.LoginView.as_view(authentication_form=LoginForm,template_name="login.html"), name="login"),
    path('<int:pk>/',detail, name="detail"),
    path('<int:pk>/delete/',delete, name='delete'),
    path('<int:pk>/edit/',edit,name='edit'),
    path('logout/',lout,name="logout")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

