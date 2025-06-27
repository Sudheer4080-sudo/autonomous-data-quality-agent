# autonomous-data-quality-agent
Cloud-ready, ML-powered data quality agent using rule-based and anomaly detection techniques across industries.
---

## 🗃️ Database Integration (NEW)

This agent now supports reading and writing directly from third-party databases using **SQLAlchemy**, including:

- PostgreSQL
- MySQL
- SQL Server
- SQLite
- Oracle
- Cloud-hosted DBs (e.g., Amazon RDS, Aurora)

### Example Usage
```python
from db_connector import connect_db, read_table, write_table

engine = connect_db(
    db_type="postgresql",
    username="your_user",
    password="your_pass",
    host="localhost",
    port="5432",
    dbname="your_db"
)

df = read_table(engine, "raw_transactions")
df_cleaned = ...  # process with your agent
write_table(df_cleaned, engine, "cleaned_transactions")

## 🚀 Installation

```bash
pip install autonomous-dq-agent


# 🤖 Autonomous Data Quality Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://autonomous-data-quality-agent-lejzddggm8vetbvnwpcmj.streamlit.app)

A Python-based agent that automatically applies industry-specific data quality rules to any dataset. Upload CSVs, apply YAML configs, detect issues — all from a no-code UI.

## 🔗 Live Demo

👉 [Click to Launch the Web App](https://autonomous-data-quality-agent-lejzddggm8vetbvnwpcmj.streamlit.app)

