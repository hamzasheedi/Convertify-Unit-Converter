# ╔════════════════════════════════════════════════╗
# ║        🎵 FREQUENCY UNITS CONVERSION DICT      ║
# ║    (Everything is Converted to Hertz First)   ║
# ╚════════════════════════════════════════════════╝

frequency_to_hz = {
    "Hertz (Hz)": 1, 
    "Kilohertz (kHz)": 1e3, 
    "Megahertz (MHz)": 1e6, 
    "Gigahertz (GHz)": 1e9, 
    "Terahertz (THz)": 1e12
}

# ╔════════════════════════════════════════════════╗
# ║           🎚️ FREQUENCY CONVERSION FUNCTION      ║
# ║       (Convert Any Frequency Unit to Another)  ║
# ╚════════════════════════════════════════════════╝

def convert_frequency(value, from_unit, to_unit, precision=6):
    """
    📌 Function to convert frequency from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in frequency_to_hz or to_unit not in frequency_to_hz:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert the input value to Hertz
    value_in_hz = value * frequency_to_hz[from_unit]

    # 🔹 Step 2: Convert from Hertz to the target unit
    converted_value = value_in_hz / frequency_to_hz[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {frequency_to_hz[from_unit]}) ÷ {frequency_to_hz[to_unit]}"

    return converted_value, formula

