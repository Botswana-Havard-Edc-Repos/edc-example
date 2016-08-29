import factory

from datetime import date
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from faker import Factory as FakerFactory

from edc_example.models import SubjectConsent, SubjectVisit, Enrollment
from edc_constants.constants import YES, NO

faker = FakerFactory.create()


class SubjectConsentFactory(factory.DjangoModelFactory):

    class Meta:
        model = SubjectConsent

    confirm_identity = '123156789'
    consent_datetime = timezone.now() - relativedelta(minutes=45)
    dob = date.today() - relativedelta(years=25)
    first_name = factory.LazyAttribute(lambda x: 'E{}'.format(faker.first_name().upper()))
    gender = 'M'
    identity = '123156789'
    identity_type = 'OMANG'
    initials = 'EE'
    is_dob_estimated = '-'
    is_incarcerated = NO
    is_literate = YES
    language = 'en'
    last_name = factory.LazyAttribute(lambda x: 'E{}'.format(faker.last_name().upper()))
    study_site = '40'
    subject_identifier = '12345'
    subject_type = 'subject'
    witness_name = None
    assessment_score = YES
    consent_reviewed = YES
    consent_signature = YES
    study_questions = YES
    citizen = YES
    consent_copy = YES


class SubjectVisitFactory(factory.DjangoModelFactory):

    class Meta:
        model = SubjectVisit

    # subject_identifier = '12345'
    report_datetime = timezone.now() - relativedelta(minutes=30)


class EnrollmentFactory(factory.DjangoModelFactory):

    report_datetime = timezone.now() - relativedelta(minutes=15)

    class Meta:
        model = Enrollment
