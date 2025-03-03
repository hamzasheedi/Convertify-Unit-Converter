# ╔════════════════════════════════════════════════╗
# ║              🥤 VOLUME CONVERSION UNITS        ║
# ║  (Convert Any Volume: Liters, Gallons, Cups)  ║
# ╚════════════════════════════════════════════════╝

volume_to_liters = {
    "Liters (L)": 1, "Milliliters (mL)": 1e-3, "Cubic Meters (m³)": 1000,
    "Cubic Centimeters (cm³)": 1e-3, "Cubic Millimeters (mm³)": 1e-6,

    # 🏛️ Imperial & US Customary Units
    "Gallons (gal)": 3.78541, "Quarts (qt)": 0.946353, "Pints (pt)": 0.473176,
    "Cups (cup)": 0.24, "Fluid Ounces (fl oz)": 0.0295735,
    "Cubic Inches (in³)": 0.0163871, "Cubic Feet (ft³)": 28.3168,
    "Cubic Yards (yd³)": 764.555
}

# ╔════════════════════════════════════════════════╗
# ║             🔄 VOLUME CONVERSION FUNCTION      ║
# ╚════════════════════════════════════════════════╝

def convert_volume(value, from_unit, to_unit, precision=6):
    """
    🥤 Convert volume from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The original volume unit.
    - to_unit: The target volume unit.
    - precision: Decimal precision (default: 6).
    """

    # 🛑 Handle Same-Unit Conversion
    if from_unit == to_unit:
        return value, "No conversion needed"

    # 🥤 Step 1: Convert to Liters First
    if from_unit in volume_to_liters:
        value_in_liters = value * volume_to_liters[from_unit]
    else:
        return None, "❌ Error: Invalid unit provided"

    # 🔄 Step 2: Convert from Liters to Target Unit
    if to_unit in volume_to_liters:
        converted_value = value_in_liters / volume_to_liters[to_unit]
    else:
        return None, "❌ Error: Invalid target unit"

    # 📝 Formula Explanation
    formula = f"({value} × {volume_to_liters[from_unit]}) ÷ {volume_to_liters[to_unit]}"

    return round(converted_value, precision), formula

