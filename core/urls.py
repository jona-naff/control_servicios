from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name='home'),
    path('products/',views.servicios,name='servicios'),
    path('products/estados',views.get_estados,name='get_estados'),
    path('products/municipios/<int:estadoid>',views.get_municipios,name='get_municipios'),
    path('products/colonias/<int:municipioid>',views.get_colonias,name='get_colonias'),
    path('logout/',views.exit,name='exit'),
    path('prueba/',views.prueba,name='prueba'),
    path('municipios/',views.get_municipios,name='municipios'),
]