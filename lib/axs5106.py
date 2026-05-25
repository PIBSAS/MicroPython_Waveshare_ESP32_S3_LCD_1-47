from machine import I2C
import time

_AXS5106_ADDR = 0x63
_TOUCH_REG = 0x01
_ID_REG = 0x08
_MAX_TOUCH = 5
_BUF_SIZE = 14


class AXS5106:
    def __init__(self, i2c, address=_AXS5106_ADDR, reset=None, rotation=0, width=240, height=240, debug=False):
        self.i2c = i2c
        self.addr = address
        self.reset = reset
        self.rotation = rotation
        self.width = width
        self.height = height
        self.debug = debug

        if self.reset:
            self.reset.value(0)
            time.sleep_ms(200)
            self.reset.value(1)
            time.sleep_ms(300)

        # test chip
        try:
            self._read(_ID_REG, 3)
        except:
            if self.debug:
                print("AXS5106 not responding")

    def touched(self):
        data = self._read(_TOUCH_REG, _BUF_SIZE)
        return data[1]

    def touches(self):
        data = self._read(_TOUCH_REG, _BUF_SIZE)

        count = data[1]
        if count == 0:
            return []

        points = []

        for i in range(min(count, _MAX_TOUCH)):
            offset = 2 + i * 6

            x = ((data[offset] & 0x0F) << 8) | data[offset + 1]
            y = ((data[offset + 2] & 0x0F) << 8) | data[offset + 3]

            x, y = self._rotate(x, y)

            points.append({
                "x": x,
                "y": y,
                "id": i
            })

        return points

    def _rotate(self, x, y):
        if self.rotation == 1:
            x = self.width - x
        elif self.rotation == 2:
            y = self.height - y
        elif self.rotation == 3:
            x = self.width - x
            y = self.height - y

        return x, y

    def _read(self, reg, n):
        self.i2c.writeto(self.addr, bytes([reg]))
        return self.i2c.readfrom(self.addr, n)