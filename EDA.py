# Import Required Packages
import streamlit as st
import numpy as np
import pandas as pd
# Title and Description
st.title("🔍 Descriptive Analyzer for Numerical and Categorical Data")
st.text("This application will explore and analyze to understand the dataset. Analyzes both categorical columns and numerical columns.")
st.text("It identifies any missing values, view statistical measures and provide an preview of your data structure")
st.text("This will help you draw better and accurate obervation for you data.")
st.text("🚀 Upload your dataset and start exploring instantly!")
# Uploading of CSV file
file_upload = st.file_uploader("Upload your CSV file (.csv):", type=["csv"])
if file_upload is not None:
    st.session_state.df = pd.read_csv(file_upload)
# Identifying the numerical columns and categorical columns
if "df" in st.session_state:
    df = st.session_state.df
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns
    st.session_state.num_cols = num_cols
    st.session_state.cat_cols = cat_cols
    st.write("Numerical Columns:", list(num_cols))
    st.write("Categorical Columns:", list(cat_cols))
    st.session_state.num_cols=num_cols
    )
    # Numerical Selectbox _ Stats
    st.subheader("Numerical Analysis")
    # Displaying the columns to perform statistical measures
    select_num_col=st.selectbox(
        "Select the Numerical Column:",
        st.session_state.num_cols
    )
    #Performing the statistical measures on numerical data:
    if select_num_col:
        if st.button("Analyze Numerical Column"):
            col_data=df[select_num_col]
            # Checking if the column is a Null value column
            if col_data.empty:
                st.write("Non Non-Null values to perform statistical measures.")
                st.write("Please select another column to perform statistical measure")
            elif col_data.nunique()>25:
                st.info("This collumn consists of discrete values")
                st.write("Value Count:",col_data.value_counts())
                st.write("Mode:",col_data.mode()[0])
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
            elif col_data.nunique>25:
                st.write("This column consists of discrete values.")
                st.write("Value Count:",col_data.value_counts())
                st.write("Mode:",col_data.mode()[0])
            else:
                st.write("Count:",df[select_cat_col].count())
                st.write("Number of Unique Values:",df[select_cat_col].nunique())
                st.write("Unique Values:",df[select_cat_col].unique())
                st.write("Value Count:",df[select_cat_col].value_counts())
                st.write("Mode:",df[select_cat_col].mode())
            st.write(f"🎉 Categorical Statistical Measure for {select_cat_col} completed!")

else:
    st.info("Please upload a CSV file to continue")
