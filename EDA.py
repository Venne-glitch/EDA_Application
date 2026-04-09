import streamlit as st
import pandas as pd

# Title
st.title("🔍 Descriptive Analyzer for Numerical and Categorical Data")

st.text("This application helps you explore and analyze datasets.")

# Upload
file_upload = st.file_uploader("Upload your CSV file (.csv):", type=["csv"])

# Load
if file_upload is not None:
    st.session_state.df = pd.read_csv(file_upload)

# Main logic
if "df" in st.session_state:
    df = st.session_state.df

    # Identify columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    st.write("Numerical Columns:", list(num_cols))
    st.write("Categorical Columns:", list(cat_cols))

    # -------------------------
    # NUMERICAL ANALYSIS
    # -------------------------
    st.subheader("Numerical Analysis")

    select_num_col = st.selectbox("Select Numerical Column", num_cols)

    if st.button("Analyze Numerical Column", key="num_btn"):
        col_data = df[select_num_col]

        if col_data.dropna().empty:
            st.warning("⚠️ No non-null values to analyze")

        # ✅ Discrete condition FIXED
        elif col_data.nunique() <= 25:
            st.info("ℹ️ This column appears to be discrete")

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

    # -------------------------
    # CATEGORICAL ANALYSIS
    # -------------------------
    st.subheader("Categorical Analysis")

    select_cat_col = st.selectbox("Select Categorical Column", cat_cols)

    if st.button("Analyze Categorical Column", key="cat_btn"):
        col_data = df[select_cat_col]

        if col_data.dropna().empty:
            st.warning("No non-null values to analyze")

        else:
            st.write("Count:", col_data.count())
            st.write("Unique Values:", col_data.nunique())

            if col_data.nunique() > 25:
                st.warning("Discrete value column")

            st.write("Value Counts:")
            st.write(col_data.value_counts())

            st.write("Mode:", col_data.mode()[0])

        st.success(f"🎉 Analysis completed for {select_cat_col}")

else:
    st.info("Please upload a CSV file to continue")
