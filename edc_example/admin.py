from django.contrib import admin

from .admin_site import edc_example_admin

from .models import (SubjectConsent, Enrollment, SubjectVisit,
                     Appointment, CrfOne, CrfTwo, CrfThree, CrfFour, CrfFive)
from edc_example.forms import SubjectConsentForm


@admin.register(SubjectConsent, site=edc_example_admin)
class SubjectConsentAdmin(admin.ModelAdmin):
    form = SubjectConsentForm


edc_example_admin.register(Enrollment)
edc_example_admin.register(SubjectVisit)
edc_example_admin.register(Appointment)
edc_example_admin.register(CrfOne)
edc_example_admin.register(CrfTwo)
edc_example_admin.register(CrfThree)
edc_example_admin.register(CrfFour)
edc_example_admin.register(CrfFive)
