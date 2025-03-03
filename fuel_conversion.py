# ╔════════════════════════════════════════════════╗
# ║        ⛽ FUEL ECONOMY UNITS CONVERSION DICT    ║
# ║      (Everything is Converted to km/L First)   ║
# ╚════════════════════════════════════════════════╝

fuel_economy_to_kmpl = {
    "Kilometers per Liter (km/L)": 1,
    "Liters per 100 Kilometers (L/100km)": 100,
    "Miles per Gallon (mpg)": 0.425144,  # Approximate conversion
    "Miles per Gallon (US) (mpg US)": 0.425144,
    "Miles per Gallon (UK) (mpg UK)": 0.354006
}

# ╔════════════════════════════════════════════════╗
# ║           🚗 FUEL ECONOMY CONVERSION           ║
# ║    (Convert Any Fuel Economy Unit to Another)  ║
# ╚════════════════════════════════════════════════╝

def convert_fuel_economy(value, from_unit, to_unit, precision=6):
    """
    ⛽ Function to convert fuel economy from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The unit of the given value.
    - to_unit: The target unit to convert into.
    - precision: Decimal precision for output (default: 6).
    """

    # 🚨 Handle Case: Same Unit Conversion
    if from_unit == to_unit:
        return round(value, precision), "✅ No conversion needed"

    # ❌ Handle Case: Invalid Units
    if from_unit not in fuel_economy_to_kmpl or to_unit not in fuel_economy_to_kmpl:
        return None, "❌ Error: Invalid unit provided"

    # 🔹 Special Case: Converting from L/100km (inverse conversion)
    if from_unit == "Liters per 100 Kilometers (L/100km)":
        value_in_kmpl = 100 / value
    else:
        value_in_kmpl = value * fuel_economy_to_kmpl[from_unit]

    # 🔹 Convert km/L to the Target Unit
    if to_unit == "Liters per 100 Kilometers (L/100km)":
        converted_value = 100 / value_in_kmpl
    else:
        converted_value = value_in_kmpl / fuel_economy_to_kmpl[to_unit]

    # 🎯 Round the final result for better readability
    converted_value = round(converted_value, precision)

    # 📏 Formula Explanation (for educational purposes)
    formula = (
        f"100 ÷ {value}" if from_unit == "Liters per 100 Kilometers (L/100km)" else
        f"({value} × {fuel_economy_to_kmpl[from_unit]}) ÷ {fuel_economy_to_kmpl[to_unit]}"
    )

    return converted_value, formula

