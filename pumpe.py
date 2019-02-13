import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.output(17,True)
GPIO.output(18,True)
GPIO.output(22,True)
GPIO.output(23,True)



def menu():
	cls()
	print("1 = 1. Relais 2 sek. ausschalten "\n" 2 = 2. Relais 2 sek. ausschalten /n 0 = Programm beenden")
	

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

try:
	menu()
	x = int(input("Was soll ich machen ?"))

	while True:
	   if x > 4:
	   	print("Die Eingabe war ungueltig")
		time.sleep(1)
		menu()
	   	x = int(input("Was soll ich machen ? "))
	        
       	   elif x == 0:
        	break

	   elif x == 1:
	        print("Ich schalte Ralais 1 fuer 2 Sekunden aus")
	        GPIO.output(17, False)
	        time.sleep(2)
		GPIO.output(17, True)
		menu()
		x = int(input("Was soll ich machen ? "))
	        
	   elif x == 2:
	        print("Ich schalte Ralais 2 fuer 2 Sekunden aus")
	        GPIO.output(18, False)
	        time.sleep(2)
		GPIO.output(18, True)
	        menu()
		x = int(input("Was soll ich machen ? "))
	   elif x == 3:
	        print("Ich schalte Ralais 3 fuer 2 Sekunden aus")
	        GPIO.output(22, False)
	        time.sleep(2)
		GPIO.output(22, True)
	        menu()
		x = int(input("Was soll ich machen ? "))
	   elif x == 4:
		cls()
	        print("Ich schalte Ralais 4 fuer 2 Sekunden aus")
	        GPIO.output(23, False)
	        time.sleep(2)
		GPIO.output(23, True)
	        menu()
		x = int(input("Was soll ich machen ? "))



except KeyboardInterrupt:
	print("du hat strg c gedrueckt")

except:
	print ("other error occurred")
finally:
	GPIO.cleanup()
