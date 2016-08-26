from edc_consent.forms_mixins import BaseConsentForm

from .models import SubjectConsent, SubjectConsentProxy


class SubjectConsentForm(BaseConsentForm):

    class Meta:
        model = SubjectConsent
        fields = '__all__'


class SubjectConsentProxyForm(BaseConsentForm):

    class Meta:
        model = SubjectConsentProxy
        fields = '__all__'
