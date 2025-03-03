# ╔════════════════════════════════════════════════╗
# ║     🏋️ PRESSURE UNITS CONVERSION DICT         ║
# ║    (Everything is Converted to Pascals First)  ║
# ╚════════════════════════════════════════════════╝

pressure_to_pascals = {
    "Pascals (Pa)": 1,
    "Kilopascals (kPa)": 1e3,       # 1 kPa = 1,000 Pa
    "Megapascals (MPa)": 1e6,       # 1 MPa = 1,000,000 Pa
    "Bars (bar)": 1e5,              # 1 bar = 100,000 Pa
    "Millibars (mbar)": 100,        # 1 mbar = 100 Pa
    "Pounds per Square Inch (psi)": 6894.76,  # 1 psi ≈ 6894.76 Pa
    "Atmospheres (atm)": 101325,    # 1 atm = 101,325 Pa
    "Torr (Torr)": 133.322,         # 1 Torr ≈ 133.322 Pa
    "Millimeters of Mercury (mmHg)": 133.322  # 1 mmHg ≈ 133.322 Pa
}

# ╔════════════════════════════════════════════════╗
# ║         🔄 PRESSURE CONVERSION                 ║
# ║    (Convert Any Pressure Unit to Another)      ║
# ╚════════════════════════════════════════════════╝

def convert_pressure(value, from_unit, to_unit, precision=6):
    """
    🏋️ Function to convert pressure from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in pressure_to_pascals or to_unit not in pressure_to_pascals:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert to Pascals First
    value_in_pascals = value * pressure_to_pascals[from_unit]

    # 🔹 Step 2: Convert from Pascals to Target Unit
    converted_value = value_in_pascals / pressure_to_pascals[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {pressure_to_pascals[from_unit]}) ÷ {pressure_to_pascals[to_unit]}"

    return converted_value, formula

