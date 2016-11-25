from django.contrib import admin
from django.conf.urls import include, url

from edc_base.views import LoginView
from edc_base.views import LogoutView

from .admin_site import edc_example_admin
# from .views import HomeView

urlpatterns = [
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(pattern_name='login_url'), name='logout_url'),
    url(r'^admin/', edc_example_admin.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^edc-visit-schedule/', include('edc_visit_schedule.urls')),
    url(r'^edc/', include('edc_base.urls', namespace='edc-base')),
#     url(r'^', HomeView.as_view(), name='home_url'),
]
