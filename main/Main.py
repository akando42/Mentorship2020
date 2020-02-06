import numpy as np
from openpyxl import load_workbook
from main import Country
from main import Reader
from main import Reader2
from main import Coordinates

class Main:
    # Game coefficients
    GDPc = .01
    ARMYc = .01
    NAVYc = .01
    AFc = .01
    MPc = .01
    NC = .01
    def __init__(self):
        n =4
    def prob(Main,c):
        prob = (Main.GDPc*c.GDP) + (Main.ARMYc*Main.armyCommitments) + (Main.NAVYc*Main.navyCommitments) + (Main.AFc*Main.afCommitments) + (Main.NC*Main.ncCommitments)
        prob *= Main.maneuvers[Main.move_player][Main.move_comp]
        return prob
    def winner(a,b):
        if(b != 0):
            return 100*(a/b)
        else:
            return print("Error")
    def getUserMoves(n):
        n = 1
        move_player = -1
        military_type = input("Entering the following number for:\n[0] Offense\n[1] Defense\n")
        if (military_type == '0'):
            maneuver = input("Pick one of the following offensive maneuvers: \n[0] Push Middle\n[1] Flank Right\n[2] Flank Left\n[3] Pincer\n[4] Push Equally\n[5]Trap on Two Fronts\n[999] Go back to beginning\n")
            if (maneuver == '0'):
                print('You tried to push middle\n')
                move_player = 0
            elif (maneuver == '1'):
                print('You tried to flank right\n')
                move_player = 1
            elif (maneuver == '2'):
                print('You tried to flank left\n')
                move_player = 2
            elif (maneuver == '3'):
                print('You tried to do a pincer movement\n')
                move_player = 3
            elif (maneuver == '4'):
                print('You tried to push equally on all fronts\n')
                move_player = 4
            elif (maneuver == '5'):
                print('You tried to trap the enemy on two fronts\n')
                move_player = 5
            elif (maneuver == '999'):
                print("Return to beginning")
            else:
                print('Wrong input. Try again.')
        if (military_type == '1'):
            maneuver = input(
                'Pick one of the following defensive maneuvers:\n[0] Retreat\n[1] Retreating Fire\n[2] Find and Hold a Choke Point\n[3] Turtle')
            if (maneuver == '0'):
                print('You tried to retreat\n')
                move_player = 6
            elif (maneuver == '1'):
                print('You tried to retreat to cover fire\n')
                move_player = 7
            elif (maneuver == '2'):
                print('You tried to find and hold a choke point\n')
                move_player = 8
            elif (maneuver == '3'):
                print('You tried to create a defensive turtle for a better defense\n')
                move_player = 9
            elif (maneuver == '999'):
                print("Return to beginning")
            else:
                print('Wrong input. Try again.')
        return move_player

    def getArmyResources(c):
        ARMY = input("Enter number of army assets between 0 and " + str(c.ARMY_ASSETS) + "\n")
        if(int(ARMY) < c.ARMY_ASSETS):
            return int(ARMY)
    def getNavyResources(c):
        NAVY = input("Enter number of navy assets between 0 and " + str(c.NAVY_ASSETS) + "\n")
        if(int(NAVY) < c.NAVY_ASSETS):
            return int(NAVY)
    def getAFResources(c):
        AF = input("Enter number of air force assets between 0 and " + str(c.AIR_FORCE_ASSETS) + "\n")
        if(int(AF) < c.AIR_FORCE_ASSETS):
            return int(AF)
    def getNCResources(c):
        NC = input("Enter number of nuclear assets between 0 and " + str(c.NUCLEAR_CAPABILITIES) + "\n")
        if(int(NC) < c.NUCLEAR_CAPABILITIES):
            return int(NC)
    #Defines variable committed resources
    armyCommitments = 0
    navyCommitments = 0
    afCommitments = 0
    ncCommitments = 0
    #Starts the game
    end_game = False
    # Countries Init
    print('Welcome to the the Battle Simulator')
    c1 = Reader.country_init(1)
    c2 = Reader.country_init(2)
    print("You have chosen to be " + c1.ID_TAG)
    print("Your opponent is " + c2.ID_TAG)
    # Records moves of both players to determine win probability
    move_player = 0
    move_comp = 0
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
    print("Battle will take place at: " + str(battle_loc.get_loc()))

    while (end_game == False):
        move_comp = np.random.uniform(0, 9)
        #Gets user move
        move_player = getUserMoves(1)
        #Gets how much the user wants to commit
        armyCommitments = getArmyResources(c1)
        navyCommitments = getNavyResources(c1)
        afCommitments = getAFResources(c1)
        ncCommitments = getNCResources(c1)
        print("You committed " + str(armyCommitments) + " ground units\n",
              "You committed " + str(navyCommitments) + " naval units\n",
              "You committed " + str(afCommitments) + " air units\n",
              "You committed " + str(ncCommitments) + " nuclear missiles\n",
              "")
        #Set random values for computer
        a1 = int(np.random.uniform(0, c2.ARMY_ASSETS))
        a2 = int(np.random.uniform(0, c2.NAVY_ASSETS))
        a3 = int(np.random.uniform(0, c2.AIR_FORCE_ASSETS))
        a4 = int(np.random.uniform(0, c2.NUCLEAR_CAPABILITIES))
        #player win percentage
        p1 = prob(c1)
        p2 = prob(c2)

        winner = winner(p1,p2)
        print("There is an " + str(winner) +" of you winning")