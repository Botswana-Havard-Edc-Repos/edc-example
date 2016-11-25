from model_mommy.recipe import Recipe, seq

from django.utils import timezone

from edc_base.edc_faker import edc_faker

from .models import SubjectConsent


subjectconsent = Recipe(
    SubjectConsent,
    consent_datetime=timezone.now,
    dob=edc_faker.dob_for_consenting_adult,
    first_name=edc_faker.first_name,
    last_name=edc_faker.last_name,
    initials=edc_faker.initials,  # note, passes for model but won't pass validation in modelform clean()
    gender='M',
    identity=seq('12315678'),  # will raise IntegrityError if multiple made without _quantity
    confirm_identity=seq('12315678'),  # will raise IntegrityError if multiple made without _quantity
    identity_type='OMANG',
    is_dob_estimated='-',
)
