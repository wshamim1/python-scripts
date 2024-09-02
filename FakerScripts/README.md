# Python Scripts Collection

This repository contains a collection of Python scripts for generating various types of fake data using the Faker library. These scripts are useful for creating test data, populating databases, or generating sample datasets for development and testing purposes.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Scripts Overview](#scripts-overview)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Requirements

- Python 3.6+
- Faker library
- pandas (for CSV and Parquet scripts)
- pyarrow (for Parquet script)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/python-scripts.git
   cd python-scripts/FakerScripts
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Scripts Overview

This repository contains the following scripts:

1. `generate_csv_data.py`: Generates fake data and saves it as a CSV file.
2. `generate_parquet_data.py`: Creates fake data and stores it in Parquet format.
3. `generate_xml_data.py`: Produces fake personal data in XML format.
4. `generate_json_data.py`: Generates fake data and saves it as a JSON file.

## Usage

### Generate CSV Data

To generate fake data in CSV format:

```
python GenerateFakeCSVData.py
```

This will create a file named `fake_data.csv` in the current directory.

### Generate Parquet Data

To create fake data in Parquet format:

```
python GenerateFakeParquetData.py
```

This script will produce a file named `fake_data.parquet`.

### Generate XML Data

To generate fake personal data in XML format:

```
python GenerateFakeXMLData.py
```

This will create a file named `fake_people_catalog.xml`.

### Generate JSON Data

To produce fake data in JSON format:

```
python GenerateFakeJsonData.py
```

This script will create a file named `fake_data.json`.

