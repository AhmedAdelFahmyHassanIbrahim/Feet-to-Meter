#functions
from main import feet_entry, feet_value, meter_value

def convert():
    """
    docstring
    """
    value = float(feet_entry.get())
    meter = value * 0.3048
    meter_value.set("%.4f" %meter)

def clear():
    feet_value.set("")
    meter_value.set("")