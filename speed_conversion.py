# ╔════════════════════════════════════════════════╗
# ║       🚗 SPEED UNITS CONVERSION DICTIONARY     ║
# ║   (Everything is Converted to Meters/Second)   ║
# ╚════════════════════════════════════════════════╝

speed_to_mps = {
    "Meters per Second (m/s)": 1,
    "Kilometers per Hour (km/h)": 0.277778,  # 1 km/h = 0.277778 m/s
    "Miles per Hour (mph)": 0.44704,        # 1 mph = 0.44704 m/s
    "Feet per Second (ft/s)": 0.3048,       # 1 ft/s = 0.3048 m/s
    "Knots (kn)": 0.514444                  # 1 knot = 0.514444 m/s
}

# ╔════════════════════════════════════════════════╗
# ║          🔄 SPEED CONVERSION FUNCTION          ║
# ║   (Convert Any Speed Unit to Another)         ║
# ╚════════════════════════════════════════════════╝

def convert_speed(value, from_unit, to_unit, precision=6):
    """
    🚗 Function to convert speed from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in speed_to_mps or to_unit not in speed_to_mps:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert to Meters per Second (m/s)
    value_in_mps = value * speed_to_mps[from_unit]

    # 🔹 Step 2: Convert from Meters per Second to Target Unit
    converted_value = value_in_mps / speed_to_mps[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {speed_to_mps[from_unit]}) ÷ {speed_to_mps[to_unit]}"

    return converted_value, formula
