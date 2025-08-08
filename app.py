
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ThrivvMart Dashboard", layout="wide")

st.sidebar.title("ThrivvMart Navigation")
page = st.sidebar.radio("Go to", ["Home", "Budgeting & Forecasting", "AI Assistant"])

# Load mock data
@st.cache_data
def load_data():
    account_data = pd.read_csv("data/account_balances.csv")
    payables_data = pd.read_csv("data/payables.csv")
    receivables_data = pd.read_csv("data/receivables.csv")
    return account_data, payables_data, receivables_data

account_data, payables_data, receivables_data = load_data()

# --- Pages ---
if page == "Home":
    st.title("🏪 ThrivvMart Overview")
    st.metric("Total Balance", f"AED {account_data['balance'].sum():,.2f}")
    st.subheader("📋 Account Balances")
    st.dataframe(account_data)
    st.subheader("⚠️ Alerts")
    st.warning("2 invoices overdue | Expenses spiked 30% last week")
    st.button("Ask AI Why?")

elif page == "Budgeting & Forecasting":
    st.title("📊 Budgeting & Forecasting")
    st.dataframe(payables_data)
    st.dataframe(receivables_data)
    st.info("Download forecast report (Coming soon)")

elif page == "AI Assistant":
    st.title("🤖 AI Financial Assistant")
    st.text_input("Ask a question:", placeholder="e.g. Why did infra costs spike last week?")
    st.markdown("💡 Try asking:\n- What's my cash position?\n- Show vendor trend\n- Why did profit fall?")
