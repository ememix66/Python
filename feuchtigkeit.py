#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import sys
import Adafruit_DHT


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
	print("##########################################################################")
	print("#					MENU			        #")
	print("#Taste druecken				|				#")				
	print("#1 = 1. Relais 2 sek. ausschalten	|				#")
	print("#2 = 2. Relais 2 sek. ausschalten	|				#")
	print("#3 = 3. Relais 2 sek. ausschalten	|				#")
	print("#4 = 4. Relais 2 sek. ausschalten	|				#")
	print("#8 = Temperatur & Luftfeuchtigkeit	|				#")
	print("#9 = IP Adressen checken		1	|				#")
	print("#0 = Programm verlassen			|				#")
	print("##########################################################################")

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

def ping():
	ip = "localhost"
	if os.system("ping -c 1 " + ip) == 0:
		time.sleep(1)
		cls()
		print "Die IP Adresse",ip,"ist erreichbar !!!"
		time.sleep(2)
		
	else:
		print "IP ist NICHT erreichbar"
		time.sleep(3)
			



try:
	menu()
	x = int(input("Was soll ich machen ?"))

	while True:
	   if x > 9:
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

	   elif x == 8:
		cls()
	        print("Aktuelle Temperatur und Luftfeuchtigkeit ist:")
		humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
		#print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
		
		if humidity is not None and temperature is not None:
			print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
			
			smtpserver.sendmail(Absender, [Empfaenger], msg.as_string())
			smtpserver.quit()
						
		else:
			print 'Failed to get reading. Try again!'
			

		time.sleep(2)
		menu()
		x = int(input("Was soll ich machen ? "))


	        
	   elif x == 9:


		ping()
		menu()
		x = int(input("Was soll ich machen ? "))

except KeyboardInterrupt:
	print("du hat strg c gedrueckt")

except:
	print ("other error occurred")
finally:
	GPIO.cleanup()
