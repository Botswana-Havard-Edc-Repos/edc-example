from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.visit import Crf, Requisition
from edc_visit_schedule.schedule import Schedule
from edc_example.lab_profiles import viral_load_panel, rdb_panel

crfs = (
    Crf(show_order=10, model='edc_example.crfone'),
    Crf(show_order=20, model='edc_example.crftwo'),
    Crf(show_order=30, model='edc_example.crfthree'),
    Crf(show_order=40, model='edc_example.crffour'),
    Crf(show_order=50, model='edc_example.crffive'),
)

requisitions = (
    Requisition(show_order=10, model='edc_example.SubjectRequisition', panel=rdb_panel),
    Requisition(show_order=20, model='edc_example.SubjectRequisition', panel=viral_load_panel),
)

# create a visit schedule that contains three schedules, schedule1, schedule2, schedule3
subject_visit_schedule = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='Example Visit Schedule',
    app_label='edc_example',
    visit_model='edc_example.subjectvisit',
    offstudy_model='edc_example.subjectoffstudy',
    default_enrollment_model='edc_example.enrollment',
    default_disenrollment_model='edc_example.disenrollment')

schedule = Schedule(name='schedule1')
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

# create a second schedule
schedule = Schedule(name='schedule2', enrollment_model='edc_example.enrollmenttwo')
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

# create a third schedule
schedule = Schedule(name='schedule3', enrollment_model='edc_example.enrollmentthree')
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
