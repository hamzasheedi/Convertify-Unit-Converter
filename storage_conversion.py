# ╔════════════════════════════════════════════════╗
# ║        💾 DIGITAL STORAGE UNITS DICTIONARY     ║
# ║     (Everything is Converted to Bits First)   ║
# ╚════════════════════════════════════════════════╝

digital_storage_to_bits = {
    "Bits (b)": 1, 
    "Bytes (B)": 8, 
    "Kilobytes (KB)": 8e3, 
    "Megabytes (MB)": 8e6, 
    "Gigabytes (GB)": 8e9, 
    "Terabytes (TB)": 8e12, 
    "Petabytes (PB)": 8e15, 
    "Exabytes (EB)": 8e18, 
    "Zettabytes (ZB)": 8e21, 
    "Yottabytes (YB)": 8e24
}

# ╔════════════════════════════════════════════════╗
# ║      ⚡ DIGITAL STORAGE CONVERSION FUNCTION    ║
# ║    (Convert Any Storage Unit to Another)      ║
# ╚════════════════════════════════════════════════╝

def convert_digital_storage(value, from_unit, to_unit, precision=6):
    """
    📌 Function to convert digital storage from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in digital_storage_to_bits or to_unit not in digital_storage_to_bits:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert the input value to Bits
    value_in_bits = value * digital_storage_to_bits[from_unit]

    # 🔹 Step 2: Convert from Bits to the target unit
    converted_value = value_in_bits / digital_storage_to_bits[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {digital_storage_to_bits[from_unit]}) ÷ {digital_storage_to_bits[to_unit]}"

    return converted_value, formula

