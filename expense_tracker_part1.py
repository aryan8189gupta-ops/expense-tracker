import streamlit as st
import pandas as pd
from datetime import date
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Expense Tracker")
st.write("Track your daily expenses easily.")

# -----------------------------
# File Name
# -----------------------------
FILE_NAME = "expenses.csv"


# -----------------------------
# Load Existing Expenses
# -----------------------------
if os.path.exists(FILE_NAME):
    df = pd.read_csv(FILE_NAME)
else:
    df = pd.DataFrame(
        columns=["Date", "Category", "Description", "Amount"]
    )


# -----------------------------
# Add Expense
# -----------------------------
st.header("➕ Add Expense")

col1, col2 = st.columns(2)

with col1:
    expense_date = st.date_input(
        "Date",
        date.today()
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Education",
            "Entertainment",
            "Other"
        ]
    )

with col2:
    description = st.text_input(
        "Description",
        placeholder="e.g. Lunch at college"
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=10.0
    )


# -----------------------------
# Add Button
# -----------------------------
if st.button("Add Expense"):

    if amount <= 0:
        st.error("Please enter an amount greater than 0.")

    else:
        new_expense = pd.DataFrame({
            "Date": [expense_date],
            "Category": [category],
            "Description": [description],
            "Amount": [amount]
        })

        df = pd.concat(
            [df, new_expense],
            ignore_index=True
        )

        df.to_csv(FILE_NAME, index=False)

        st.success("Expense added successfully! 🎉")


# -----------------------------
# Expense Summary
# -----------------------------
st.header("📊 Expense Summary")

if len(df) > 0:

    total_expense = df["Amount"].sum()
    average_expense = df["Amount"].mean()
    highest_expense = df["Amount"].max()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Expense",
        f"₹{total_expense:,.2f}"
    )

    col2.metric(
        "Average Expense",
        f"₹{average_expense:,.2f}"
    )

    col3.metric(
        "Highest Expense",
        f"₹{highest_expense:,.2f}"
    )

else:
    st.info("No expenses added yet.")


# -----------------------------
# Display Expenses
# -----------------------------
st.header("📋 All Expenses")

if len(df) > 0:

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("Your expense table is empty.")


# -----------------------------
# Category-wise Expenses
# -----------------------------
if len(df) > 0:

    st.header("📈 Category-wise Expenses")

    category_expenses = df.groupby(
        "Category"
    )["Amount"].sum()

    st.bar_chart(category_expenses)


# -----------------------------
# Download CSV
# -----------------------------
if len(df) > 0:

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Expenses",
        data=csv,
        file_name="expenses.csv",
        mime="text/csv"
    )