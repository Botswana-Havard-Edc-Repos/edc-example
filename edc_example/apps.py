from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.apps.config import AppConfig as DjangoAppConfig

from edc_consent.apps import AppConfig as EdcConsentAppConfigParent
from edc_timepoint.apps import AppConfig as EdcTimepointAppConfigParent
from edc_visit_schedule.apps import AppConfig as EdcVisitScheduleAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'edc_example'


class EdcConsentAppConfig(EdcConsentAppConfigParent):
    consent_type_setup = [
        {'app_label': 'edc_example',
         'model_name': 'subjectconsent',
         'start_datetime': datetime.today() + relativedelta(years=-1),
         'end_datetime': datetime.today() + relativedelta(years=+1),
         'version': '1'}
    ]


class EdcTimepointAppConfig(EdcTimepointAppConfigParent):
    timepoint_models = {
        'edc_example.appointment': {
            'datetime_field': 'appt_datetime',  # the datetime field
            'status_field': 'appt_status',  # the status field
            'closed_status': 'CLOSED'  # the value of appt_status when closed
        }
    }
