from .admin_site import edc_example_admin

from .models import (
    SubjectConsent, Enrollment, SubjectVisit, Appointment, CrfOne, CrfTwo, CrfThree, CrfFour, CrfFive)

edc_example_admin.register(SubjectConsent)
edc_example_admin.register(Enrollment)
edc_example_admin.register(SubjectVisit)
edc_example_admin.register(Appointment)
edc_example_admin.register(CrfOne)
edc_example_admin.register(CrfTwo)
edc_example_admin.register(CrfThree)
edc_example_admin.register(CrfFour)
edc_example_admin.register(CrfFive)
