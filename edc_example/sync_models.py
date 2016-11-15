from edc_sync.site_sync_models import site_sync_models
from edc_sync.sync_model import SyncModel

sync_models = [
    'edc_example.crypt',
    'edc_example.badtestmodel',
    'edc_example.anotherbadtestmodel',
    'edc_example.testmodel',
    'edc_example.TestModelProxy',
    'edc_example.TestEncryptedModel',
    'edc_example.M2M',
    'edc_example.ComplexTestModel',
]

site_sync_models.register(sync_models, SyncModel)
