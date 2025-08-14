import pandas as pd
import matplotlib.pyplot as plt

# Expanded k-anonymized dataset (maintaining k=2 anonymity)
k_anon_dataset = [
    # Group 1: 30-39, M, 123, Medium (2 records)
    {"age_group": "30-39", "gender": "M", "zipcode_prefix": "123", "income_level": "Medium", "diagnosis": "Diabetes"},
    {"age_group": "30-39", "gender": "M", "zipcode_prefix": "123", "income_level": "Medium", "diagnosis": "Flu"},

    # Group 2: 30-39, M, 678, Medium (2 records)
    {"age_group": "30-39", "gender": "M", "zipcode_prefix": "678", "income_level": "Medium", "diagnosis": "Hypertension"},
    {"age_group": "30-39", "gender": "M", "zipcode_prefix": "678", "income_level": "Medium", "diagnosis": "Asthma"},

    # Group 3: 20-29, F, 678, Medium (2 records)
    {"age_group": "20-29", "gender": "F", "zipcode_prefix": "678", "income_level": "Medium", "diagnosis": "Cold"},
    {"age_group": "20-29", "gender": "F", "zipcode_prefix": "678", "income_level": "Medium", "diagnosis": "Allergy"},

    # Group 4: 40-49, F, 123, High (2 records)
    {"age_group": "40-49", "gender": "F", "zipcode_prefix": "123", "income_level": "High", "diagnosis": "Migraine"},
    {"age_group": "40-49", "gender": "F", "zipcode_prefix": "123", "income_level": "High", "diagnosis": "Arthritis"},

    # Group 5: 50-59, M, 456, High (2 records)
    {"age_group": "50-59", "gender": "M", "zipcode_prefix": "456", "income_level": "High", "diagnosis": "Heart Disease"},
    {"age_group": "50-59", "gender": "M", "zipcode_prefix": "456", "income_level": "High", "diagnosis": "Diabetes"},

    # Group 6: 30-39, F, 123, Low (2 records)
    {"age_group": "30-39", "gender": "F", "zipcode_prefix": "123", "income_level": "Low", "diagnosis": "Anxiety"},
    {"age_group": "30-39", "gender": "F", "zipcode_prefix": "123", "income_level": "Low", "diagnosis": "Depression"},

    # Non-matching noise records added here
    {"age_group": "60-780", "gender": "M", "zipcode_prefix": "999", "income_level": "Medium", "diagnosis": "Stroke"},
    {"age_group": "20-29", "gender": "F", "zipcode_prefix": "121", "income_level": "High", "diagnosis": "Fatigue"},
    {"age_group": "40-49", "gender": "M", "zipcode_prefix": "224", "income_level": "Low", "diagnosis": "Back Pain"}
]

# Expanded auxiliary dataset (with potential matches)
auxiliary_dataset = [
    # Matches for Group 1: 30-39, M, 123, Medium
    {"name": "John Smith", "age": 34, "gender": "M", "zipcode": 12346, "income": 52000},
    {"name": "Alex Wilson", "age": 33, "gender": "M", "zipcode": 12348, "income": 47000},

    # Matches for Group 2: 30-39, M, 678, Medium
    {"name": "Mike Johnson", "age": 35, "gender": "M", "zipcode": 67890, "income": 49000},
    {"name": "David Brown", "age": 32, "gender": "M", "zipcode": 67891, "income": 55000},

    # Matches for Group 3: 20-29, F, 678, Medium
    {"name": "Sarah Davis", "age": 28, "gender": "F", "zipcode": 67845, "income": 50000},
    {"name": "Lisa Anderson", "age": 26, "gender": "F", "zipcode": 67892, "income": 48000},

    # Matches for Group 4: 40-49, F, 123, High
    {"name": "Emily Clark", "age": 45, "gender": "F", "zipcode": 12321, "income": 72000},
    {"name": "Jennifer White", "age": 42, "gender": "F", "zipcode": 12347, "income": 68000},

    # Matches for Group 5: 50-59, M, 456, High
    {"name": "Robert Lee", "age": 52, "gender": "M", "zipcode": 45699, "income": 78000},
    {"name": "Mark Thompson", "age": 55, "gender": "M", "zipcode": 45622, "income": 82000},

    # Matches for Group 6: 30-39, F, 123, Low
    {"name": "Maria Garcia", "age": 31, "gender": "F", "zipcode": 12345, "income": 38000},
    {"name": "Amanda Rodriguez", "age": 36, "gender": "F", "zipcode": 12349, "income": 42000},

    # Non-matching records (noise)
    {"name": "William Johnson", "age": 62, "gender": "M", "zipcode": 99999, "income": 95000},
    {"name": "Patricia Williams", "age": 29, "gender": "F", "zipcode": 11111, "income": 85000},
    {"name": "Christopher Brown", "age": 41, "gender": "M", "zipcode": 22222, "income": 35000}
]

# Generalization functions
def generalize_age(age):
    if 20 <= age <= 29: return "20-29"
    elif 30 <= age <= 39: return "30-39"
    elif 40 <= age <= 49: return "40-49"
    elif 50 <= age <= 59: return "50-59"
    else: return "60+"

def generalize_zipcode(zipcode):
    return str(zipcode)[:3]

def generalize_income(income):
    if income < 45000: return "Low"
    elif income < 65000: return "Medium"
    else: return "High"

# Convert to DataFrames
k_anon_df = pd.DataFrame(k_anon_dataset)
aux_df = pd.DataFrame(auxiliary_dataset)

# Generalize auxiliary dataset
aux_df['age_group'] = aux_df['age'].apply(generalize_age)
aux_df['zipcode_prefix'] = aux_df['zipcode'].apply(generalize_zipcode)
aux_df['income_level'] = aux_df['income'].apply(generalize_income)

# Add record IDs
k_anon_df = k_anon_df.reset_index().rename(columns={'index': 'record_id'})

# Quasi-identifiers for linking
qi_cols = ['age_group', 'gender', 'zipcode_prefix', 'income_level']

# Perform linkage attack
linkage_results = pd.merge(k_anon_df, aux_df[['name'] + qi_cols], on=qi_cols, how='inner')

# Calculate metrics
total_records = len(k_anon_df)
linked_records = linkage_results['record_id'].nunique()
risk = linked_records / total_records

print(f"Total k-anonymized records: {total_records}")
print(f"Records with matches: {linked_records}")
print(f"Re-identification risk: {risk:.3f}")
print(f"Total potential matches: {len(linkage_results)}")

print("\nLinkage results:")
print(linkage_results[['record_id', 'diagnosis', 'name']].sort_values('record_id'))

# Ambiguity analysis
print("\nAmbiguity per record:")
ambiguity = linkage_results.groupby('record_id').agg({
    'name': lambda x: list(x),
    'diagnosis': 'first'
})
for record_id, row in ambiguity.iterrows():
    names = ", ".join(row['name'])
    print(f"Record {record_id} ({row['diagnosis']}): Could be {names}")

# Group-level analysis
print(f"\nGroup-level k-anonymity verification:")
group_counts = k_anon_df.groupby(qi_cols).size().reset_index(name='count')
print(group_counts)
print(f"All groups have k>=2: {all(group_counts['count'] >= 2)}")

# Plotting re-identification risk
plt.bar(["Re-identified", "Not re-identified"],
            [linked_records, total_records - linked_records],
            color=["red", "green"])
plt.ylabel("Number of records")
plt.title("Linkage attack on k-anonymized dataset")
plt.show()
