from django.urls import path 
from users.views import login_view, orders_view, calculators_view, home_page


urlpatterns = [
    path('login/',login_view,name='Login'),
    path('orders/',orders_view, name='Orders'),
    path('calculator/',calculators_view),
    path('',home_page)
]