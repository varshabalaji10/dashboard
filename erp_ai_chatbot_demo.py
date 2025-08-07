
import streamlit as st
import pandas as pd

# Load ERP data
accounts = pd.read_csv("accounts.csv")
invoices = pd.read_csv("invoices.csv")
bills = pd.read_csv("bills.csv")
budget = pd.read_csv("budget.csv")

# Set page config
st.set_page_config(page_title="ERP AI Assistant", page_icon="🤖", layout="wide")

st.title("🤖 AI Financial Assistant")
st.markdown("Ask anything about your business — your assistant pulls live financial data to help you decide faster.")

st.markdown("### 🔎 Suggested Questions:")
cols = st.columns(3)
with cols[0]:
    if st.button("Why did profit fall last month?"):
        st.session_state.preset = "Why did profit fall last month?"
with cols[1]:
    if st.button("What's my current cash balance?"):
        st.session_state.preset = "What's my current cash balance?"
with cols[2]:
    if st.button("Which invoices are overdue?"):
        st.session_state.preset = "Which invoices are overdue?"

st.markdown("---")

# Chat input box
user_input = st.text_input("💬 Ask a question", value=st.session_state.get("preset", ""))
st.session_state["preset"] = ""  # Clear preset

# Fake responses for demo
if user_input:
    st.markdown(f"**You:** {user_input}")
    st.markdown("**Assistant:**")

    if "cash balance" in user_input.lower():
        total = accounts['balance'].sum()
        st.success(f"💰 You currently have AED {total:,.0f} across all accounts.")
        st.markdown("- Emirates NBD: AED {:,}".format(accounts.iloc[0]['balance']))
        st.markdown("- ADCB: AED {:,}".format(accounts.iloc[1]['balance']))
        st.markdown("- Mashreq: AED {:,}".format(accounts.iloc[2]['balance']))

    elif "profit" in user_input.lower():
        st.error("📉 Your profit dropped by AED 17,000 in July.")
        st.markdown("**Reasons:**")
        st.markdown("- Client XYZ delayed a payment worth AED 12,000.")
        st.markdown("- Infra expenses rose by 25% compared to June.")

    elif "overdue" in user_input.lower() and "invoice" in user_input.lower():
        od = invoices[invoices["status"] == "overdue"]
        st.warning(f"🧾 You have {len(od)} overdue invoices worth AED {od['amount'].sum():,.0f}")
        for i, row in od.iterrows():
            st.markdown(f"- {row['client']}: AED {row['amount']} (Overdue by {row['days_overdue']} days)")

    elif "vendor payment trend" in user_input.lower():
        st.info("📈 Vendor ABC Payments:\n\n- May: AED 8,000\n- June: AED 12,000\n- July: AED 15,000\n\nTrend: Upward")

    else:
        st.markdown("🤔 I'm still learning. Try asking about cash balance, profit, or invoices.")

st.markdown("---")
st.caption("This is a demo assistant powered by static data. A real version would connect to your ERP/CRM.")
