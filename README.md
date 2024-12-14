# Education in Kazakhstan

## Original data

<PlotlyBarChart data={{ url: 'data/data.csv' }} xAxis="Region/City" yAxis="Number of Students" />

<FlatUiTable data={{ url: 'data/data.csv' }} />


## Data Story

The data on the number of students and research expenditures across different regions of Kazakhstan reveal significant disparities in the levels of education and scientific activity. For instance, cities like Almaty and Shymkent, with the highest student populations, also have substantial research funding and higher levels of innovation activity. In contrast, regions like Mangystau, despite having fewer students, allocate significant resources to research and development, indicating a focus on innovation.

The level of innovation activity ranges from 4.7% in West Kazakhstan to 15.2% in North Kazakhstan, reflecting varying degrees of regional involvement in innovative processes. These differences highlight how resource distribution and focus on research can impact the accessibility and quality of education, as well as the development of scientific infrastructure across the country.

## Description

This dataset provides various educational and socio-economic indicators across the regions of Kazakhstan. The main data is stored in `data/data_norm.csv`, with columns covering metrics such as:

- **Internal and External R&D Expenses**: This column includes expenses related to research and development within and outside each region.
- **Innovation Activity Indicators**: Shows regional data on enterprise innovation, providing insights into each region's activity level.
- **Financial Operations in Educational Organizations**: Includes revenue and expenditure data for educational institutions.
- **Preschool Availability**: Indicates the number of children per 100 places in preschool organizations.
- **Technical and Vocational Education Organizations**: Represents the number of such institutions per region.
- **General Education Teachers**: Contains teacher counts in general education schools.

Some data in the dataset has been manually adjusted due to the recent reorganization of regions in Kazakhstan. These adjustments include proportional estimations or synthetic data additions to maintain dataset consistency.

## Installation

To set up this project:

1. Clone the repository:
    ```shell
    git clone https://github.com/open-data-kazakhstan/education-kz.git
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv /path/to/localrepo
    cd /path/to/localrepo
    Scripts/activate  # For Windows users
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Generate or update the `datapackage.json` file:
    ```bash
    python scripts/package.py
    ```

## Data

Data sources for the educational indicators include [Kazakhstan National Bureau of Statistics](https://stat.gov.kz/), containing raw and normalized versions:

- `data/data.csv`: Raw data with various educational indicators for Kazakhstan's regions, using a semicolon (`;`) delimiter.
- `data/data_normalized.csv`: Normalized and cleaned data with adjustments for recent regional changes.
- `archive/innovations.xls`: Source file for innovation activity indicators.
- `archive/research_and_development_works.xls`: R&D expenses by region.
- `archive/revenues_and_expenditures.xls`: Financial data for education institutions, including revenues and expenditures by region.

## Scripts

- **`package.py`**: Generates or updates the `datapackage.json` file, capturing metadata about the dataset for easier sharing and usage.
- **`transform.py`**: Transforms the raw data files from their original format (Excel or other) into the structured CSV format `data_normalized.csv` for analysis.
- **transform.ipynb**: Jupyter notebook version of the `transform.py` script with additional information on choosing weights for the score calculation.

## License

This dataset is available under the Open Data Commons [Public Domain Dedication and License (PDDL)][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/
