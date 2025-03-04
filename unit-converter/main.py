#type: ignore
import streamlit as st # streamlit is a library for creating web apps

#  Function to convert units
def convert_units(value, from_unit, to_unit):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,  
    }
    key = f"{from_unit}_{to_unit}"
    
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not available"
st.set_page_config(page_title="Unit Converter", page_icon=":bar_chart:", layout="centered")

value = st.number_input("Enter value:", value=1.0, step=1.0)
unit_from = st.selectbox("From unit:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("To unit:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    if result == "Conversion not available":
        st.error("Conversion not available")
        st.stop()
    else:
        result = convert_units(value, unit_from, unit_to)
        st.success(f"{value} {unit_from} is equal to {result} {unit_to}")

