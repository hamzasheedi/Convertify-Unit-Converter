# ╔════════════════════════════════════════════════╗
# ║            ⚖️ WEIGHT UNITS DICTIONARY         ║
# ║      (Everything is Converted to Kilograms)   ║
# ╚════════════════════════════════════════════════╝

weight_to_kg = {
    "Kilograms (kg)": 1, "Grams (g)": 0.001, "Milligrams (mg)": 1e-6, "Metric Tons (t)": 1000,
    "Pounds (lb)": 0.453592, "Ounces (oz)": 0.0283495, "Stones (st)": 6.35029,
    "Tons (US)": 907.184, "Tons (UK)": 1016, "Micrograms (µg)": 1e-9, "Nanograms (ng)": 1e-12,
    "Earth Mass (M⊕)": 5.972e24, "Solar Mass (M☉)": 1.989e30
}

# ╔════════════════════════════════════════════════╗
# ║        🔄 WEIGHT CONVERSION FUNCTION          ║
# ║    (Convert Any Weight Unit to Another)      ║
# ╚════════════════════════════════════════════════╝

def convert_weight(value, from_unit, to_unit, precision=6):
    """
    📌 Function to convert weight from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in weight_to_kg or to_unit not in weight_to_kg:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert the input value to kilograms
    value_in_kg = value * weight_to_kg[from_unit]

    # 🔹 Step 2: Convert from kilograms to the target unit
    converted_value = value_in_kg / weight_to_kg[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # ⚖️ Formula Explanation (for educational purposes)
    formula = f"({value} × {weight_to_kg[from_unit]}) ÷ {weight_to_kg[to_unit]}"

    return converted_value, formula


