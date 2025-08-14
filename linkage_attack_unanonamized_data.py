import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# 1. Create toy dataset
# --------------------------
deidentified_data = [
    {"age": 28, "gender": "F", "zipcode": 12345, "diagnosis": "Cold"},
    {"age": 36, "gender": "F", "zipcode": 54323, "diagnosis": "Hypertension"},
    {"age": 28, "gender": "M", "zipcode": 99999, "diagnosis": "Asthma"},
    {"age": 34, "gender": "M", "zipcode": 12345, "diagnosis": "Flu"},
    {"age": 32, "gender": "F", "zipcode": 12340, "diagnosis": "Cold"},
    {"age": 47, "gender": "M", "zipcode": 67841, "diagnosis": "Diabetes"},
    {"age": 35, "gender": "F", "zipcode": 54320, "diagnosis": "Hypertension"},
    {"age": 29, "gender": "M", "zipcode": 99990, "diagnosis": "Asthma"},
    {"age": 45, "gender": "F", "zipcode": 67890, "diagnosis": "Diabetes"}
]

true_ids_data = [
    {"Name": "Alice",   "age": 34, "gender": "F", "zipcode": 54321},
    {"Name": "Bob",     "age": 28, "gender": "M", "zipcode": 99999},
    {"Name": "Charlie", "age": 34, "gender": "M", "zipcode": 12345},
    {"Name": "Diana",   "age": 45, "gender": "F", "zipcode": 67890},
    {"Name": "Eve",     "age": 28, "gender": "F", "zipcode": 12345},
    {"Name": "Frank",   "age": 32, "gender": "F", "zipcode": 12340},
    {"Name": "Grace",   "age": 46, "gender": "M", "zipcode": 67891},
    {"Name": "Helen",   "age": 35, "gender": "F", "zipcode": 54320},
    {"Name": "Ian",     "age": 29, "gender": "M", "zipcode": 99990}
]

# Convert to DataFrames
deid_df = pd.DataFrame(deidentified_data)
true_df = pd.DataFrame(true_ids_data)

# --------------------------
# 2. Function: linkage attack
# --------------------------
def linkage_attack(deid, true, qi_cols, title="Linkage Attack"):
    linked = pd.merge(deid, true, on=qi_cols, suffixes=("_deid", "_true"))
    total_records = len(deid)
    successful_links = len(linked)
    risk = successful_links / total_records if total_records > 0 else 0

    print(f"\n--- {title} ---")
    print(f"Total de-identified records: {total_records}")
    print(f"Successful re-identifications: {successful_links}")
    print(f"Re-identification risk: {risk:.3f}")
    print(linked)

    plt.bar(["Re-identified", "Not re-identified"],
            [successful_links, total_records - successful_links],
            color=["red", "green"])
    plt.ylabel("Number of records")
    plt.title(title)
    plt.show()

# --------------------------
# 3. Show risk BEFORE anonymization
# --------------------------
qi_cols = ["age", "gender", "zipcode"]
linkage_attack(deid_df, true_df, qi_cols, title="Linkage Risk Before Anonymization")


