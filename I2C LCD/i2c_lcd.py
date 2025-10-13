"""
Improved I2C LCD driver for ESP32 (PCF8574 + HD44780)
Includes error handling and better timing.
"""

from lcd_api import LcdApi
from time import sleep_ms

DEFAULT_I2C_ADDR = 0x27  # Common address: 0x27 or 0x3F

MASK_RS = 0x01
MASK_RW = 0x02
MASK_E = 0x04
SHIFT_BACKLIGHT = 3
SHIFT_DATA = 4


class I2cLcd(LcdApi):
    """HD44780 LCD via PCF8574 on I2C."""

    def __init__(self, i2c, i2c_addr=DEFAULT_I2C_ADDR, num_lines=2, num_columns=16):
        self.i2c = i2c
        self.i2c_addr = i2c_addr

        # ✅ Kiểm tra kết nối I2C trước khi ghi dữ liệu
        devices = i2c.scan()
        if self.i2c_addr not in devices:
            raise OSError(f"Không tìm thấy LCD tại địa chỉ {hex(self.i2c_addr)}! "
                          f"Các thiết bị tìm thấy: {[hex(d) for d in devices]}")

        try:
            self.i2c.writeto(self.i2c_addr, bytearray([0]))
        except Exception as e:
            raise OSError(f"Lỗi khi ghi dữ liệu I2C tới LCD ({hex(self.i2c_addr)}): {e}")

        sleep_ms(20)
        # Gửi lệnh reset 3 lần
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(5)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(1)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(1)

        # Đặt LCD vào chế độ 4-bit
        self.hal_write_init_nibble(self.LCD_FUNCTION)
        sleep_ms(1)

        LcdApi.__init__(self, num_lines, num_columns)
        cmd = self.LCD_FUNCTION
        if num_lines > 1:
            cmd |= self.LCD_FUNCTION_2LINES
        self.hal_write_command(cmd)
        self.hal_backlight_on()

    def hal_write_init_nibble(self, nibble):
        byte = ((nibble >> 4) & 0x0f) << SHIFT_DATA
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

    def hal_backlight_on(self):
        self.i2c.writeto(self.i2c_addr, bytearray([1 << SHIFT_BACKLIGHT]))
        self.backlight = 1

    def hal_backlight_off(self):
        self.i2c.writeto(self.i2c_addr, bytearray([0]))
        self.backlight = 0

    def hal_write_command(self, cmd):
        byte = ((self.backlight << SHIFT_BACKLIGHT) | (((cmd >> 4) & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        byte = ((self.backlight << SHIFT_BACKLIGHT) | ((cmd & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        if cmd <= 3:
            sleep_ms(5)

    def hal_write_data(self, data):
        byte = (MASK_RS | (self.backlight << SHIFT_BACKLIGHT) |
                (((data >> 4) & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        byte = (MASK_RS | (self.backlight << SHIFT_BACKLIGHT) |
                ((data & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

