# main.py

import argparse
import logging
import sys
from eda_traffic import load_clean_data
from rules.traffic_rules import apply_rules
from reports.generate_outputs import generate_rule_reports

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def parse_args():
    parser = argparse.ArgumentParser(description="Run traffic rule analysis pipeline.")
    parser.add_argument('--path', type=str, default="C:/Users/2024/Desktop/data.xlsx",
                        help="Path to the Excel file containing traffic data.")
    parser.add_argument('--sheet', type=str, default="Sheet1",
                        help="Name of the Excel sheet to read.")
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        logging.info("🔄 Starting traffic rule analysis pipeline...")

        # 1. Load clean dataset
        logging.info(f"📂 Loading data from {args.path} (sheet: {args.sheet})...")
        df = load_clean_data(args.path, sheet=args.sheet)
        logging.info("✅ Data loaded successfully.")

        # 2. Apply traffic rules
        logging.info("🚦 Applying traffic rules...")
        df_with_flags, rule_summary = apply_rules(df)
        logging.info("✅ Traffic rules applied.")

        # 3. Generate reports
        logging.info("📊 Generating report...")
        generate_rule_reports(df_with_flags, rule_summary)
        logging.info("✅ Report generated.")

    except Exception as e:
        logging.error(f"❌ An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
