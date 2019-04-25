#!/usr/bin/env python
 #-*- coding: utf-8 -*-
import time
#using the web library 
import web
# input output library 
import RPi.GPIO as GPIO


# L293D pins with raspberry
Motor1A = 20
Motor1B = 21
Motor2A = 26
Motor2B = 19

#using bcm mode
GPIO.setmode(GPIO.BCM)


GPIO.setwarnings(False) 

#set pins as outputs

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)

 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)





#function for forward the robot

def avancer ():
     print("avancer")
     GPIO.output(Motor2A,GPIO.HIGH)
     GPIO.output(Motor2B,GPIO.LOW)
     GPIO.output(Motor1A,GPIO.LOW)
     GPIO.output(Motor1B,GPIO.HIGH)
     
    

#backward the robot
def arriere():
     print("arriere")
     
     GPIO.output(Motor2A,GPIO.LOW)
     GPIO.output(Motor2B,GPIO.HIGH)
     GPIO.output(Motor1A,GPIO.HIGH)
     GPIO.output(Motor1B,GPIO.LOW)
# Right
def adroite():
    print("adroite")
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    
 #left
def agauche():
    print("agauche")
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    
    
    
 #stop 
def stop():
    print("stop")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
  

                       

            
# definit la page de nom index pour le site web 





urls = ('/','myrobot')

app = web.application(urls, globals())

class myrobot:
  

    # recieve a request from client 
    def POST(self):
        
        userdata = web.input()                
        if hasattr(userdata,'direction'):
            if userdata.direction == 'avant':
                avancer()
            elif userdata.direction == 'gauche':
                agauche()         
            elif userdata.direction == 'droite':
                adroite()      
            elif userdata.direction == 'arriere':
                arriere()
            elif userdata.direction == 'stop':
                stop()
        

# programme 
if __name__ == '__main__':
    #run the server instance
    app.run()    

                  
