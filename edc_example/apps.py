from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.apps.config import AppConfig as DjangoAppConfig

from edc_consent.apps import AppConfig as EdcConsentAppConfigParent
from edc_timepoint.apps import AppConfig as EdcTimepointAppConfigParent
from edc_timepoint.timepoint import Timepoint
from edc_visit_schedule.apps import AppConfig as EdcVisitScheduleAppConfigParent
from edc_protocol.apps import AppConfig as EdcProtocolAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'edc_example'


class EdcProtocolAppConfig(EdcProtocolAppConfigParent):
    enrollment_caps = {'edc_example.enrollment': ('subject', -1)}  # {label_lower: (key, count)}


class EdcConsentAppConfig(EdcConsentAppConfigParent):
    consent_type_setup = [
        {'app_label': 'edc_example',
         'model_name': 'subjectconsent',
         'start_datetime': datetime.today() + relativedelta(years=-1),
         'end_datetime': datetime.today() + relativedelta(years=+1),
         'version': '1'}
    ]


class EdcTimepointAppConfig(EdcTimepointAppConfigParent):
    timepoints = [
        Timepoint(
            model='edc_example.appointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='CLOSED'
        )
    ]
