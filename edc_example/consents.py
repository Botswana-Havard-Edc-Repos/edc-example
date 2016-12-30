from django.apps import apps as django_apps

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

app_config = django_apps.get_app_config('edc_protocol')

subjectconsent_v1 = Consent(
    'edc_example.subjectconsent',
    version='1',
    start=app_config.study_open_datetime,
    end=app_config.study_close_datetime,
    age_min=16,
    age_is_adult=18,
    age_max=64,
    gender=[MALE, FEMALE],
    subject_type='subject')

site_consents.register(subjectconsent_v1)
