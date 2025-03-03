# ╔════════════════════════════════════════════════╗
# ║          🔄 DATA TRANSFER UNITS DICTIONARY     ║
# ║     (Everything is Converted to bps First)    ║
# ╚════════════════════════════════════════════════╝

data_transfer_to_bps = {
    "Bits per Second (bps)": 1, 
    "Kilobits per Second (kbps)": 1e3, 
    "Megabits per Second (Mbps)": 1e6, 
    "Gigabits per Second (Gbps)": 1e9, 
    "Terabits per Second (Tbps)": 1e12, 

    "Bytes per Second (B/s)": 8, 
    "Kilobytes per Second (kB/s)": 8e3, 
    "Megabytes per Second (MB/s)": 8e6, 
    "Gigabytes per Second (GB/s)": 8e9, 
    "Terabytes per Second (TB/s)": 8e12
}

# ╔════════════════════════════════════════════════╗
# ║       ⚡ DATA TRANSFER CONVERSION FUNCTION     ║
# ║    (Convert Any Data Rate Unit to Another)    ║
# ╚════════════════════════════════════════════════╝

def convert_data_transfer(value, from_unit, to_unit, precision=6):
    """
    📌 Function to convert data transfer speed from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in data_transfer_to_bps or to_unit not in data_transfer_to_bps:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Step 1: Convert the input value to Bits per Second (bps)
    value_in_bps = value * data_transfer_to_bps[from_unit]

    # 🔹 Step 2: Convert from bps to the target unit
    converted_value = value_in_bps / data_transfer_to_bps[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = f"({value} × {data_transfer_to_bps[from_unit]}) ÷ {data_transfer_to_bps[to_unit]}"

    return converted_value, formula

