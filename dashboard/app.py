
import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Healthcare Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)

# Title
st.title("🏥 Healthcare Analytics Dashboard")
st.markdown("Analysis of 10,000+ patient records using Python, SQL, Excel, and Power BI")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("../data/cleaned_healthcare_dataset.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

condition_filter = st.sidebar.multiselect(
    "Select Medical Condition",
    options=df["Medical Condition"].unique(),
    default=df["Medical Condition"].unique()
)

# Apply filters
filtered_df = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Medical Condition"].isin(condition_filter))
]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Patients", f"{len(filtered_df):,}")

with col2:
    avg_billing = filtered_df["Billing Amount"].mean()
    st.metric("Avg Billing", f"${avg_billing:,.2f}")

with col3:
    avg_age = filtered_df["Age"].mean()
    st.metric("Avg Age", f"{avg_age:.1f} yrs")

with col4:
    avg_stay = filtered_df["Length_of_Stay"].mean()
    st.metric("Avg Stay", f"{avg_stay:.1f} days")

st.markdown("---")

# Row 1: Disease Distribution + Gender Distribution
col1, col2 = st.columns(2)

with col1:
    st.subheader("Disease Distribution")
    disease_counts = filtered_df["Medical Condition"].value_counts().reset_index()
    disease_counts.columns = ["Medical Condition", "Count"]
    fig1 = px.bar(
        disease_counts,
        x="Count",
        y="Medical Condition",
        orientation="h",
        color="Medical Condition",
        title="Patients by Medical Condition"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Gender Distribution")
    gender_counts = filtered_df["Gender"].value_counts().reset_index()
    gender_counts.columns = ["Gender", "Count"]
    fig2 = px.pie(
        gender_counts,
        names="Gender",
        values="Count",
        title="Patients by Gender",
        hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

# Row 2: Billing by Insurance + Admission Type
col1, col2 = st.columns(2)

with col1:
    st.subheader("Average Billing by Insurance Provider")
    billing_by_insurance = filtered_df.groupby("Insurance Provider")["Billing Amount"].mean().reset_index()
    fig3 = px.bar(
        billing_by_insurance,
        x="Insurance Provider",
        y="Billing Amount",
        color="Insurance Provider",
        title="Avg Billing by Insurance"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("Admission Type Breakdown")
    admission_counts = filtered_df["Admission Type"].value_counts().reset_index()
    admission_counts.columns = ["Admission Type", "Count"]
    fig4 = px.pie(
        admission_counts,
        names="Admission Type",
        values="Count",
        title="Patients by Admission Type",
        hole=0.4
    )
    st.plotly_chart(fig4, use_container_width=True)

# Row 3: Length of Stay by Condition
st.subheader("Average Length of Stay by Medical Condition")
stay_by_condition = filtered_df.groupby("Medical Condition")["Length_of_Stay"].mean().reset_index()
fig5 = px.bar(
    stay_by_condition,
    x="Medical Condition",
    y="Length_of_Stay",
    color="Medical Condition",
    title="Avg Length of Stay (Days) by Condition"
)
st.plotly_chart(fig5, use_container_width=True)

# Row 4: Top Doctors
st.subheader("Top 10 Doctors by Patient Count")
top_doctors = filtered_df["Doctor"].value_counts().head(10).reset_index()
top_doctors.columns = ["Doctor", "Patient Count"]
fig6 = px.bar(
    top_doctors,
    x="Patient Count",
    y="Doctor",
    orientation="h",
    title="Most Active Doctors"
)
st.plotly_chart(fig6, use_container_width=True)

# Data table
st.markdown("---")
st.subheader("📋 Raw Data")
st.dataframe(filtered_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Built by Saroj Kumawat** | Healthcare Analytics Dashboard Project")
