import datetime
import factory
from sqlalchemy import Time
from stacktach import models, datetime_to_decimal


class DeploymentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Deployment
    name = factory.Sequence(lambda n: 'name{0}'.format(n))

class RawDataFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.RawData
    deployment = factory.SubFactory(DeploymentFactory)
    when = datetime_to_decimal.dt_to_decimal(datetime.datetime.utcnow())

class InstanceExists(factory.DjangoModelFactory):
    FACTORY_FOR = models.InstanceExists
    status = 'pending'
    raw = factory.SubFactory(RawDataFactory)