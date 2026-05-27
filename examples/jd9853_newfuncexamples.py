from machine import Pin, SPI
import jd9853
import tft_config
import time
# Inicializar display
display = tft_config.config(0, buffer_size=0)
display.init()
display.fill(jd9853.BLACK)

# Degradado
#display.gradient_fill(0, 0, 240, 60, jd9853.RED, jd9853.BLUE, jd9853.GRADIENT_HORIZONTAL)

# Rectángulo redondeado
#display.round_rect(10, 70, 100, 50, 10, jd9853.YELLOW)

# Triángulo relleno
#display.fill_triangle(120, 100, 180, 150, 120, 150, jd9853.GREEN)
# Triangle with vertices at (50,50), (100,100), (0,100)
#display.triangle(70, 250, 100, 100, 0, 100, jd9853.PINK)

# Elipse
#display.fill_ellipse(50, 50, 30, 20, jd9853.CYAN)

#display.ellipse(100, 200, 30, 20, jd9853.RED)
#display.fade_out(30, 500)
for i in range(0,255):
    display.contrast(i) # Increase the contrast
    time.sleep(2000)
#display.contrast(100)  # Decrease the contrast
#time.sleep(30)
#display.contrast(255)

# Icon 16x16 (32 bytes: 16 filas * 2 bytes per row)
"""icon = bytes([
    0x00, 0x00,  # Row 0
    0x00, 0x00,  # Row 1
    0x00, 0x00,  # Row 2
    0x0C, 0x00,  # Row 3
    0x1E, 0x00,  # Row 4
    0x3F, 0x00,  # Row 5
    0x7F, 0x80,  # Row 6
    0xFF, 0xC0,  # Row 7
    0xFF, 0xC0,  # Row 8
    0x7F, 0x80,  # Row 9
    0x3F, 0x00,  # Row 10
    0x1E, 0x00,  # Row 11
    0x0C, 0x00,  # Row 12
    0x00, 0x00,  # Row 13
    0x00, 0x00,  # Row 14
    0x00, 0x00,  # Row 15
])
display.draw_icon(icon, 70, 250, 16, jd9853.RED)
# Obtener información
info = display.get_info()
print(info)
"""