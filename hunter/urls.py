from django.contrib import admin
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from Hunter_App.views import login_view, index_view,  personal_view# Asumiendo que estas vistas están en Hunter_App.views

# No hay necesidad de importar views nuevamente si ya lo has hecho desde Hunter_App

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path('personal/',personal_view, name='personal_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
