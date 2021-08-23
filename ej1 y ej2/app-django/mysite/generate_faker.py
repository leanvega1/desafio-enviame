
import factory
from api_rest.models import Company

class RandomCompanyFactory(factory.Factory):
    class Meta:
        model = Company

    name = factory.Faker('company')
    rut = factory.Faker('msisdn')

for _ in range(0, 20):
    company = RandomCompanyFactory()
    company.save()
