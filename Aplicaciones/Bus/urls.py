from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name="inicio"),
    path('1',views.uno, name="1"),
    path('2',views.dos, name="2"),
    path('3',views.tres, name="3"),
    path('4',views.cuatro, name="4"),
    path('5',views.cinco, name="5"),
    path('6',views.seis, name="6"),
    path('7',views.siete, name="7"),
    path('8',views.ocho, name="8"),
    path('9',views.nueve, name="9"),
    path('10',views.diez, name="10"),
    path('11',views.once, name="11"),
    path('12',views.doce, name="12"),
    path('13',views.trece, name="13"),
    path('14',views.catorce, name="14"),
    path('15',views.quince, name="15")





]