from django.db import models
from django.utils import timezone

from django_crypto_fields.crypt_model_mixin import CryptModelMixin
from django_crypto_fields.fields.encrypted_char_field import EncryptedCharField

from edc_appointment.model_mixins import AppointmentModelMixin, CreateAppointmentsMixin
from edc_base.model.models import BaseUuidModel, ListModelMixin, HistoricalRecords
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.model_mixins import RequiresConsentMixin
from edc_constants.constants import NO
from edc_lab.model_mixins import (
    RequisitionModelMixin, AliquotModelMixin, SpecimenCollectionModelMixin, SpecimenCollectionItemModelMixin)
from edc_metadata.model_mixins import (
    CrfMetadataModelMixin, RequisitionMetadataModelMixin, CreatesMetadataModelMixin,
    UpdatesCrfMetadataModelMixin, UpdatesRequisitionMetadataModelMixin)
from edc_registration.model_mixins import RegisteredSubjectModelMixin, RegisteredSubjectMixin
from edc_registration.model_mixins import RegistrationMixin
from edc_visit_tracking.model_mixins import CrfModelMixin, CrfInlineModelMixin, VisitModelMixin
from edc_offstudy.model_mixins import OffstudyModelMixin, OffstudyMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class SubjectConsent(ConsentModelMixin, RegistrationMixin, IdentityFieldsMixin,
                     ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin,
                     BaseUuidModel):

    class Meta:
        app_label = 'edc_example'
        unique_together = ['subject_identifier', 'version']


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class Enrollment(CreateAppointmentsMixin, RegisteredSubjectMixin, RequiresConsentMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(default=timezone.now)

    is_eligible = models.BooleanField(default=True)

    class Meta:
        visit_schedule_name = 'subject_visit_schedule'
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class Appointment(AppointmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta(AppointmentModelMixin.Meta):
        consent_model = 'edc_example.subjectconsent'
        app_label = 'edc_example'


class SubjectVisit(VisitModelMixin, OffstudyMixin, CreatesMetadataModelMixin, RequiresConsentMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

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
        offstudy_model = 'edc_example.subjectoffstudy'


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
    natural_key.dependencies = ['example.fk']

    class Meta:
        app_label = 'edc_example'
        unique_together = ('f1', 'fk')
