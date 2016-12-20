from faker import Faker
from model_mommy.recipe import Recipe, seq

from edc_base_test.faker import EdcBaseProvider
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_lab.faker import EdcLabProvider
from edc_visit_tracking.constants import SCHEDULED

from .models import SubjectConsent, SubjectVisit, EnrollmentTwo, EnrollmentThree, SubjectRequisition, Enrollment

fake = Faker()
fake.add_provider(EdcBaseProvider)
fake.add_provider(EdcLabProvider)


subjectconsent = Recipe(
    SubjectConsent,
    consent_datetime=get_utcnow,
    dob=fake.dob_for_consenting_adult,
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials=fake.initials,  # note, passes for model but won't pass validation in modelform clean()
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
    requisition_identifier=fake.requisition_identifier,
    specimen_type='WB',
    is_drawn=YES)
