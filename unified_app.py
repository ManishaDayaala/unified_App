# app.py
import streamlit as st

st.set_page_config(page_title="Unified Machine Dashboard", layout="wide")
st.title("🛠️ Unified Machine Dashboard")

machine_links = {
    "ACME-1": "https://appacme.streamlit.app/",
    "Barpeeling-Reeling": "https://barpeelingupdatedtime.streamlit.app/",
    "Straightening": "https://app-straightning-crp.streamlit.app/",
    "ACME-2": "https://app-acme2-crp.streamlit.app/",
}

st.subheader("Select a Machine:")

# Layout buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🔧ACME-1 "):
        st.markdown(f"[Open Machine A 🔗]({machine_links['ACME-1']})", unsafe_allow_html=True)
    if st.button("⚙️ Straightening"):
        st.markdown(f"[Open Machine C 🔗]({machine_links['Straightening']})", unsafe_allow_html=True)

with col2:
    if st.button("🔩 Barpeeling-Reeling"):
        st.markdown(f"[Open Machine B 🔗]({machine_links['Barpeeling-Reeling']})", unsafe_allow_html=True)
    if st.button("🧰 ACME-2"):
        st.markdown(f"[Open Machine D 🔗]({machine_links['ACME-2']})", unsafe_allow_html=True)

st.markdown("---")
st.write("Or preview one machine right here ⬇️")

selected = st.selectbox("Choose a machine to embed:", list(machine_links.keys()))
st.components.v1.iframe(machine_links[selected], height=800)
