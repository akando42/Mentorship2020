import numpy as np
from openpyxl import load_workbook
from main import Country
from main import Reader
from main import Reader2
from main import Coordinates

class Main:
    end_game = False

    # Countries Init
    print('Welcome to the the Battle Simulator')
    c1 = Reader.country_init(1)
    c2 = Reader.country_init(2)
    print(c1.ID_TAG)
    print(c2.ID_TAG)

    # Battle Location Init
    print("Select Battle Location")
    battle_loc = Coordinates.Cords()
    loc_type = input("Entering the following number for:\n[0] Custom Location\n[1] Random Location\n")
    if loc_type == 0:
        x = input("Enter x value:\n")
        y = input("Enter y value:\n")
        battle_loc.set_loc(x,y)
    else:
        battle_loc.set_rand_cords()
    print("Battle will take place at: " + battle_loc.get_loc())


    # while(end_game == False):
    #     military_type = input("Entering the following number for:\n[0] Offense\n[1] Defense\n")
    #     if(military_type == '0'):
    #         maneuver = input("Pick one of the following offensive maneuvers: \n[0] Push Middle\n[1] Flank Right\n[2] Flank Left\n[3] Pincer\n[4] Push Equally\n[5]Trap on Two Fronts\n[999] Go back to beginning\n")
    #         if(maneuver == '0'):
    #             print('You tried to push middle\n')
    #         elif (maneuver == '1'):
    #             print('You tried to flank right\n')
    #         elif (maneuver == '2'):
    #             print('You tried to flank left\n')
    #         elif (maneuver == '3'):
    #             print('You tried to do a pincer movement\n')
    #         elif (maneuver == '4'):
    #             print('You tried to push equally on all fronts\n')
    #         elif (maneuver == '5'):
    #             print('You tried to trap the enemy on two fronts\n')
    #         elif(maneuver == '999'):
    #             break
    #         else:
    #             print('Wrong input. Try again.')
    #     if(military_type == '1'):
    #         maneuver = input('Pick one of the following defensive maneuvers:\n[0] Retreat\n[1] Retreating Fire\n[2] Find and Hold a Choke Point\n[3] Turtle')
    #         if (maneuver == '0'):
    #             print('You tried to retreat\n')
    #         elif (maneuver == '1'):
    #             print('You tried to retreat to cover fire\n')
    #         elif (maneuver == '2'):
    #             print('You tried to find and hold a choke point\n')
    #         elif (maneuver == '3'):
    #             print('You tried to create a defensive turtle for a better defense\n')
    #         elif (maneuver == '999'):
    #             break
    #         else:
    #             print('Wrong input. Try again.')
    #     print(moves[int(maneuver)][int(military_type)])
