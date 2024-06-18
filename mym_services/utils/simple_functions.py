from faker import Faker

from mym_services.users.models import Company

fake = Faker()


def generate_companies(num_companies):
    for _ in range(num_companies):
        company = {
            "ruc_number": fake.random_number(digits=11, fix_len=True),
            "company_name": fake.company(),
            "address": fake.address(),
            "district": fake.city(),
        }
        Company.objects.create(**company)
