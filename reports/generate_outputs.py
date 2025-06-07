import pandas as pd

def generate_rule_reports(df, summary_dict, output_excel="Rule_Evaluation.xlsx"):
    with pd.ExcelWriter(output_excel, engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, sheet_name='Evaluated Data', index=False)
        pd.DataFrame.from_dict(summary_dict, orient='index').to_excel(writer, sheet_name='Rule Summary')
    print(f"🚦 Rule report saved to: {output_excel}")
