from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from Documents import views
from DocServer.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sign_up/$', views.SignUp),
    url(r'^sign_in/$', views.SignIn),
    url(r'^licence/$', views.ShowLicence),
    url(r'^refresh_token/$', views.RefreshTOKEN),
    url(r'^clear_token/$', views.ClearTOKEN),
    url(r'^contact/', views.contac),
    url(r'^filer/', include('filer.urls')),
    url(r'^get_root/$', views.GetRootFolders),
    url(r'^get_folder/$', views.GetAllFromFolder),
    url(r'^find_root/$', views.FindByRoot),
    url(r'^find_folder/$', views.FindByFolder),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
