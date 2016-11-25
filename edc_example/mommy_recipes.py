from model_mommy.recipe import Recipe, seq

from django.utils import timezone

from edc_base.edc_faker import edc_faker as edc_base_faker
from edc_lab.edc_faker import edc_faker as edc_lab_faker
from edc_visit_tracking.constants import SCHEDULED

from .models import SubjectConsent, SubjectVisit, EnrollmentTwo, EnrollmentThree, SubjectRequisition
from edc_example.models import Enrollment
from edc_constants.constants import YES


subjectconsent = Recipe(
    SubjectConsent,
    consent_datetime=timezone.now,
    dob=edc_base_faker.dob_for_consenting_adult,
    first_name=edc_base_faker.first_name,
    last_name=edc_base_faker.last_name,
    initials=edc_base_faker.initials,  # note, passes for model but won't pass validation in modelform clean()
    gender='M',
    identity=seq('12315678'),  # will raise IntegrityError if multiple made without _quantity
    confirm_identity=seq('12315678'),  # will raise IntegrityError if multiple made without _quantity
    identity_type='OMANG',
    is_dob_estimated='-',
)

subjectvisit = Recipe(
    SubjectVisit,
    reason=SCHEDULED)

enrollment = Recipe(
    Enrollment,
    schedule_name='schedule1')

enrollmenttwo = Recipe(
    EnrollmentTwo,
    schedule_name='schedule2')

enrollmentthree = Recipe(
    EnrollmentThree,
    schedule_name='schedule3')

subjectrequisition = Recipe(
    SubjectRequisition,
    requisition_identifier=edc_lab_faker.requisition_identifier,
    specimen_type='WB',
    is_drawn=YES)
