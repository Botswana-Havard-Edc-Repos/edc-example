from dateutil.relativedelta import relativedelta
from django.apps.config import AppConfig as DjangoAppConfig
from django.utils import timezone

from edc_consent.apps import AppConfig as EdcConsentAppConfigParent
from edc_consent.consent_config import ConsentConfig
from edc_timepoint.apps import AppConfig as EdcTimepointAppConfigParent
from edc_timepoint.timepoint import Timepoint
from edc_protocol.apps import AppConfig as EdcProtocolAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'edc_example'


class EdcProtocolAppConfig(EdcProtocolAppConfigParent):
    enrollment_caps = {'edc_example.enrollment': ('subject', -1)}  # {label_lower: (key, count)}


class EdcConsentAppConfig(EdcConsentAppConfigParent):
    consent_configs = [
        ConsentConfig(
            'edc_example.subjectconsent',
            version='1',
            start=timezone.now() - relativedelta(years=1),
            end=timezone.now() + relativedelta(years=1),
            age_min=16,
            age_is_adult=18,
            age_max=64,
            gender=['M', 'F']),
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
