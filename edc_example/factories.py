import factory

from faker import Factory as FakerFactory

from django.utils import timezone
from datetime import date
from edc_example.models import SubjectConsent, SubjectConsentProxy
from dateutil.relativedelta import relativedelta
from edc_constants.constants import YES, NO

faker = FakerFactory.create()


class SubjectConsentFactory(factory.DjangoModelFactory):

    class Meta:
        model = SubjectConsent

    subject_identifier = '12345'
    study_site = '40'
    first_name = factory.LazyAttribute(lambda x: 'E{}'.format(faker.first_name().upper()))
    last_name = factory.LazyAttribute(lambda x: 'E{}'.format(faker.last_name().upper()))
    initials = 'EE'
    gender = 'M'
    consent_datetime = timezone.now()
    dob = date.today() - relativedelta(years=25)
    is_dob_estimated = '-'
    identity = '123156789'
    confirm_identity = '123156789'
    identity_type = 'OMANG'
    is_literate = YES
    is_incarcerated = NO
    witness_name = None
    language = 'en'
    subject_type = 'subject'
    consent_datetime = timezone.now()


class SubjectConsentProxyFactory(factory.DjangoModelFactory):

    class Meta:
        model = SubjectConsentProxy

    subject_identifier = '12345'
    study_site = '40'
    first_name = 'ERIK'
    last_name = 'ERIKS'
    initials = 'EE'
    gender = 'M'
    consent_datetime = timezone.now()
    dob = date.today() - relativedelta(years=25)
    is_dob_estimated = '-'
    identity = '123156789'
    confirm_identity = '123156789'
    identity_type = 'OMANG'
    is_literate = YES
    is_incarcerated = NO
    language = 'en'
    subject_type = 'subject'
    consent_datetime = timezone.now()
