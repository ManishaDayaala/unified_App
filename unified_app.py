import streamlit as st

# Set up the page
st.set_page_config(page_title="Smart Maintenance App", layout="wide")
st.title("🛠️ Smart Maintenance App")

# Data: Plant and its machine links
plant_links = {
    "Hinupur CRP ": {
        "ACME-1": "https://appacme.streamlit.app/",
        "Barpeeling-Reeling": "https://barpeelingupdatedtime.streamlit.app/",
        "Straightening": "https://app-straightning-crp.streamlit.app/",
        "ACME-2": "https://app-acme2-crp.streamlit.app/"
    },
    "Hinupur CP ": {
        "Doosan": "https://doosan-cp-app.streamlit.app/",
        "Paint Bhooth TH": "https://paint-cp-app.streamlit.app/",
        "Sierra Burnishing": "https://sierra-cp-app.streamlit.app/"
    },
    "Peenya ": {
        "FG-Paint Bhooth": "https://fgpeenya-app.streamlit.app/",
        "Sierra Burnishing-2": "https://peenya-sierra-app.streamlit.app/",
        "TFW-2": "https://tfw2peenya-app.streamlit.app/"
    },
    "Chennai C1 ": {
        "Paint Shop-1": "https://app-ps1c1.streamlit.app/",
        "Paint shop-2": "https://app-ps2c1.streamlit.app/",
        "Sierra-2": "https://sierra-2c1-app.streamlit.app/"
    },
    "Chennai A22 ": {
        "Robo Polishing": "https://app-roboa22.streamlit.app/",
        "Microtek Burnishing": "https://microteka22-app.streamlit.app/",
        "Sierra burnishing": "https://sierraa22py-app.streamlit.app/"
    },
    "Jaipur ": {
        "Friction Welding": "https://friction-jaipur-app.streamlit.app/",
        "Widma Burnishing": "https://widma-jaipur-app.streamlit.app/"
        
    }
}

# Display Instructions
instructions = """
### Welcome to Smart Maintenance App!
- Select a plant below to view the available machines.
- Click on the machine name to open the respective machine link.

---

### NOTE:
- 📁 **Excel File Only**  
  The app only accepts Excel (.xlsx) files. Other file formats will not be processed.

- 🔄 **Facing an Error**  
  If something goes wrong, simply refresh the page and try again.

- 📞 **Still Not Working**  
  If the issue continues after a refresh, please contact the app owner or support team for help.
  
- 🛠️ **Not Used Recently?**  
  Tap **"Get the App Backup"** if the app hasn’t been used in a few days.
"""
st.markdown(instructions)

# Function to display machine links for a selected plant
def display_plant_machine_links(plant_name):
    st.subheader(f"Machines in {plant_name}")
    
    machine_links = plant_links[plant_name]
    
    # Display machine names with links
    for machine, link in machine_links.items():
        st.markdown(f"""
            <a href="{link}" target="_blank">
                <button style="width: 100%; padding: 10px; font-size: 16px;">{machine}</button>
            </a>
        """, unsafe_allow_html=True)
    
    # Back button to return to Home
    #if st.button("Back to Home"):
        #show_home_page()

# Home page: Select a plant
def show_home_page():
    st.subheader("Select a Plant:")

    plant_names = list(plant_links.keys())
    selected_plant = st.selectbox("Choose a plant to explore:", plant_names)

    if selected_plant:
        display_plant_machine_links(selected_plant)

# Start with home page
show_home_page()
