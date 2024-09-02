import json
from faker import Faker

# Initialize the Faker object
fake = Faker()

# Function to generate fake data
def generate_fake_data(num_entries=10):
    data = []
    for _ in range(num_entries):
        entry = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "job": fake.job(),
            "company": fake.company(),
            "birthdate": fake.date_of_birth().isoformat(),
            "credit_card": {
                "number": fake.credit_card_number(),
                "provider": fake.credit_card_provider(),
                "expiration_date": fake.credit_card_expire(),
            },
            "ssn": fake.ssn()
        }
        data.append(entry)
    return data

# Number of fake entries you want to generate
num_entries = 10000

# Generate the fake data
fake_data = generate_fake_data(num_entries)


# Write the fake data to a JSON file
with open('GenerativeAI/Data/fake_data.json', 'w') as json_file:
    json.dump(fake_data, json_file, indent=4)

print(f"Generated {num_entries} fake entries and saved to fake_data.json")
