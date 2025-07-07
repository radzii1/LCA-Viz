import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load emission data
df = pd.read_csv("mep_lca_factors.csv")

st.title("🔧 MEP Carbon Visualizer – LCA Tool")
st.caption("Estimate and visualize life cycle emissions for MEP components.")

# Select component
component = st.selectbox("Select MEP Component", df["Component"].unique())

# Filter data
component_df = df[df["Component"] == component]

# Display data
st.subheader(f"📊 Emission Breakdown for: {component}")
st.dataframe(component_df)

# Total emissions
total_emissions = component_df["Emission Factor (kg CO2e)"].sum()
st.markdown(f"### 🔥 Total CO₂e Emissions: **{total_emissions:.2f} kg**")

# Plot chart
st.subheader("🔍 Stage-wise Emissions")
fig, ax = plt.subplots()
ax.bar(component_df["Stage"], component_df["Emission Factor (kg CO2e)"], color='skyblue')
plt.xticks(rotation=30)
plt.ylabel("kg CO₂e")
plt.title(f"{component} – Emissions by Life Cycle Stage")
st.pyplot(fig)
