import streamlit as st
import pandas as pd
import os
import sys
from data_transformation import transform_csv_data

def main():
    st.set_page_config(page_title="Sup Peak Report Transformation", page_icon=":bar_chart:", layout="wide")
    st.title("Sup Peak Report Transformation App")

    # Check if the data_transformation.py file exists
    if not os.path.exists("data_transformation.py"):
        st.error("data_transformation.py file not found. Please make sure the file is in the same directory as this app.")
        sys.exit(1)

    # Upload the .csv file
    uploaded_file = st.sidebar.file_uploader("Upload a Sup Peak report in .csv file here", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)

        # Run the data transformation function
        transformed_df = transform_csv_data(df)

        # Display the transformed DataFrame
        st.subheader("Transformed Sup Peak Report")
        st.write(transformed_df)

        # Display how many columns and rows there are in the dataframe
        st.write(f"There are {transformed_df.shape[0]} rows and {transformed_df.shape[1]} columns in the dataframe.")

        # Show the duplicate rows
        duplicate_rows = transformed_df.loc[transformed_df.duplicated(), :]

        # Display a message if duplicates were found and also a message if there were none
        if transformed_df.duplicated().sum() > 0:
            st.warning("There were duplicates found in the transformed Sup Peak report. Please check the duplicate rows below.")
            # Display the duplicate rows
            st.write(duplicate_rows)
        else:
            st.success("No duplicates found in the transformed report.")

        # Download the transformed DataFrame as a .csv file
        st.download_button(
            label="Download transformed DataFrame",
            data=transformed_df.to_csv(index=False).encode(encoding= "utf-8"),
            file_name="sup_peak_transformed.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()