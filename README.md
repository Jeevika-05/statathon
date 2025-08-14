# README

## Overview
This repository contains three scripts demonstrating **privacy risk analysis** and **privacy-preserving techniques** for datasets.  
The scripts showcase:
1. **Linkage attacks on raw data** (before anonymization)  
2. **Linkage attacks on k-anonymized data**  
3. **Differential Privacy synthetic data generation**  

Each script performs a privacy-related operation, provides metrics, and in some cases, visualizes the results.

---

## **Script 1 – Linkage Attack on De-identified Data**
**Purpose:**  
Demonstrates how a dataset containing quasi-identifiers (like age, gender, and ZIP code) can still be vulnerable to **re-identification** when combined with an auxiliary dataset.  

**Workflow:**  
1. Creates two toy datasets:  
   - **De-identified dataset** – Contains quasi-identifiers and sensitive attributes (like diagnosis).  
   - **True identity dataset** – Contains names along with quasi-identifiers.  
2. Performs a **linkage attack** by matching on quasi-identifiers.  
3. Calculates:  
   - Total number of records.  
   - Number of successful re-identifications.  
   - Re-identification risk percentage.  
4. Displays a bar chart comparing re-identified vs. not re-identified records.

**Graph:**  
[Script 1 Linkage Attack Graph](images/Linkage_risk_before_anonymisation.jpg)

---

## **Script 2 – Linkage Attack on k-Anonymized Data**
**Purpose:**  
Shows that even after **k-anonymization**, a dataset may still have re-identification risks, depending on generalization and auxiliary data availability.  

**Workflow:**  
1. Defines generalization rules for:  
   - Age (into ranges, e.g., 20–29).  
   - ZIP codes (prefix only).  
   - Income (Low, Medium, High).  
2. Applies generalization to the auxiliary dataset.  
3. Performs a **linkage attack** using generalized quasi-identifiers.  
4. Calculates and prints:  
   - Total records.  
   - Records successfully linked.  
   - Re-identification risk.  
   - Ambiguity (number of possible identities per record).  
5. Performs **k-anonymity verification** by checking if all groups have size ≥ k.  
6. Plots a bar chart showing the number of re-identified vs. non-re-identified records.

**Graph:**  
[Script 2 Linkage Attack on K-anonamized data Graph](images/Linkage_attack_on_k-anonymized_dataset.jpg)

---

## **Script 3 – Differential Privacy Synthetic Data Generation**
**Purpose:**  
Implements **Differential Privacy (DP)** via **randomized response** to generate a synthetic version of binary transaction data, reducing privacy risks while retaining statistical utility.  

**Workflow:**  
1. Reads the original transaction dataset from `original_transactions.csv`.  
2. Defines a function to apply randomized response:  
   - Uses a privacy budget parameter (**epsilon**).  
   - Each binary value has a probability `p` of being kept or flipped.  
3. Generates a synthetic dataset using the DP mechanism.  
4. Saves the synthetic dataset to `synthetic_transactions.csv`.  
5. Prints summary statistics for both the original and synthetic datasets.

---

## **Notes**
- The linkage attack scripts (1 & 2) use **Pandas** for data manipulation and **Matplotlib** for visualization.  
- The Differential Privacy script (3) relies on **NumPy** and **randomized response** to protect sensitive binary data.  
