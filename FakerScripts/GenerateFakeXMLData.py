import xml.etree.ElementTree as ET
from xml.dom import minidom
from faker import Faker

# Initialize the Faker object
fake = Faker()

def generate_person():
    """Generate a single person's data with fake information."""
    person = ET.Element("person")
    ET.SubElement(person, "name").text = fake.name()
    ET.SubElement(person, "address").text = fake.address().replace('\n', ', ')
    ET.SubElement(person, "email").text = fake.email()
    ET.SubElement(person, "phone_number").text = fake.phone_number()
    ET.SubElement(person, "job").text = fake.job()
    ET.SubElement(person, "company").text = fake.company()
    ET.SubElement(person, "birthdate").text = fake.date_of_birth().isoformat()
    
    credit_card = ET.SubElement(person, "credit_card")
    ET.SubElement(credit_card, "number").text = fake.credit_card_number()
    ET.SubElement(credit_card, "provider").text = fake.credit_card_provider()
    ET.SubElement(credit_card, "expiration_date").text = fake.credit_card_expire()
    
    ET.SubElement(person, "ssn").text = fake.ssn()
    
    return person

def generate_people_catalog(num_people=10):
    """Generate a catalog with multiple people's data."""
    root = ET.Element("people_catalog")
    
    for _ in range(num_people):
        root.append(generate_person())
    
    return root

def pretty_print_xml(element):
    """Convert XML element to a pretty-printed XML string."""
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Generate the fake XML data
num_people = 20
catalog = generate_people_catalog(num_people)

# Convert to a pretty-printed XML string
xml_string = pretty_print_xml(catalog)

# Write to file
with open('GenerativeAI/Data/fake_people_catalog.xml', 'w', encoding='utf-8') as f:
    f.write(xml_string)

print(f"Generated XML file 'fake_people_catalog.xml' with {num_people} fake personal records.")

# Optionally, print the first few lines of the generated XML
print("\nFirst few lines of the generated XML:")
print('\n'.join(xml_string.split('\n')[:20]))