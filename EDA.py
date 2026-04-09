# Import Required Pakages
import streamlit as st
import numpy as np
import pandas as pd
# Title and Description
st.title("🔍 Descriptive Analyzer for Numerical and Categorical Data")
st.text("This application will explore and analyze to understand the dataset. Analyzes both categorical columns and numerical columns.")
st.text("It identifies any missing values, view statistical measures and provide an pverview of you data structure")
st.text("This will help you draw better and accurate obervation for you data.")
st.text("🚀 Upload your dataset and start exploring instantly!")
# Uploading of CSV file
file_upload = st.file_uploader("Upload your CSV file (.csv):", type=["csv"])

# Step 1: Load and store df
if file_upload is not None:
    st.session_state.df = pd.read_csv(file_upload)

# Step 2: Use df safely
if "df" in st.session_state:
    df = st.session_state.df

    # ✅ FIRST create
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    # ✅ THEN store
    st.session_state.num_cols = num_cols
    st.session_state.cat_cols = cat_cols

    # ✅ THEN use
    st.write("Numerical Columns:", list(num_cols))
    st.write("Categorical Columns:", list(cat_cols))
    st.session_state.num_cols=num_cols

    # Displaying the columns top perform statistical measures
    select_num_col=st.selectbox(
        "Select the Numerical Column:",
        st.session_state.num_cols
    )
    select_cat_col=st.selectbox(
        "Select the Categorical Column:",
        st.session_state.cat_cols
    )
    # Numerical Selectbox _ Stats
    st.subheader("Numerical Analysis")
    #Performing the statistical measures on numerical data:
    if select_num_col:
        if st.button("Analyze Numerical Column"):
            col_data=df[select_num_col]
            # Checking if the column is a Null value column
            if col_data.empty:
                st.write("Non Non-Null values to perform statistical measures.")
                st.write("Please select another column to perform statistical measure")
            else:
                st.write("Count:",df[select_num_col].count())
                st.write("Maximum:",df[select_num_col].max())
                st.write("Minimum:",df[select_num_col].min())
                st.write("Mean:",df[select_num_col].mean())
                st.write("Median:",df[select_num_col].median())
                st.write("Variance:",df[select_num_col].var())
                st.write("Standard Deviation:",df[select_num_col].std())
            st.write(f"🎉 Numerical Statistical Measure for {select_num_col} completed!")

    # Categorical Analysis + Stats
    st.subheader("Categorical Analysis")
    # Performing the statistical measures on categorical data:
    if select_cat_col:
        if st.button("Analyze Cateorical Column"):
            col_data=df[select_cat_col]
            # Checking if the categorical column is Null value column
            if col_data.empty:
                st.write("Non Non-Null values to perform statistical measures.")
                st.write("Please select another column to perform statistical measure")
            else:
                st.write("Count:",df[select_cat_col].count())
                st.write("Number of Unique Values:",df[select_cat_col].nunique())
                st.write("Unique Values:",df[select_cat_col].unique())
                st.write("Value Count:",df[select_cat_col].value_counts())
                st.write("Mode:",df[select_cat_col].mode())
            st.write(f"🎉 Categorical Statistical Measure for {select_cat_col} completed!")

else:
    st.info("Please upload a CSV file to continue")
