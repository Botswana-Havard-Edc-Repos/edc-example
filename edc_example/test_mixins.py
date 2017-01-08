from model_mommy import mommy

from edc_example.models import Appointment, Enrollment, SubjectVisit
from edc_visit_tracking.constants import SCHEDULED


class TestMixin:

    def setUp(self):
        super().setUp()
        self.subject_consent = None
        self.enrollment = None
        self.appointments = None

    def make_enrolled_subject(self):
        self.subject_consent = mommy.make_recipe(
            'edc_example.subjectconsent',
            consent_datetime=self.get_utcnow())
        self.enrollment = mommy.make(
            Enrollment,
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=self.subject_consent.consent_datetime,
            visit_schedule_name=Enrollment._meta.visit_schedule_name.split('.')[0],
            schedule_name=Enrollment._meta.visit_schedule_name.split('.')[-1])
        self.appointments = Appointment.objects.all().order_by('appt_datetime')
        self.subject_identifier = self.subject_consent.subject_identifier

    def add_visit(self, appointment):
        mommy.make(
            SubjectVisit,
            appointment=appointment,
            report_datetime=appointment.appt_datetime,
            reason=SCHEDULED)
