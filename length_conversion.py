# ╔════════════════════════════════════════════════╗
# ║           🌍 LENGTH UNITS DICTIONARY           ║
# ║       (Everything is Converted to Meters)      ║
# ╚════════════════════════════════════════════════╝

length_to_meters = {
    "Yoctometers (ym)": 1e-24, "Zeptometers (zm)": 1e-21, "Attometers (am)": 1e-18,
    "Femtometers (fm)": 1e-15, "Picometers (pm)": 1e-12, "Nanometers (nm)": 1e-9,
    "Micrometers (µm)": 1e-6, "Millimeters (mm)": 1e-3, "Centimeters (cm)": 1e-2,
    "Decimeters (dm)": 1e-1, "Meters (m)": 1, "Decameters (dam)": 10, "Hectometers (hm)": 100,
    "Kilometers (km)": 1000, "Megameters (Mm)": 1e6, "Gigameters (Gm)": 1e9,
    "Inches (in)": 0.0254, "Feet (ft)": 0.3048, "Yards (yd)": 0.9144,
    "Miles (mi)": 1609.344, "Nautical Miles (nmi)": 1852, "Astronomical Units (AU)": 149597870700,
    "Light Years (ly)": 9.461e15, "Parsecs (pc)": 3.086e16
}

# ╔════════════════════════════════════════════════╗
# ║        🔄 LENGTH CONVERSION FUNCTION          ║
# ║    (Convert Any Length Unit to Another)      ║
# ╚════════════════════════════════════════════════╝

def convert_length(value, from_unit, to_unit, precision=6):
    """
    📌 Function to convert length from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in length_to_meters or to_unit not in length_to_meters:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert the input value to meters
    value_in_meters = value * length_to_meters[from_unit]

    # 🔹 Step 2: Convert from meters to the target unit
    converted_value = value_in_meters / length_to_meters[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {length_to_meters[from_unit]}) ÷ {length_to_meters[to_unit]}"

    return converted_value, formula
