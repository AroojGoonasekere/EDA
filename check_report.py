import pandas as pd


# Path to the generated Excel report

file_path = "Rule_Evaluation.xlsx"  # Adjust the path if necessary


# Load the evaluated data

df_evaluated = pd.read_excel(file_path, sheet_name='Evaluated Data')

print("Evaluated Data:")

print(df_evaluated)


# Load the summary data

df_summary = pd.read_excel(file_path, sheet_name='Rule Summary')

print("\nRule Summary:")

print(df_summary)