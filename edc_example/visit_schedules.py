from edc_example.models import SubjectVisit, Enrollment

from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.visit import Crf, Requisition
from edc_visit_schedule.schedule import Schedule

crfs = (
    Crf(show_order=10, model='edc_example.crfone'),
    Crf(show_order=20, model='edc_example.crftwo'),
    Crf(show_order=30, model='edc_example.crfthree'),
    Crf(show_order=40, model='edc_example.crffour'),
    Crf(show_order=50, model='edc_example.crffive'),
)

requisitions = (
    Requisition(
        show_order=10, model='edc_example.RequisitionOne',
        panel_name='Research Blood Draw', panel_type='TEST', aliqout_type_alpha_code='WB'),
    Requisition(
        show_order=20, model='edc_example.RequisitionTwo',
        panel_name='Viral Load', panel_type='TEST', aliqout_type_alpha_code='WB'),
)

subject_visit_schedule = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='Example Visit Schedule',
    app_label='edc_example',
    visit_model=SubjectVisit,
)

# add schedules
schedule = Schedule(name='schedule-1', enrollment_model=Enrollment)

# add visits to this schedule
schedule.add_visit(
    code='1000',
    title='Visit 1000',
    timepoint=0,
    base_interval=0,
    requisitions=requisitions,
    crfs=crfs)
schedule.add_visit(
    code='2000',
    title='Visit 2000',
    timepoint=1,
    base_interval=1,
    requisitions=requisitions,
    crfs=crfs)
schedule.add_visit(
    code='3000',
    title='Visit 3000',
    timepoint=2,
    base_interval=2,
    requisitions=requisitions,
    crfs=crfs)
schedule.add_visit(
    code='4000',
    title='Visit 4000',
    timepoint=3,
    base_interval=3,
    requisitions=requisitions,
    crfs=crfs)

subject_visit_schedule.add_schedule(schedule)

# register the visit_schedule
site_visit_schedules.register(subject_visit_schedule)
