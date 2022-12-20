from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('add/', AddExpenseView.as_view(), name='add'),
    path('update/<int:id>/', update, name='update'),
    # path('update/<int:id>/', UpdateExepenseView.as_view(), name='update'),
     path('', TemplateView.as_view(template_name='homepage.html'),name='homepage'),
    # path('', homepage, name='homepage'),
    path('display/', DisplayExepsneView.as_view(), name='display'), 
    path('today/', today, name='today'),
    path('month/', month, name='month'),
    path('year/', year, name='year'),
    path('home/', home, name='home'),
    path('limit/', limit, name='limit'),
    path('delete/<pk>/', DeleteExpenseView.as_view(), name='delete'),
    # path('delete/<int:id>/', delete, name='delete'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search_product/', SearchView.as_view(), name='search_product'),
    
    
]
