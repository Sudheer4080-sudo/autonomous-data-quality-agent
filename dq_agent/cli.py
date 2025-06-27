import argparse
import pandas as pd
import yaml
from dq_agent.db_connector import connect_db, read_table, write_table

def apply_rules(df, config):
    issues = []
    for rule in config.get("rules", []):
        try:
            result = df.query(rule["condition"])
            if not result.empty:
                issues.append((rule["name"], result))
        except Exception as e:
            print(f"Error evaluating rule '{rule['name']}': {e}")
    return issues

def main():
    parser = argparse.ArgumentParser(description="Run the Autonomous Data Quality Agent")
    parser.add_argument("--input", type=str, required=True, help="Path to CSV input file")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
    args = parser.parse_args()

    # Load data and config
    df = pd.read_csv(args.input)
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    print("🔍 Running rules...")
    issues = apply_rules(df, config)

    if not issues:
        print("No issues found.")
    else:
        for rule_name, issue_df in issues:
            print(f"⚠️ Rule triggered: {rule_name}")
            print(issue_df)

if __name__ == "__main__":
    main()