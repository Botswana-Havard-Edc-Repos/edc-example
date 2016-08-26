from django.db import models
from django.utils import timezone
from edc_appointment.model_mixins import AppointmentModelMixin, CreateAppointmentsMixin
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.model_mixins import RequiresConsentMixin
from edc_consent.models.fields import ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin
from edc_consent.models.fields.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_meta_data.managers import CrfMetaDataManager
from edc_meta_data.mixins import CrfMetaDataMixin
from edc_meta_data.model_mixins import CrfMetaDataModelMixin, RequisitionMetaDataModelMixin
from edc_registration.model_mixins import RegisteredSubjectModelMixin, RegisteredSubjectMixin
from edc_registration.model_mixins import RegistrationMixin
from edc_timepoint.model_mixins import TimepointStatusMixin
from edc_visit_tracking.model_mixins import CrfModelMixin, PreviousVisitModelMixin, VisitModelMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class SubjectConsent(ConsentModelMixin, RegistrationMixin, IdentityFieldsMixin,
                     ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin,
                     BaseUuidModel):

    class Meta:
        app_label = 'edc_example'
        unique_together = ['subject_identifier', 'version']


class SubjectConsentProxy(SubjectConsent):

    class Meta:
        app_label = 'edc_example'  # required!
        proxy = True


class Enrollment(CreateAppointmentsMixin, RegisteredSubjectMixin, RequiresConsentMixin, BaseUuidModel):

    visit_schedule_name = 'subject_visit_schedule'

    consent_model = 'edc_example.subjectconsent'

    report_datetime = models.DateTimeField(default=timezone.now)

    registration_datetime = models.DateTimeField(default=timezone.now)

    is_eligible = models.BooleanField(default=True)

    class Meta:
        app_label = 'edc_example'


class Appointment(AppointmentModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class SubjectVisit(CrfMetaDataMixin, PreviousVisitModelMixin, VisitModelMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    class Meta:
        app_label = 'edc_example'


class CrfOne(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    consent_model = 'edc_example.subjectconsent'

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class CrfTwo(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class CrfThree(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class CrfFour(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class CrfFive(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class CrfSix(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class RequisitionOne(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    panel_name = models.CharField(max_length=25, null=True)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class RequisitionTwo(CrfModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    panel_name = models.CharField(max_length=25, null=True)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class CrfMetaData(CrfMetaDataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta:
        app_label = 'edc_example'


class RequisitionMetaData(RequisitionMetaDataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta:
        app_label = 'edc_example'
