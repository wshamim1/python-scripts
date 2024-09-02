import csv
from faker import Faker

# Initialize the Faker object
fake = Faker()

# Function to generate fake data
def generate_fake_data(num_entries=10):
    data = []
    for _ in range(num_entries):
        entry = [
            fake.name(),
            fake.address().replace('\n', ', '),
            fake.email(),
            fake.phone_number(),
            fake.job(),
            fake.company(),
            fake.date_of_birth().isoformat(),
            fake.credit_card_number(),
            fake.credit_card_provider(),
            fake.credit_card_expire(),
            fake.ssn()
        ]
        data.append(entry)
    return data

# Number of fake entries you want to generate
num_entries = 100

# Generate the fake data
fake_data = generate_fake_data(num_entries)

# Write the data to a CSV file
with open('GenerativeAI/Data/fakecsvdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Address', 'Email', 'Phone Number', 'Job', 'Company', 'Birthdate', 'Credit Card Number', 'Credit Card Provider', 'Credit Card Expiration', 'SSN'])
    writer.writerows(fake_data)

print(f"{num_entries} fake entries have been generated and written to fakecsvdata.csv")