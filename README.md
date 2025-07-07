#  MEP LCA Visualizer – Streamlit Web App

A web-based **Life Cycle Assessment (LCA) Visualizer** for common MEP (Mechanical, Electrical, Plumbing) components.

This tool estimates and displays carbon emissions (kg CO₂e) across multiple life cycle stages — from raw material extraction to end-of-life — for MEP equipment like FAHUs and GI Ducts.

---

##  Live Demo

🔗 [Click here to try the app](https://your-streamlit-app-link.com)  
*(Replace with your actual deployed Streamlit link)*

---

##  Features

- Component selection (e.g., FAHU, GI Duct)
- Emission breakdown by life cycle stage:
  - Material Extraction
  - Manufacturing
  - Transport
  - Installation
  - Operation
  - End of Life
- Stage-wise carbon visualization (bar chart)
- Total carbon footprint summary
- CSV-driven — easy to extend with more components

---

## 📁 File Structure
mep-lca-visualizer/
├── app.py # Streamlit frontend and logic
├── mep_lca_factors.csv # Lifecycle emissions data
├── requirements.txt # Streamlit, pandas, matplotlib
└── README.md # Project documentation

yaml
Copy
Edit

---

##  Sample Data (FAHU Example)

| Stage               | Emissions (kg CO₂e) |
|---------------------|---------------------|
| Material Extraction | 300                 |
| Manufacturing       | 650                 |
| Transport           | 35                  |
| Installation        | 60                  |
| Operation           | 1800                |
| End of Life         | 120                 |

---

##  Tech Stack

- Python
- Streamlit
- pandas
- matplotlib

---

##  How to Run Locally

```bash
git clone https://github.com/yourusername/mep-lca-visualizer.git
cd mep-lca-visualizer
pip install -r requirements.txt
streamlit run app.py

## This is a very basic for beginners understanding Model.

Developed By
Radhika

