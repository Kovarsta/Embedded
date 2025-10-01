from machine import Pin, ADC
from time import sleep

# --- Configuration ---
ROTARY_PIN = 15
READ_DELAY = 0.1 

# ADC Max value for 12-bit resolution
ADC_MAX = 4095 

# --- Setup ---
adc = ADC(Pin(ROTARY_PIN))
adc.atten(ADC.ATTN_11DB) # Max voltage ~3.3V
adc.width(ADC.WIDTH_12BIT) # 0 to 4095

# --- Main Loop ---
while True:
    # 1. Read the raw ADC value (0 to 4095)
    raw_value = adc.read()

    # 2. Normalize the value to a 0.0 to 1.0 range
    # Ensure floating point division by using 4095.0
    normalized_value = raw_value / ADC_MAX
    
    # 3. Print the results (formatted to 3 decimal places)
    print(f"Raw ADC: {raw_value}, Normalized Value: {normalized_value:.3f}")
    
    sleep(READ_DELAY)