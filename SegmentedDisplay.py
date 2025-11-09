from machine import Pin
import time

"""
The center Pins, from both side, is connected to GND, connect it with a resistor
"""

pin_map = {
    'g': Pin(19, Pin.OUT),
    'f': Pin(18, Pin.OUT),
    'a': Pin(17, Pin.OUT),
    'b': Pin(16, Pin.OUT),
    'e': Pin(12, Pin.OUT),
    'd': Pin(14, Pin.OUT),
    'c': Pin(27, Pin.OUT),
    'dp': Pin(26, Pin.OUT)
}

numMap = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'd', 'e', 'g'],
    3: ['a', 'b', 'c', 'd', 'g'],
    4: ['b', 'c', 'f', 'g'],
    5: ['a', 'c', 'd', 'f', 'g'],
    6: ['a', 'c', 'd', 'e', 'f', 'g'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
}

def cls():
    for i in pin_map.values():
        i.value(False)
    
def display(num):
    cls()
    numToLight = numMap[num]
    for segment in numToLight:
        pin_map[segment].value(True)

while True:
    lightNum = [0,1,2,3,4,5,6,7,8,9]
    for num in reversed(lightNum):
        display(num)
        time.sleep(1)
            
    