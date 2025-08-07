
import streamlit as st
import pandas as pd

# Load data
accounts = pd.read_csv("accounts.csv")
invoices = pd.read_csv("invoices.csv")
bills = pd.read_csv("bills.csv")
budget = pd.read_csv("budget.csv")

st.set_page_config(layout="wide", page_title="ERP AI Dashboard", page_icon="📊")

# Sidebar Navigation
st.sidebar.title("📊 ERP Performance Dashboard")
menu = st.sidebar.radio("Navigate", [
    "Dashboard",
    "Anomaly Center",
    "Forecasting & Budgeting",
    "Invoice & Bill Management",
    "AI Financial Assistant",
    "Reports & Export"
])

# SESSION PRESETS for chatbot
if "chat_preset" not in st.session_state:
    st.session_state.chat_preset = ""

# Home Dashboard
if menu == "Dashboard":
    st.title("📊 Financial Overview")

    st.markdown("### Summary Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Cash on Hand", "AED 248,500")
    with col2:
        st.metric("📉 Burn Rate (Monthly)", "AED 53,827", "-7.2%")
    with col3:
        st.metric("📤 Outstanding Invoices", "AED 87,144", "+5 Overdue")

    st.markdown("---")
    st.markdown("### 🔔 Live Alerts")
    alert1 = st.container()
    with alert1:
        st.warning("🚨 3 invoices are overdue for more than 10 days")
        if st.button("🔎 View in Invoice Management", key="alert1"):
            st.experimental_set_query_params(page="Invoice & Bill Management")

    alert2 = st.container()
    with alert2:
        st.warning("📉 Infra cost spiked by 25% last month")
        if st.button("💬 Ask AI Why", key="alert2"):
            st.session_state.chat_preset = "Why did infra cost spike last month?"
            st.experimental_set_query_params(page="AI Financial Assistant")

    st.markdown("---")
    st.markdown("### 🧠 Smart Insights")
    insight = st.container()
    with insight:
        st.success("💡 You can save AED 200 by paying Vendor ABC early")
        if st.button("💬 Ask AI for Vendor Advice", key="insight1"):
            st.session_state.chat_preset = "Should I pay Vendor ABC early?"
            st.experimental_set_query_params(page="AI Financial Assistant")

# Anomaly Center
elif menu == "Anomaly Center":
    st.title("🧪 Anomaly Center")
    st.line_chart({
        "Detected Anomalies": [3, 5, 2, 4, 1, 6]
    })
    st.bar_chart({
        "Categories": [1, 3, 2, 4],
    })

# Forecasting & Budgeting
elif menu == "Forecasting & Budgeting":
    st.title("📈 Forecasting & Budgeting")
    st.bar_chart(budget.set_index("category")[["budgeted", "actual"]])
    st.line_chart({
        "Forecasted Cash": [220000, 210000, 180000, 175000]
    })

# Invoice & Bill Management
elif menu == "Invoice & Bill Management":
    st.title("📤 Invoices & Bills")
    st.markdown("### Accounts Payable")
    st.dataframe(bills)
    st.markdown("### Accounts Receivable")
    st.dataframe(invoices)

# AI Financial Assistant
elif menu == "AI Financial Assistant":
    st.title("🤖 AI Financial Assistant")
    st.markdown("Ask a financial question below:")

    if st.session_state.chat_preset:
        user_input = st.text_input("💬", value=st.session_state.chat_preset)
        st.session_state.chat_preset = ""
    else:
        user_input = st.text_input("💬")

    if user_input:
        st.markdown(f"**You:** {user_input}")
        if "infra cost" in user_input.lower():
            st.markdown("**Assistant:** Infra cost rose by 25% due to cloud subscriptions and vendor upgrades.")
        elif "vendor" in user_input.lower():
            st.markdown("**Assistant:** Paying Vendor ABC early qualifies for a 2% discount. Recommend paying before 10th Aug.")
        else:
            st.markdown("**Assistant:** I'm still learning. Try asking about profit, invoices, or forecast.")

# Reports & Export
elif menu == "Reports & Export":
    st.title("📄 Reports & Export Center")
    st.markdown("Download historical reports or schedule new ones (static view)")
    st.table(pd.DataFrame({
        "Report Name": ["Monthly Summary", "Vendor Spend Q2", "Forecast Q3"],
        "Status": ["Ready", "Processing", "Ready"],
        "Download": ["Download", "In Progress", "Download"]
    }))
