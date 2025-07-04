
import streamlit as st
import pandas as pd
import yaml
from dq_agent.core import apply_rules

st.set_page_config(page_title="Autonomous Data Quality Agent", layout="wide")
st.title("Autonomous Data Quality App")

tab1, tab2 = st.tabs(["Rule Builder", "Run Data Quality"])

# -------- Tab 1: Rule Builder -------- #
with tab1:
    st.header("Step 1: Build Data Quality Rules (YAML)")
    uploaded_file = st.file_uploader("Upload CSV file", type="csv", key="builder_csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success(f"Uploaded: {uploaded_file.name}")
        columns = df.columns.tolist()

        rule_configs = []

        for col in columns:
            with st.expander(f"Rules for: `{col}`"):
                rules = []
                if st.checkbox(f"{col} must not be null", key=f"{col}_not_null"):
                    rules.append("not_null")
                if st.checkbox(f"{col} must be unique", key=f"{col}_unique"):
                    rules.append("unique")
                if st.checkbox(f"Range check for {col}", key=f"{col}_range"):
                    min_val = st.number_input(f"Min {col}", key=f"{col}_min")
                    max_val = st.number_input(f"Max {col}", key=f"{col}_max")
                    rules.append({"range": {"min": float(min_val), "max": float(max_val)}})
                if st.checkbox(f"Regex check for {col}", key=f"{col}_regex"):
                    regex = st.text_input(f"Regex for {col}", key=f"{col}_regex_input")
                    rules.append({"pattern": regex})
                if rules:
                    rule_configs.append({"column": col, "rules": rules})

        if rule_configs:
            yaml_obj = {"rules": rule_configs}
            yaml_str = yaml.dump(yaml_obj, sort_keys=False)
            st.subheader("Generated YAML:")
            st.code(yaml_str, language="yaml")
            st.download_button("Download YAML", data=yaml_str, file_name="rules.yaml", mime="text/yaml")
        else:
            st.info("Add at least one rule to generate YAML.")

# -------- Tab 2: Apply Rules -------- #
with tab2:
    st.header("Step 2: Apply Rules on Data")
    uploaded_csv = st.file_uploader("Upload CSV file", type="csv", key="dq_csv")
    uploaded_yaml = st.file_uploader("Upload YAML config", type=["yaml", "yml"])

    if uploaded_csv and uploaded_yaml:
        df = pd.read_csv(uploaded_csv)
        config = yaml.safe_load(uploaded_yaml)
        issues = apply_rules(df, config)

        if issues:
            st.warning("Issues found:")
            for issue in issues:
                st.markdown(f"- **{issue['rule']}**: {len(issue['rows'])} rows")
        else:
            st.success("No data quality issues found!")
