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
    url(r'^user_test/$', views.DeleteUserForTESTING),
    url(r'^contact/', views.contac),
    url(r'^filer/', include('filer.urls')),
    url(r'^files/$', views.GetFiles),
    url(r'^root_folders/$', views.GetRootFolders),
    url(r'^get_folder/$', views.GetAllFromFolder),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

