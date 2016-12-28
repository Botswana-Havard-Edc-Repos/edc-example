from django.apps.config import AppConfig as DjangoAppConfig

from edc_timepoint.apps import AppConfig as EdcTimepointAppConfigParent
from edc_timepoint.timepoint import Timepoint
from edc_protocol.apps import AppConfig as EdcProtocolAppConfigParent
from edc_protocol.cap import Cap
from edc_protocol.subject_type import SubjectType


class AppConfig(DjangoAppConfig):
    name = 'edc_example'


class EdcProtocolAppConfig(EdcProtocolAppConfigParent):
    subject_types = [
        SubjectType('subject', 'Research Subjects', Cap(model_name='edc_example.enrollment', max_subjects=9999)),
        SubjectType('subject', 'Research Subjects', Cap(model_name='edc_example.enrollmenttwo', max_subjects=9999)),
        SubjectType('subject', 'Research Subjects', Cap(model_name='edc_example.enrollmentthree', max_subjects=5))
    ]


class EdcTimepointAppConfig(EdcTimepointAppConfigParent):
    timepoints = [
        Timepoint(
            model='edc_appointment.appointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='CLOSED'
        )
    ]
