from django import forms

from edc_consent.modelform_mixins import ConsentModelFormMixin

from .models import SubjectConsent


class SubjectConsentForm(ConsentModelFormMixin, forms.ModelForm):

    class Meta:
        model = SubjectConsent
        fields = '__all__'
