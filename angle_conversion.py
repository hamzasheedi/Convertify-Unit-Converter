# ╔════════════════════════════════════════════════╗
# ║     📐 PLANE ANGLE UNITS CONVERSION DICT       ║
# ║    (Everything is Converted to Degrees First)  ║
# ╚════════════════════════════════════════════════╝

plane_angle_to_degrees = {
    "Degrees (°)": 1,
    "Radians (rad)": 57.2958,  # 1 rad ≈ 57.2958°
    "Gradians (grad)": 0.9,    # 1 grad = 0.9°
    "Arcminutes (')": 1 / 60,  # 1 arcminute = 1/60°
    "Arcseconds (″)": 1 / 3600,  # 1 arcsecond = 1/3600°
    "Turns (rev)": 360  # 1 full turn = 360°
}

# ╔════════════════════════════════════════════════╗
# ║         🔄 PLANE ANGLE CONVERSION              ║
# ║    (Convert Any Angle Unit to Another)         ║
# ╚════════════════════════════════════════════════╝

def convert_plane_angle(value, from_unit, to_unit, precision=6):
    """
    📐 Function to convert plane angle from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in plane_angle_to_degrees or to_unit not in plane_angle_to_degrees:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert to Degrees First
    value_in_degrees = value * plane_angle_to_degrees[from_unit]

    # 🔹 Step 2: Convert from Degrees to Target Unit
    converted_value = value_in_degrees / plane_angle_to_degrees[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {plane_angle_to_degrees[from_unit]}) ÷ {plane_angle_to_degrees[to_unit]}"

    return converted_value, formula

