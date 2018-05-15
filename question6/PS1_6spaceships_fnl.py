#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:01:15 2018

@author: jenniferlaing


CTA200H 2018
Problem Set #1

Question #6
Program to simulate a space battle

"""
import random
from time import sleep

#At the moment my battle simulation goes on forever. It doesn't recognize
#when a ship is dead and I'm not sure how to make the program reach an ending.
#-----------------------------------------------------

class Spaceship:

    # Constructor
    def __init__(self, name, shields, hull, laser):
        self.name = name
        self.shieldstrength = shields
        self.hullstrength = hull
        self.laserpower = laser
        
    def __str__(self):
        status = "[{}] Shieldstrength: {}, Hullstrength: {}, laser power: {}"
        return status.format(self.name, self.shieldstrength, self.hullstrength,
                            self.laserpower)        

 
    def gethit(self):
        laser = 0.5
        hitDamage = max(self.shieldstrength - laser, 0)

        self.shieldstrength = round(self.shieldstrength - hitDamage, 1)

        if self.shieldstrength <= 0:
            self.hullstrength = round(self.hullstrength - hitDamage, 1)
        elif self.hullstrength <= 0:
            self.is_dead()
            print("CRITICAL HIT!!!!")
        else:
            self.shieldstrength <= 0.5

        
    def is_dead(self):
        return self.hullstrength <= 0
        

    def shoots(self, ship_hit):
        laser = 0.5
        hitDamage = max(ship_hit.shieldstrength - laser, 0)

        ship_hit.shieldstrength = round(ship_hit.shieldstrength - hitDamage, 1)

        if ship_hit.shieldstrength <= 0:
            ship_hit.hullstrength = round(ship_hit.hullstrength - 2*hitDamage, 1)
            print("CRITICAL HIT!!!!")

        else:
            ship_hit.hullstrength <= 0
            ship_hit.is_dead()

        print(self.name, "did", hitDamage, "damage to", ship_hit.name, ".")
        print()
        print()
    
    def battle(self, ship_hit):
        # Choose first shooter randomly
        shooter, defender = (self, ship_hit)

        if not (self.is_dead() or ship_hit.is_dead()):
            print()
            sleep(.7)

            shooter.shoots(defender)

        if defender.is_dead():
            print(defender.name, "Destroyed!")
        else:
            sequence()




    def encounter(self, ship_hit):
        sleep(.7)
        self.battle(ship_hit)
        if self.is_dead():        
            winner = ship_hit.name if self.is_dead() else self.name
            print()
            print()
            print(winner, "is the final victor!")
        elif not self.is_dead():
            print(self)
            

#---


    
#---Subclasses
class Warship(Spaceship):
    def shoots(self, ship_hit):
        missile = 0.75
        hitDamage = max(ship_hit.shieldstrength - missile, 0)

        ship_hit.shieldstrength = round(ship_hit.shieldstrength - hitDamage, 1)

        if ship_hit.shieldstrength <= 0:
            ship_hit.hullstrength = round(ship_hit.hullstrength - 2*hitDamage, 1)
            print("CRITICAL HIT!!!!")
        else:
            ship_hit.hullstrength <= 0
            ship_hit.is_dead()

        print(self.name, "did", hitDamage, "damage to", ship_hit.name, ".")
        print()
        print()
        
class Speeder(Spaceship):
    def gethit(self):
        laser = 0.5
        hitDamage = max(self.shieldstrength - laser/2, 0)

        self.shieldstrength = round(self.shieldstrength - hitDamage, 1)

        if self.shieldstrength <= 0:
            self.hullstrength = round(self.hullstrength - hitDamage, 1)
        elif self.hullstrength <= 0:
            self.is_dead()
            print("CRITICAL HIT!!!!")
        else:
            self.shieldstrength <= 0.5

#Define the ships
ship1 = Spaceship('Prometheus',1,1,1)
ship2 = Spaceship('Andromeda',1,1,1)
ship3 = Spaceship('Pegasus',1,1,1)
ship4 = Warship('Hercules',1,1,1)
ship5 = Speeder('Hero',1,1,1)

#Program
#Randomly choose a ship
#shoot (not at self or dead ship)
#make status update and log
#loop until one ship left

def sequence():
    #Randomly choose a ship
    shiplist = [ship1, ship2, ship3, ship4, ship5]
    name1 = random.choice(shiplist)
#    name1_string = '' + name1 + ''
    shiplist.remove(name1)

    name2 = random.choice(shiplist)
    
    ship_shoots = name1
    print(ship_shoots)

    while not ship_shoots.is_dead():
        ship_hit = name2
        print(ship_hit)

        ship_shoots.encounter(ship_hit)

if __name__ == "__main__":
    sequence()
