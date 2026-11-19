from django.urls import path
from . import views

urlpatterns = [
		path('',views.domace, name="domace" ), 
        path('vizitka/', views.du2_vizitka, name='du2_vizitka'),
	]