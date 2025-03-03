import streamlit as st
#conversion functions
from length_conversion import convert_length
from weight_conversion import convert_weight
from area_conversion import convert_area
from time_conversion import convert_time
from energy_conversion import convert_energy
from storage_conversion import convert_digital_storage
from data_conversion import convert_data_transfer
from temperature_conversion import convert_temperature
from speed_conversion import convert_speed
from volume_conversion import convert_volume
from pressure_conversion import convert_pressure
from fuel_conversion import convert_fuel_economy
from frequency_conversion import convert_frequency
from angle_conversion import convert_plane_angle



#unit lists
from units import (
    length_units, weight_units, area_units, time_units, energy_units, 
    digital_storage_units, data_transfer_units, temperature_units, 
    speed_units, volume_units, pressure_units, fuel_economy_units, 
    frequency_units, plane_angle_units
)



#app
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
    }

    section[data-testid="stSidebar"] {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }

    div.stButton > button {
        background-color: #BB86FC !important;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }

    div.stAlert.stSuccess {
        background-color: #198754 !important;
        color: white !important;
        border-radius: 5px;
        padding: 10px;
    }

    div.stAlert.stInfo {
        background-color: #FFC107 !important;
        color: black !important;
        border-radius: 5px;
        padding: 10px;
    }

    /* 📝 Input Fields */
    input[type="text"], input[type="number"], textarea, select {
        background-color: #1E1E1E !important;
        color: #E0E0E0 !important;
        border-radius: 5px;
        border: 1px solid #BB86FC;
    }

    /*  Slider */
    div[data-baseweb="slider"] {
        background-color: #BB86FC !important;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🔄 Convertify: The Ultimate Unit Converter")    
st.subheader("Effortlessly convert between **500+ units** across **14+ categories** with precision and speed!")  





#tab
tabs = st.tabs([
    "Length", "Weight", "Area", "Time", "Energy",
    "Digital Storage", "Data Transfer", "Temperature",
    "Speed", "Volume", "Pressure", "Fuel Economy",
    "Frequency", "Plane Angle"
])



#Conversion Function for all conversion
def unit_conversion(tab_name, unit_list, convert_function, key_prefix):
    """Handles conversion for all unit categories in a structured way."""
    st.markdown(f"### **Convert {tab_name}**")
    
    #Three-column layout
    col1, col2, col3 = st.columns([3, 3, 4])

    with col1:
        from_unit = st.selectbox(f"From:", unit_list, key=f"{key_prefix}_from")

    with col2:
        to_unit = st.selectbox(f"To:", unit_list, key=f"{key_prefix}_to")

    with col3:
        value = st.number_input("Enter Value:", min_value=0.0, format="%.4f", key=f"{key_prefix}_value")

    if from_unit and to_unit:
        converted_value, formula = convert_function(value, from_unit, to_unit)
        st.success(f" **Converted Value:** {value} {from_unit} ➝ **{converted_value:.4f} {to_unit}**")
        st.info(f"📌 **Formula Used:** `{formula}`")




#  Handling Each Tab
#((tab_name, unit_list, convert_function, key_prefix))
with tabs[0]:  unit_conversion("Length", length_units, convert_length, "length")
with tabs[1]:  unit_conversion("Weight", weight_units, convert_weight, "weight")
with tabs[2]:  unit_conversion("Area", area_units, convert_area, "area")
with tabs[3]:  unit_conversion("Time", time_units, convert_time, "time")
with tabs[4]:  unit_conversion("Energy", energy_units, convert_energy, "energy")
with tabs[5]:  unit_conversion("Digital Storage", digital_storage_units, convert_digital_storage, "storage")
with tabs[6]:  unit_conversion("Data Transfer", data_transfer_units, convert_data_transfer, "data")
with tabs[7]:  unit_conversion("Temperature", temperature_units, convert_temperature, "temperature")
with tabs[8]:  unit_conversion("Speed", speed_units, convert_speed, "speed")
with tabs[9]:  unit_conversion("Volume", volume_units, convert_volume, "volume")
with tabs[10]: unit_conversion("Pressure", pressure_units, convert_pressure, "pressure")
with tabs[11]: unit_conversion("Fuel Economy", fuel_economy_units, convert_fuel_economy, "fuel")
with tabs[12]: unit_conversion("Frequency", frequency_units, convert_frequency, "frequency")
with tabs[13]: unit_conversion("Plane Angle", plane_angle_units, convert_plane_angle, "angle")



