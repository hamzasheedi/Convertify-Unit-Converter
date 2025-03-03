# ╔════════════════════════════════════════════════╗
# ║        ⚡ ENERGY UNITS CONVERSION DICTIONARY   ║
# ║     (Everything is Converted to Joules First) ║
# ╚════════════════════════════════════════════════╝

energy_to_joules = {
    "Joules (J)": 1, 
    "Kilojoules (kJ)": 1e3, 
    "Megajoules (MJ)": 1e6, 
    "Calories (cal)": 4.184, 
    "Kilocalories (kcal)": 4184, 

    # ⚡ Electrical Units
    "Watt-hours (Wh)": 3600, 
    "Kilowatt-hours (kWh)": 3.6e6, 
    "Megawatt-hours (MWh)": 3.6e9, 

    # 🔬 Scientific Units
    "Electronvolts (eV)": 1.60218e-19, 
    "British Thermal Units (BTU)": 1055.06, 
    "Ergs (erg)": 1e-7
}

# ╔════════════════════════════════════════════════╗
# ║           🔥 ENERGY CONVERSION FUNCTION        ║
# ║    (Convert Any Energy Unit to Another)       ║
# ╚════════════════════════════════════════════════╝

def convert_energy(value, from_unit, to_unit, precision=6):
    """
    📌 Function to convert energy from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in energy_to_joules or to_unit not in energy_to_joules:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert the input value to Joules
    value_in_joules = value * energy_to_joules[from_unit]

    # 🔹 Step 2: Convert from Joules to the target unit
    converted_value = value_in_joules / energy_to_joules[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {energy_to_joules[from_unit]}) ÷ {energy_to_joules[to_unit]}"

    return converted_value, formula

