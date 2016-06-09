from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from users.views import vista_login, vista_logout, vista_registre, vista_perfil, vista_clau

urlpatterns = (
    [
        url(r'^admin/', admin.site.urls),
        url(r'^', include('items.urls', namespace="items")),
        url(r'^cart/', include('carts.urls', namespace="carts")),
        url(r'^backups/', include('backups.urls', namespace="backups")),
        url(r'^login/$', vista_login, name="login"),
        url(r'^logout/$', vista_logout, name="logout"),
        url(r'^registration/$', vista_registre, name="registration"),
        url(r'^profile/$', vista_perfil, name="profile"),
        url(r'^profile/reset/$', vista_clau, name="resetPassword")
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))