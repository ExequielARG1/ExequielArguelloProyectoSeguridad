from django.contrib import admin
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from Hunter_App.views import login_view, index_view, ubicacion_views,  personal_view, acerca_de_nosotros, change_avatar, contact, delete_message, acercademi#


urlpatterns = [
    path('', index_view, name='index'), 
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path('personal/',personal_view, name='personal_view'),
    path('ubicacion/', ubicacion_views, name='ubicacion'),
    path('acerca/', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('change_avatar/', change_avatar, name='change_avatar'),
    path('contact/', contact, name='contact'),
    path('contact/delete/<int:message_id>/', delete_message, name='delete_message'),
    path('acercademi/', acercademi, name='acercademi'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
