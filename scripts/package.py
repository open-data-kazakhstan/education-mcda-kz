from datapackage import Package
import os

# Define the relative base path to the data directory from the scripts folder
base_path = os.path.join('..', 'data')

# Create the package using the relative base path
package = Package(base_path=base_path)

# Infer metadata from 'data_norm.csv' located in the data folder
package.infer('data_norm.csv')

# Save the `datapackage.json` in the `education_kz` folder (one level up from scripts)
package.save(os.path.join('..', 'datapackage.json'))