from edc_constants.constants import MALE, FEMALE
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_rule_groups.logic import Logic
from edc_rule_groups.crf_rule import CrfRule
# RequisitionRule
from edc_rule_groups.rule_group import RuleGroup
from edc_rule_groups.predicate import P
from edc_rule_groups.decorators import register


@register()
class ExampleRuleGroup(RuleGroup):

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
class ExampleRuleGroup2(RuleGroup):

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
