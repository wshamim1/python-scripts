import pandas as pd
from faker import Faker
import pyarrow as pa
import pyarrow.parquet as pq

# Initialize the Faker object
fake = Faker()

# Function to generate fake data
def generate_fake_data(num_entries=1000):
    data = {
        "name": [fake.name() for _ in range(num_entries)],
        "address": [fake.address().replace('\n', ', ') for _ in range(num_entries)],
        "email": [fake.email() for _ in range(num_entries)],
        "phone_number": [fake.phone_number() for _ in range(num_entries)],
        "job": [fake.job() for _ in range(num_entries)],
        "company": [fake.company() for _ in range(num_entries)],
        "birthdate": [fake.date_of_birth().isoformat() for _ in range(num_entries)],
        "credit_card_number": [fake.credit_card_number() for _ in range(num_entries)],
        "credit_card_provider": [fake.credit_card_provider() for _ in range(num_entries)],
        "credit_card_expiration": [fake.credit_card_expire() for _ in range(num_entries)],
        "ssn": [fake.ssn() for _ in range(num_entries)]
    }
    return pd.DataFrame(data)

# Number of fake entries you want to generate
num_entries = 100

# Generate the fake data
df = generate_fake_data(num_entries)

# Convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# Write the PyArrow Table to a Parquet file
pq.write_table(table, 'fake_data.parquet')

print(f"{num_entries} fake entries have been generated and written to fake_data.parquet")

# Optional: Read back the Parquet file to verify
read_df = pq.read_table('fake_data.parquet').to_pandas()
print(read_df.head())
print(f"Shape of the read data: {read_df.shape}")