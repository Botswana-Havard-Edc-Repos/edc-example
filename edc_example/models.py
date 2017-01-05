from django.db import models
from django.db.models.deletion import PROTECT

from django_crypto_fields.crypt_model_mixin import CryptModelMixin
from django_crypto_fields.fields.encrypted_char_field import EncryptedCharField

from edc_appointment.models import Appointment
from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model.models import BaseUuidModel, ListModelMixin, HistoricalRecords
from edc_consent.field_mixins import (
    ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin)
from edc_consent.field_mixins.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.model_mixins import RequiresConsentMixin
from edc_constants.constants import NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_lab.model_mixins import RequisitionModelMixin
from edc_metadata.model_mixins import (
    CreatesMetadataModelMixin, UpdatesCrfMetadataModelMixin, UpdatesRequisitionMetadataModelMixin)
from edc_offstudy.model_mixins import OffstudyModelMixin, OffstudyMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_visit_tracking.model_mixins import CrfModelMixin, CrfInlineModelMixin, VisitModelMixin
from edc_visit_schedule.model_mixins import DisenrollmentModelMixin, EnrollmentModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_protocol.model_mixins import SubjectTypeCapMixin


class SubjectConsent(ConsentModelMixin, NonUniqueSubjectIdentifierModelMixin, UpdatesOrCreatesRegistrationModelMixin,
                     IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin,
                     VulnerabilityFieldsMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'
        unique_together = ['subject_identifier', 'version']


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):

    objects = models.Manager()

    history = HistoricalRecords()

    class Meta:
        app_label = 'edc_example'
        visit_schedule_name = 'subject_visit_schedule'
        consent_model = 'edc_example.subjectconsent'


class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta(EnrollmentModelMixin.Meta):
        visit_schedule_name = 'subject_visit_schedule.schedule1'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class EnrollmentTwo(EnrollmentModelMixin, SubjectTypeCapMixin, CreateAppointmentsMixin,
                    RequiresConsentMixin, BaseUuidModel):

    subject_type = models.CharField(max_length=15, editable=False)

    class Meta(EnrollmentModelMixin.Meta):
        visit_schedule_name = 'subject_visit_schedule.schedule2'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class EnrollmentThree(EnrollmentModelMixin, SubjectTypeCapMixin, CreateAppointmentsMixin,
                      RequiresConsentMixin, BaseUuidModel):
    """Includes schedule_name on Meta"""
    class Meta(EnrollmentModelMixin.Meta):
        visit_schedule_name = 'subject_visit_schedule.schedule3'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'
        subject_type_name = 'subject'


class Disenrollment(DisenrollmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'subject_visit_schedule.schedule1'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class DisenrollmentTwo(DisenrollmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'subject_visit_schedule.schedule2'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class DisenrollmentThree(DisenrollmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'subject_visit_schedule.schedule3'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class SubjectVisit(
        VisitModelMixin, OffstudyMixin, CreatesMetadataModelMixin, RequiresConsentMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment, on_delete=PROTECT)

    objects = VisitModelManager()

    class Meta(VisitModelMixin.Meta):
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class CrfOne(CrfModelMixin, OffstudyMixin, RequiresConsentMixin, UpdatesCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    vl = models.CharField(max_length=10, default=NO)

    rdb = models.CharField(max_length=10, default=NO)

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


class CrfTwo(CrfModelMixin, OffstudyMixin, RequiresConsentMixin, UpdatesCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class CrfThree(CrfModelMixin, OffstudyMixin, RequiresConsentMixin, UpdatesCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class CrfFour(CrfModelMixin, OffstudyMixin, RequiresConsentMixin, UpdatesCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class CrfFive(CrfModelMixin, OffstudyMixin, RequiresConsentMixin, UpdatesCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class CrfSix(CrfModelMixin, OffstudyMixin, RequiresConsentMixin, UpdatesCrfMetadataModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class Panel(BaseUuidModel):

    name = models.CharField(max_length=25)

    class Meta:
        app_label = 'edc_example'


class SubjectRequisition(CrfModelMixin, OffstudyMixin, RequisitionModelMixin, RequiresConsentMixin,
                         UpdatesRequisitionMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class RequisitionTwo(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                     UpdatesRequisitionMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    class Meta:
        app_label = 'edc_example'
        consent_model = 'edc_example.subjectconsent'


class Crypt(CryptModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'
        unique_together = (('hash', 'algorithm', 'mode'),)


class BadTestModel(BaseUuidModel):
    """A test model that is missing natural_key and get_by_natural_key."""

    f1 = models.CharField(max_length=10, default='f1')

    objects = models.Manager()

    class Meta:
        app_label = 'edc_example'


class AnotherBadTestModel(BaseUuidModel):
    """A test model that is missing get_by_natural_key."""

    f1 = models.CharField(max_length=10, default='f1')

    objects = models.Manager()

    def natural_key(self):
        return (self.f1, )

    class Meta:
        app_label = 'edc_example'


class TestModelManager(models.Manager):

    def get_by_natural_key(self, f1):
        return self.get(f1=f1)


class TestModel(BaseUuidModel):

    f1 = models.CharField(max_length=10, unique=True)

    objects = TestModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.f1, )

    class Meta:
        app_label = 'edc_example'


class TestModelProxy(TestModel):

    class Meta:
        app_label = 'edc_example'
        proxy = True


class TestEncryptedModel(BaseUuidModel):

    f1 = models.CharField(max_length=10, unique=True)

    encrypted = EncryptedCharField(max_length=10, unique=True)

    objects = TestModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.f1, )

    class Meta:
        app_label = 'edc_example'


class M2m(ListModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class FkManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Fk(BaseUuidModel):

    name = models.CharField(max_length=10, unique=True)

    objects = FkManager()

    def natural_key(self):
        return (self.name, )

    class Meta:
        app_label = 'edc_example'


class ComplexTestModelManager(models.Manager):

    def get_by_natural_key(self, f1, fk):
        return self.get(f1=f1, fk=fk)


class ComplexTestModel(BaseUuidModel):

    f1 = models.CharField(max_length=10)

    fk = models.ForeignKey(Fk)

    m2m = models.ManyToManyField(M2m)

    objects = ComplexTestModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.f1, ) + self.fk.natural_key()
    natural_key.dependencies = ['edc_example.fk']

    class Meta:
        app_label = 'edc_example'
        unique_together = ('f1', 'fk')
