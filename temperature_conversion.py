# ╔════════════════════════════════════════════════╗
# ║       🌡 TEMPERATURE CONVERSION FUNCTIONS      ║
# ║      (Handles Celsius, Fahrenheit, Kelvin)    ║
# ╚════════════════════════════════════════════════╝

def celsius_to_fahrenheit(celsius):
    """ 🌡 Convert Celsius (°C) to Fahrenheit (°F) """
    return (celsius * 9/5) + 32, f"({celsius} × 9/5) + 32"

def celsius_to_kelvin(celsius):
    """ ❄ Convert Celsius (°C) to Kelvin (K) """
    return celsius + 273.15, f"{celsius} + 273.15"

def celsius_to_rankine(celsius):
    """ 🔥 Convert Celsius (°C) to Rankine (°R) """
    return (celsius + 273.15) * 9/5, f"({celsius} + 273.15) × 9/5"

def celsius_to_delisle(celsius):
    """ 🏺 Convert Celsius (°C) to Delisle (°De) """
    return (100 - celsius) * 3/2, f"(100 - {celsius}) × 3/2"

def celsius_to_newton(celsius):
    """ ⚖ Convert Celsius (°C) to Newton (°N) """
    return celsius * 33/100, f"{celsius} × 33/100"

def celsius_to_reaumur(celsius):
    """ 🔄 Convert Celsius (°C) to Réaumur (°Ré) """
    return celsius * 4/5, f"{celsius} × 4/5"

def celsius_to_romer(celsius):
    """ 🌀 Convert Celsius (°C) to Rømer (°Rø) """
    return (celsius * 21/40) + 7.5, f"({celsius} × 21/40) + 7.5"

# ╔════════════════════════════════════════════════╗
# ║          🔄 UNIVERSAL TEMPERATURE CONVERTER    ║
# ╚════════════════════════════════════════════════╝

def convert_temperature(value, from_unit, to_unit, precision=6):
    """
    🌡 Convert temperature from one unit to another.
    - value: The numerical value to convert.
    - from_unit: The starting unit.
    - to_unit: The target unit.
    - precision: Decimal precision (default: 6).
    """

    # 🌟 Step 1: Convert Everything to Celsius
    if from_unit == "Celsius (°C)":
        celsius = value
    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin (K)":
        celsius = value - 273.15
    elif from_unit == "Rankine (°R)":
        celsius = (value - 491.67) * 5/9
    elif from_unit == "Delisle (°De)":
        celsius = 100 - (value * 2/3)
    elif from_unit == "Newton (°N)":
        celsius = value * 100/33
    elif from_unit == "Réaumur (°Ré)":
        celsius = value * 5/4
    elif from_unit == "Rømer (°Rø)":
        celsius = (value - 7.5) * 40/21
    else:
        return None, "❌ Error: Invalid unit provided"

    # 🔥 Step 2: Convert Celsius to Target Unit
    conversion_functions = {
        "Celsius (°C)": lambda x: (x, f"{x} (No conversion needed)"),
        "Fahrenheit (°F)": celsius_to_fahrenheit,
        "Kelvin (K)": celsius_to_kelvin,
        "Rankine (°R)": celsius_to_rankine,
        "Delisle (°De)": celsius_to_delisle,
        "Newton (°N)": celsius_to_newton,
        "Réaumur (°Ré)": celsius_to_reaumur,
        "Rømer (°Rø)": celsius_to_romer
    }

    if to_unit not in conversion_functions:
        return None, "❌ Error: Invalid target unit"

    converted_value, formula = conversion_functions[to_unit](celsius)
    return round(converted_value, precision), formula

