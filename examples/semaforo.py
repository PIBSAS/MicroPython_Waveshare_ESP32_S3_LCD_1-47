import jd9853 as jd
import tft_config
import vga1_16x16 as fuente
lcd = tft_config.config(3)
T = "Elias Monzon"
lcd.init()

lcd.fill(jd.GRAY)
#lcd.text(fuente,T,320//2 - 8*len(T),170//2 - 8)

#lcd.vline(320//2,0,170,jd.BLACK)
#lcd.hline(0,170//2,320,jd.BLACK)
lcd.pixel(320//2,170//2,jd.BLUE)
lcd.vline(320//2+50,170//2-3,6,jd.BLUE)
lcd.fill_ellipse(320//2,170//2,50,50,jd.YELLOW)
lcd.fill_ellipse(320//2+105,170//2,50,50,jd.RED)
lcd.fill_ellipse(320//2-105,170//2,50,50,jd.GREEN)
lcd.rect(0,20,320,170-40,jd.YELLOW)