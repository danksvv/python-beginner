from random import randint
from os import system
from time import sleep
import sys
import time


# Function to clear the screen
def clearAndSleep(delay=5):
    sleep(delay)
    system('clear')


# Function to print the welcome message

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after finishing


# message to welcome the user


print("""
                                                                         
     ▗▄▄▖▗▄▄▄▖▗▄▄▖ ▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖    ▗▄▄▄▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖ 
    ▐▌     █  ▐▌ ▐▌▐▌   ▐▌     █      ▐▌     █  ▐▌   ▐▌ ▐▌  █  ▐▌   ▐▌ ▐▌
     ▝▀▚▖  █  ▐▛▀▚▖▐▛▀▀▘▐▛▀▀▘  █      ▐▛▀▀▘  █  ▐▌▝▜▌▐▛▀▜▌  █  ▐▛▀▀▘▐▛▀▚▖
    ▗▄▄▞▘  █  ▐▌ ▐▌▐▙▄▄▖▐▙▄▄▖  █      ▐▌   ▗▄█▄▖▝▚▄▞▘▐▌ ▐▌  █  ▐▙▄▄▖▐▌ ▐▌
                                                                         
                                                                         
""")

clearAndSleep()


message = "Welcome to Street Fighter! The game where you fight to the death! \n" \
    "Before starting you will have to choose the character that will lead you to victory! \n"


typewriter(message, delay=0.05)

character = 0

while character not in [1, 2, 3, 4]:

    message = "Choose between this 4 characters: \n" \
        "1. Ryu \n" \
        "2. Ken \n" \
        "3. Chun-Li \n" \
        "4. Guile \n"

    typewriter(message, delay=0.05)

    character = int(input("Choose your character (1,2,3,4): "))
    clearAndSleep(1)

if character == 1:
    print("""

                             YOdhhkhdbkz                               
                        ^bhhhhhhhhhhhhhhhhhk                           
                         {hhhhhhhhhhhhhhhhhww                          
                       hhkhkbwhn hhC  bO Chhhh                         
                         whk p`  hOd0hd    hhhd                        
                        p hkb   thhh   kbX   dh                        
                         khhhb  hhhd k  lhb.hmh                        
                          'hhh           hhw kh                        
                           wh             dhhdh>                       
                           hhhhh          > whhx d                     
                           hhhh,         "hhhh  dhb                    
                            hph<        dhkY h  C c                    
                         kkdkhhh      kdhh   d hkk                     
              I          hhhhhhhhbmdhhhhhh   bhhh                      
     whhhZ      d"kkhhhhhmhhwd Owhhhhhhh p   h h                       
     Ohhhhhbhdhhmhh   hhp  hk     hhhhkh h   h0       h                
     -hhhhhhhhhhhhhhhhhhd C  ;X     whb! h   hhhhh     ,               
       hhhhhhhhhhhhhk       k  hY    hhh h h!bhhhhb J  hb              
     hhhhhhhh     Qwhhdf     ;k  kw    dkh hhdkhhkhhXhd dh zw          
   hhhhhhhhhh          Qk      p  wth    khr       hd b  h k   b       
    khhhhhhhh            h      h  pb     bk       Ohd k   Z )^ Od     
   bhhhhhhhhhh         .thh           Ob  h <       bmd Y      _ _b    
  Obhhhhhhhhhh  k        hw            bh    ,       hh C   k`hh   }   
    hhhhhhhhhhdphd      bd        k  h  k-    i       k      k h"  d   
  hhhhhhhO  Xhhhhhhhkkhhhhhdd    hh   m   h    h      hb z    Z'hh hd  
hhhhhhhkQ    khhhhhhhhhhhhO     hhh   hh Z k  |_     hhb n     hhhddhw 
khhhhhhd      bhhhhhhhhhhhl   OhhQ    hh       Xh    hhh !      hhhb  h
 hhhhhhX         hbhhhhhhwhhOhhhm     hI  z      w]whhhh      < hhhh   
 hhhhhhk          khhhhhhhhhhhhk      Z   p       dhhhhh      hhhhkhh  
 hhhhhhk      c  hbh Ihhhhhhhh                m  } hhhhh  k   ph b Xd  
 hhhhhhQ dh   khhpk  +hhhhhhi                k    rmhhhk  hbhdhh>p     
 hhhhhhhhh    khhk   bhhhhhk                   c    khh   Zhhhhhw      
 hhhhhhhhh    hhh   dhhhhhhh           k      b    k hh    bhhhhkZk    
hhhhhhhhhh    dh    bhhhhhhhh        hk         t    hh   hmhhhhhhw  h 
bhhhhhhhhh    bhhhhhhhhhhhhhhhhhddbhhkh    p        OZ   hhhk`  bphhhhh
dhhhhhhhhhb  lhhhhhhhhhhhhhhhhhhhhhhhk    hk   d    h(   dhh     whhhhhk
          """)
    message = "You have chosen Ryu! \n"
    message += "Ryu is a Japanese martial artist who travels the world to improve his skills. \n"

    typewriter(message, delay=0.05)
