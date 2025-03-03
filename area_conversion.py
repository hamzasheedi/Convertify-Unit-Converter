# ╔════════════════════════════════════════════════╗
# ║              📐 AREA UNITS DICTIONARY         ║
# ║       (Everything is Converted to m² First)  ║
# ╚════════════════════════════════════════════════╝

area_to_m2 = {
    "Square Meters (m²)": 1, "Square Centimeters (cm²)": 0.0001, "Square Millimeters (mm²)": 1e-6,
    "Square Kilometers (km²)": 1e6, "Hectares (ha)": 10000, "Ares (a)": 100,
    
    # 📏 Imperial & US Customary Units
    "Square Inches (in²)": 0.00064516, "Square Feet (ft²)": 0.092903, 
    "Square Yards (yd²)": 0.836127, "Square Miles (mi²)": 2.59e6, "Acres (ac)": 4046.86
}

# ╔════════════════════════════════════════════════╗
# ║          🔄 AREA CONVERSION FUNCTION          ║
# ║      (Convert Any Area Unit to Another)      ║
# ╚════════════════════════════════════════════════╝

def convert_area(value, from_unit, to_unit, precision=6):
    """
    📌 Function to convert area from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in area_to_m2 or to_unit not in area_to_m2:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert the input value to square meters
    value_in_m2 = value * area_to_m2[from_unit]

    # 🔹 Step 2: Convert from square meters to the target unit
    converted_value = value_in_m2 / area_to_m2[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {area_to_m2[from_unit]}) ÷ {area_to_m2[to_unit]}"

    return converted_value, formula
