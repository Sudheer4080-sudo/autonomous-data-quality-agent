import streamlit as st
import pandas as pd
import yaml
from dq_agent.cli import apply_rules

st.set_page_config(page_title="Autonomous DQ Agent", layout="wide")
st.title("🤖 Autonomous Data Quality Agent")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
config_file = st.file_uploader("Upload a YAML config", type=["yaml", "yml"])

if uploaded_file and config_file:
    df = pd.read_csv(uploaded_file)
    config = yaml.safe_load(config_file)

    st.subheader("📊 Input Data")
    st.dataframe(df)

    if st.button("Run DQ Agent"):
        with st.spinner("Analyzing data..."):
            issues = apply_rules(df, config)

        if not issues:
            st.success("✅ No issues found!")
        else:
            for rule_name, issue_df in issues:
                st.warning(f"⚠️ Rule triggered: {rule_name}")
                st.dataframe(issue_df)

            combined_issues = pd.concat([df for _, df in issues])
            csv = combined_issues.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Flagged Rows", csv, "flagged_rows.csv", "text/csv")