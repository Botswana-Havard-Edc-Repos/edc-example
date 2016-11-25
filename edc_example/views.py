from django.views.generic.base import TemplateView

from edc_base.views import EdcBaseViewMixin


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'edc_example/home.html'

    def __init__(self, *args, **kwargs):
        super(HomeView, self).__init__(*args, **kwargs)
