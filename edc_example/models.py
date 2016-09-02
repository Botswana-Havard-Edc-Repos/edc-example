from django.db import models
from django.utils import timezone

from edc_appointment.model_mixins import AppointmentModelMixin, CreateAppointmentsMixin
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.model_mixins import RequiresConsentMixin
from edc_lab.requisition.model_mixins import RequisitionModelMixin
from edc_metadata.model_mixins import (
    CrfMetadataModelMixin, RequisitionMetadataModelMixin, CreatesMetadataModelMixin,
    UpdateCrfMetadataModelMixin, UpdateRequisitionMetadataModelMixin)
from edc_registration.model_mixins import RegisteredSubjectModelMixin, RegisteredSubjectMixin
from edc_registration.model_mixins import RegistrationMixin
from edc_visit_tracking.model_mixins import CrfModelMixin, CrfInlineModelMixin, PreviousVisitModelMixin, VisitModelMixin
from edc_lab.aliquot.model_mixins import AliquotModelMixin
from edc_lab.specimen.model_mixins import SpecimenCollectionModelMixin, SpecimenCollectionItemModelMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class SubjectConsent(ConsentModelMixin, RegistrationMixin, IdentityFieldsMixin,
                     ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin,
                     BaseUuidModel):

    class Meta:
        app_label = 'edc_example'
        unique_together = ['subject_identifier', 'version']


class Enrollment(CreateAppointmentsMixin, RegisteredSubjectMixin, RequiresConsentMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(default=timezone.now)

    is_eligible = models.BooleanField(default=True)

    class Meta:
        visit_schedule_name = 'subject_visit_schedule'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class Appointment(AppointmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta:
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class SubjectVisit(VisitModelMixin, CreatesMetadataModelMixin, RequiresConsentMixin,
                   PreviousVisitModelMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    class Meta:
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class CrfOne(CrfModelMixin, RequiresConsentMixin, UpdateCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class OtherModel(BaseUuidModel):

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'


class BadCrfOneInline(CrfInlineModelMixin, RequiresConsentMixin, BaseUuidModel):

    crf_one = models.ForeignKey(CrfOne)

    other_model = models.ForeignKey(OtherModel)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class CrfOneInline(CrfInlineModelMixin, RequiresConsentMixin, BaseUuidModel):

    crf_one = models.ForeignKey(CrfOne)

    other_model = models.ForeignKey(OtherModel)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        consent_model = 'edc_example.subjectconsent'
        crf_inline_parent = 'crf_one'
        app_label = 'edc_example'


class CrfTwo(CrfModelMixin, RequiresConsentMixin, UpdateCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'


class CrfThree(CrfModelMixin, RequiresConsentMixin, UpdateCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'


class CrfFour(CrfModelMixin, RequiresConsentMixin, UpdateCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'


class CrfFive(CrfModelMixin, RequiresConsentMixin, UpdateCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'


class CrfSix(CrfModelMixin, RequiresConsentMixin, UpdateCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'


class Panel(BaseUuidModel):

    name = models.CharField(max_length=25)

    class Meta:
        app_label = 'edc_example'


class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                         UpdateRequisitionMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class RequisitionTwo(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                     UpdateRequisitionMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class Aliquot(AliquotModelMixin, BaseUuidModel):

    class Meta(AliquotModelMixin.Meta):
        app_label = 'edc_example'


class SpecimenCollection(SpecimenCollectionModelMixin, BaseUuidModel):

    class Meta(SpecimenCollectionModelMixin.Meta):
        app_label = 'edc_example'


class SpecimenCollectionItem(SpecimenCollectionItemModelMixin, BaseUuidModel):

    specimen_collection = models.ForeignKey(SpecimenCollection)

    class Meta(SpecimenCollectionItemModelMixin.Meta):
        app_label = 'edc_example'


class CrfMetadata(CrfMetadataModelMixin, BaseUuidModel):

    class Meta(CrfMetadataModelMixin.Meta):
        app_label = 'edc_example'


class RequisitionMetadata(RequisitionMetadataModelMixin, BaseUuidModel):

    class Meta(RequisitionMetadataModelMixin.Meta):
        app_label = 'edc_example'
