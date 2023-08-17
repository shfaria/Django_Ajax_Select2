from django.contrib import admin
from django.urls import path
from dummy.views import home, dumView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('dum/', dumView),

]
