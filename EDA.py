import streamlit as st
import pandas as pd

# Title and Description
st.title("🔍 Descriptive Analyzer for Numerical and Categorical Data")
st.text("This application helps you explore and analyze datasets.")
st.text("It analyze both categorical and numerical data columns,")
st.text("It identifies any missing values, viewsstatistical measures and provide an preview of your data structure.")
st.text("This will help you draw better and accurate observation for your data.")
st.text("🚀 Upload your dataset and start exploring instantly!")

#  Uploading the file (.csv)
file_upload = st.file_uploader("Upload your CSV file (.csv):", type=["csv"])
if file_upload is not None:
    st.session_state.df = pd.read_csv(file_upload)

# Main logic
if "df" in st.session_state:
    df = st.session_state.df

    discrete_cols=[]
    continuous_cols=[]
    threshold=30
            
    # Identify columns (Numerical and Categorical)
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns
    # Identify columns (Discrete and Continous)
    for col in num_cols:
        if df[col].nunique()>threshold:
            discrete_cols.append(col)
        else:
            continuous_cols.appen(col)
    st.session_state.discrete_cols=discrete_cols
    st.session_state.continuous_cols=continuous_cols

    st.write("Numerical Columns:", list(num_cols))
    st.write("Categorical Columns:", list(cat_cols))
    st.write("Discrete Numerical Columns:",discrete_cols)
    st.write("Continuous Numerical Columns:",continuous_cols)

    # Numerical Analysis
    st.subheader("Numerical Analysis")
    select_num_col = st.selectbox("Select Numerical Column", num_cols)
    if st.button("Analyze Numerical Column", key="num_btn"):
        col_data = df[select_num_col]
        if col_data.dropna().empty:
            st.warning("⚠️ No non-null values to analyze")
        elif select_num_col in discrete_cols:
            st.info("This column appears to be discrete")
            st.write("Value Counts:")
            st.write(col_data.value_counts())
            st.write("Mode:", col_data.mode()[0])
        else:
            st.write("Count:", col_data.count())
            st.write("Max:", col_data.max())
            st.write("Min:", col_data.min())
            st.write("Mean:", col_data.mean())
            st.write("Median:", col_data.median())
            st.write("Variance:", col_data.var())
            st.write("Standard Deviation:", col_data.std())
        st.success(f"🎉 Analysis completed for {select_num_col}")

    # Categorical Analysis
    st.subheader("Categorical Analysis")
    select_cat_col = st.selectbox("Select Categorical Column", cat_cols)
    if st.button("Analyze Categorical Column", key="cat_btn"):
        col_data = df[select_cat_col]
        if col_data.dropna().empty:
            st.warning("No non-null values to analyze")
        else:
            st.write("Count:", col_data.count())
            st.write("Unique Values:", col_data.nunique())
            if select_cat_col in discrete_cols:
                st.warning("Discrete value column")
            st.write("Value Counts:")
            st.write(col_data.value_counts())
            st.write("Mode:", col_data.mode()[0])
        st.success(f"🎉 Analysis completed for {select_cat_col}")
else:
    st.info("Please upload a CSV file to continue")
