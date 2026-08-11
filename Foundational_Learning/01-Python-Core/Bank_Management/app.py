import streamlit as st
from mainimprovised import Bank

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Management System")
st.caption("Python OOP + JSON + Streamlit")
st.sidebar.title("Banking Operations")

choice = st.sidebar.selectbox(
    "Choose an operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)
if choice == "Create Account":
    st.header("🆕 Create Account")
    name = st.text_input("Name")
    age = st.number_input("Age",min_value=1,max_value=120,step=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN",type="password")
    if st.button("Create Account"):
        success, result = Bank.create_account(name,age,email,pin)
        if success:
            st.success("Account created successfully!")
            st.info(f"Your Account Number: **{result}**")
            st.warning("Please save your account number.")
        else:
            st.error(result)

elif choice == "Deposit Money":
    st.header("💰 Deposit Money")
    account_number = st.text_input("Account Number")
    pin = st.text_input("PIN",type="password")
    amount = st.number_input("Amount",min_value=0,step=100)
    if st.button("Deposit Money"):
        success, message = Bank.deposit_money(account_number,pin,amount)
        if success:
            st.success(message)
        else:
            st.error(message)

elif choice == "Withdraw Money":
    st.header("💸 Withdraw Money")
    account_number = st.text_input("Account Number")
    pin = st.text_input("PIN",type="password")
    amount = st.number_input("Amount",min_value=0,step=100)
    if st.button("Withdraw Money"):
        success, message = Bank.withdraw_money(account_number,pin,amount)
        if success:
            st.success(message)
        else:
            st.error(message)

elif choice == "Show Details":
    st.header("👤 Account Details")
    account_number = st.text_input("Account Number")
    pin = st.text_input("PIN",type="password")
    
    if st.button("Show Details"):
        account = Bank.show_details(account_number,pin)
        if account:
            st.success("Account found!")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Name**")
                st.write(account["name"])
                st.write("**Age**")
                st.write(account["age"])
                st.write("**Email**")
                st.write(account["email"])
            with col2:
                st.write("**Account Number**")
                st.write(account["accountNo."])
                st.write("**Balance**")
                st.write(f"₹{account['balance']:,.2f}")
        else:
            st.error("Invalid account number or PIN.")

elif choice == "Update Details":
    st.header("✏️ Update Details")
    account_number = st.text_input("Account Number")
    pin = st.text_input("Current PIN",type="password")
    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN",type="password")
    st.caption("Leave a field empty if you don't want to change it.")
    if st.button("Update Details"):
        success, message = Bank.update_details(account_number,pin,new_name,new_email,new_pin)
        if success:
            st.success(message)
        else:
            st.error(message)

elif choice == "Delete Account":
    st.header("🗑️ Delete Account")
    account_number = st.text_input("Account Number")
    pin = st.text_input("PIN",type="password")
    confirmation = st.checkbox("I understand that this action cannot be undone.")
    if st.button("Delete Account"):
        if not confirmation:
            st.warning("Please confirm account deletion.")
        else:
            success, message = Bank.delete_account(account_number,pin)
            if success:
                st.success(message)
            else:
                st.error(message)
