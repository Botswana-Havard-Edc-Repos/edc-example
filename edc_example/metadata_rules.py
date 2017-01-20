from edc_constants.constants import MALE, FEMALE, YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules.crf_rule import CrfRule
from edc_metadata.rules.decorators import register
from edc_metadata.rules.logic import Logic
from edc_metadata.rules.predicate import P
from edc_metadata.rules.requisition_rule import RequisitionRule
from edc_metadata.rules.rule_group import RuleGroup

from .labs import viral_load_panel, rdb_panel


@register()
class ExampleCrfRuleGroup(RuleGroup):

    crfs_male = CrfRule(
        logic=Logic(
            predicate=P('gender', 'eq', MALE),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['crffour', 'crffive'])

    crfs_female = CrfRule(
        logic=Logic(
            predicate=P('gender', 'eq', FEMALE),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['crftwo', 'crfthree'])

    class Meta:
        app_label = 'edc_example'


@register()
class ExampleCrfRuleGroup2(RuleGroup):

    car = CrfRule(
        logic=Logic(
            predicate=P('f1', 'eq', 'car'),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['crftwo'])

    bicycle = CrfRule(
        logic=Logic(
            predicate=P('f1', 'eq', 'bicycle'),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['crfthree'])

    class Meta:
        app_label = 'edc_example'
        source_model = 'edc_example.crfone'


@register()
class ExampleRequisitionRuleGroup(RuleGroup):

    require_vl = RequisitionRule(
        logic=Logic(
            predicate=P('vl', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='subjectrequisition',
        target_panels=[viral_load_panel])

    require_rdb = RequisitionRule(
        logic=Logic(
            predicate=P('rdb', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='subjectrequisition',
        target_panels=[rdb_panel])

    class Meta:
        app_label = 'edc_example'
        source_model = 'edc_example.crfone'
