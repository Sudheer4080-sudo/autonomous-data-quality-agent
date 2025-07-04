
import streamlit as st
import pandas as pd
import yaml
import io

st.set_page_config(page_title="Rule Builder", layout="wide")
st.title(" Build Your Data Quality Rules (No-Code YAML Generator)")

uploaded_file = st.file_uploader("Upload a CSV file to begin", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"Uploaded: {uploaded_file.name}")
    columns = df.columns.tolist()

    rule_configs = []

    st.subheader("Define Rules Per Column")
    for col in columns:
        with st.expander(f" Rules for: `{col}`"):
            rules = []
            if st.checkbox(f"{col} must not be null", key=f"{col}_not_null"):
                rules.append("not_null")

            if st.checkbox(f"{col} must be unique", key=f"{col}_unique"):
                rules.append("unique")

            if st.checkbox(f"Add numeric range check for {col}", key=f"{col}_range_check"):
                min_val = st.number_input(f"Min value for {col}", key=f"{col}_min")
                max_val = st.number_input(f"Max value for {col}", key=f"{col}_max")
                rules.append({
                    "range": {
                        "min": float(min_val),
                        "max": float(max_val)
                    }
                })

            if st.checkbox(f"Add pattern (regex) check for {col}", key=f"{col}_regex_check"):
                regex = st.text_input(f"Regex pattern for {col}", key=f"{col}_regex")
                rules.append({"pattern": regex})

            if rules:
                rule_configs.append({"column": col, "rules": rules})

    if rule_configs:
        final_yaml = {"rules": rule_configs}
        yaml_str = yaml.dump(final_yaml, sort_keys=False)
        st.subheader("📝 Generated YAML Configuration")
        st.code(yaml_str, language="yaml")

        st.download_button(
            label="Download YAML",
            data=yaml_str,
            file_name="generated_rules.yaml",
            mime="text/yaml"
        )
    else:
        st.info("Define at least one rule to generate YAML.")
