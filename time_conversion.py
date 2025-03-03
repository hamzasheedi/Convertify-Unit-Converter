# ╔════════════════════════════════════════════════╗
# ║             ⏳ TIME CONVERSION UNITS           ║
# ║   (Convert Anything: Seconds, Minutes, Hours) ║
# ╚════════════════════════════════════════════════╝

time_to_seconds = {
    "Seconds (s)": 1, "Milliseconds (ms)": 1e-3, "Microseconds (µs)": 1e-6, 
    "Nanoseconds (ns)": 1e-9, "Picoseconds (ps)": 1e-12, "Femtoseconds (fs)": 1e-15, 
    "Attoseconds (as)": 1e-18,

    # ⏳ Standard Time Units
    "Minutes (min)": 60, "Hours (hr)": 3600, "Days (day)": 86400, 
    "Weeks (wk)": 604800, "Months (mo)": 2.628e6, "Years (yr)": 3.154e7
}

# ╔════════════════════════════════════════════════╗
# ║             🔄 TIME CONVERSION FUNCTION        ║
# ╚════════════════════════════════════════════════╝

def convert_time(value, from_unit, to_unit, precision=6):
    """
    ⏳ Convert time from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The original time unit.
    - to_unit: The target time unit.
    - precision: Decimal precision (default: 6).
    """

    # 🛑 Handle Same-Unit Conversion
    if from_unit == to_unit:
        return value, "No conversion needed"

    # ⏳ Step 1: Convert to Seconds First
    if from_unit in time_to_seconds:
        value_in_seconds = value * time_to_seconds[from_unit]
    else:
        return None, "❌ Error: Invalid unit provided"

    # 🔄 Step 2: Convert from Seconds to Target Unit
    if to_unit in time_to_seconds:
        converted_value = value_in_seconds / time_to_seconds[to_unit]
    else:
        return None, "❌ Error: Invalid target unit"

    # 📝 Formula Explanation
    formula = f"({value} × {time_to_seconds[from_unit]}) ÷ {time_to_seconds[to_unit]}"

    return round(converted_value, precision), formula

