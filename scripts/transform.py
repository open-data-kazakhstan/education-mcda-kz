import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

# Load the data with ';' delimiter
file_path = 'data.csv'
data = pd.read_csv(file_path, delimiter=';')

# Define functions for transformations and normalization

def convert_to_float(column):
    if column.dtype == 'object':
        return column.str.replace(',', '.').astype(float)
    else:
        return column  # If already numeric, return as is

def min_max_scale(column):
    scaler = MinMaxScaler()
    return scaler.fit_transform(column.values.reshape(-1, 1))

def z_score_standardize(column):
    scaler = StandardScaler()
    return scaler.fit_transform(column.values.reshape(-1, 1))

def log_transform(column):
    return np.log1p(column)

def percentage_to_ratio(column):
    if column.dtype == 'object':
        return column.str.replace(',', '.').str.replace('%', '').astype(float) / 100
    else:
        return column / 100

# Convert columns with commas to floats if necessary
data['Internal Expenditures on R&D'] = convert_to_float(data['Internal Expenditures on R&D'])
data['External Expenditures on R&D'] = convert_to_float(data['External Expenditures on R&D'])
data['Current Revenues'] = convert_to_float(data['Current Revenues'])
data['Current Expenditures'] = convert_to_float(data['Current Expenditures'])

# Log transform first, then apply Min-Max Scaling for large-magnitude columns
data['Internal Expenditures on R&D'] = min_max_scale(log_transform(data[['Internal Expenditures on R&D']]))
data['External Expenditures on R&D'] = min_max_scale(log_transform(data[['External Expenditures on R&D']]))
data['Current Revenues'] = min_max_scale(log_transform(data[['Current Revenues']]))
data['Current Expenditures'] = min_max_scale(log_transform(data[['Current Expenditures']]))

# Apply Min-Max Scaling for student population as well
data['Number of Students'] = min_max_scale(data[['Number of Students']])

# Convert Innovation Activity Level and Student Seat Availability to ratios
data['Innovation Activity Level, %'] = percentage_to_ratio(data['Innovation Activity Level, %'])
data['Student Seat Availability'] = percentage_to_ratio(data['Student Seat Availability'])

# Z-score standardize Innovation Activity Level and Student Seat Availability
data['Innovation Activity Level, %'] = z_score_standardize(data[['Innovation Activity Level, %']])
data['Student Seat Availability'] = z_score_standardize(data[['Student Seat Availability']])

# Educational Resources Matrix
educational_resources_matrix = np.array([
    [1, 3, 5],
    [1/3, 1, 3],
    [1/5, 1/3, 1]
])

# Investments and Innovation Matrix
investments_innovation_matrix = np.array([
    [1, 2, 2],
    [1/2, 1, 1],
    [1/2, 1, 1]
])

# Financial Stability Matrix
financial_stability_matrix = np.array([
    [1, 2],
    [1/2, 1]
])

# Environmental Factor - single criterion, so the weight is trivially 1

# Function to calculate priority weights using the Eigenvector method
def calculate_priority_weights(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    principal_eigenvector = np.real(eigenvectors[:, np.argmax(eigenvalues)])
    priority_weights = principal_eigenvector / principal_eigenvector.sum()
    return priority_weights

# Calculate weights for each criterion group
weights_educational_resources = calculate_priority_weights(educational_resources_matrix)
weights_investments_innovation = calculate_priority_weights(investments_innovation_matrix)
weights_financial_stability = calculate_priority_weights(financial_stability_matrix)

# Assign calculated weights to criteria
criteria_weights = {
    'Teachers': weights_educational_resources[0],
    'Institutions': weights_educational_resources[1],
    'Student Seat Availability': weights_educational_resources[2],
    'Innovation Activity Level, %': weights_investments_innovation[0],
    'Internal Expenditures on R&D': weights_investments_innovation[1],
    'External Expenditures on R&D': weights_investments_innovation[2],
    'Current Revenues': weights_financial_stability[0],
    'Current Expenditures': weights_financial_stability[1],
    'Number of Students': 1.0  # Environmental factor with a weight of 1
}

# Calculate the score for each region based on the criteria weights
data['Score'] = data.apply(lambda row: sum(row[criterion] * weight for criterion, weight in criteria_weights.items()), axis=1)

# remove The Republic of Kazakhstan from the data, recalculate the scores
data = data[data['Region/City'] != 'The Republic of Kazakhstan']

# Normalize the teachers column with Min-Max Scaling
data['Teachers'] = min_max_scale(data[['Teachers']])
data['Institutions'] = min_max_scale(data[['Institutions']])

data['Score'] = data.apply(lambda row: sum(row[criterion] * weight for criterion, weight in criteria_weights.items()), axis=1)

# Saving
data.to_csv('data_normalized.csv', index=False)