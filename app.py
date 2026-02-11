import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="EnergyPulse", layout="wide")

st.title("EnergyPulse ⚡")
st.write("Dashboard de consumo eléctrico y costos (demo).")

# Datos demo
df = pd.DataFrame({
    "hora": pd.date_range("2026-01-01", periods=24, freq="H"),
    "kWh": np.random.rand(24) * 2
})
st.line_chart(df.set_index("hora")["kWh"])

st.success("Si estás viendo esto, Streamlit está funcionando.")
