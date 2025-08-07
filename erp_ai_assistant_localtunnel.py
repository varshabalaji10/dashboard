
import streamlit as st
import pandas as pd

# Load ERP data
accounts = pd.read_csv("accounts.csv")
invoices = pd.read_csv("invoices.csv")
bills = pd.read_csv("bills.csv")
budget = pd.read_csv("budget.csv")

# Page navigation
st.sidebar.title("ERP AI Assistant")
page = st.sidebar.radio("Go to", ["Home", "Budgeting", "AI Assistant"])

# Home Page
if page == "Home":
    st.title("🏠 Financial Overview Dashboard")

    st.header("🏦 Account Balances")
    st.dataframe(accounts)

    st.header("🧾 Accounts Payable & Receivable Summary")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Payables")
        st.dataframe(bills)

    with col2:
        st.subheader("Receivables")
        st.dataframe(invoices)

    st.header("🚨 Alerts")
    overdue_invoices = invoices[invoices['status'] == 'overdue']
    overdue_bills = bills[bills['status'] == 'overdue']
    st.warning(f"{len(overdue_invoices)} overdue invoices found")
    st.warning(f"{len(overdue_bills)} overdue bills found")

    st.header("🧠 AI Insights")
    st.info("💡 Consider paying Vendor ABC early to save AED 200.")
    st.info("📈 Marketing spend is trending 18% above average.")

# Budgeting Page
elif page == "Budgeting":
    st.title("📊 Budgeting & Forecasting")

    st.subheader("Budget vs Actuals")
    st.dataframe(budget)

    st.subheader("Cash Flow Forecast (Mock)")
    st.line_chart({
        "Inflow": [210000, 185000, 175000],
        "Outflow": [180000, 190000, 203000]
    })

# AI Assistant Page
elif page == "AI Assistant":
    st.title("🤖 AI Financial Assistant")

    st.markdown("Ask financial questions like:")
    st.markdown("- What’s my cash balance?")
    st.markdown("- Why did profit fall last month?")
    st.markdown("- Which invoices are overdue?")
    st.markdown("---")

    user_input = st.text_input("💬 Your Question")

    if user_input:
        if "cash balance" in user_input.lower():
            total_balance = accounts['balance'].sum()
            st.success(f"💰 You currently have AED {total_balance:,.0f} across all accounts.")
        elif "profit" in user_input.lower():
            st.success("📉 Your profit dropped by AED 17,000 in July due to increased infra costs and delayed receivables.")
        elif "vendor payment trend" in user_input.lower():
            st.success("📈 Vendor ABC payments: May - AED 8K, Jun - AED 12K, Jul - AED 15K (increasing trend).")
        elif "overdue bills" in user_input.lower():
            overdue = bills[bills['status'] == 'overdue']
            st.success(f"🧾 You have {len(overdue)} overdue bills totaling AED {overdue['amount'].sum():,.0f}.")
        else:
            st.info("🤖 This is a demo. Try asking about cash balance, profit, or overdue bills.")
