import numpy as np
from openpyxl import load_workbook
from main import Country
from main import Reader
#from main import Reader2
from main import Coordinates


class Main(object):
    def __init__(self):
        n = 4
    def prob(self):
        prob = (self.ARMYc*self.armyCommitments) + (self.NAVYc*self.navyCommitments) + (self.AFc*self.afCommitments) + (self.NC*self.ncCommitments)
        return prob
    def winner(self,a,b):
            return 10000*(a/b)-50
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

    def getArmyResources(self,c):
        ARMY = input("Enter number of army assets between 0 and " + str(c.ARMY_ASSETS) + "\n")
        if(int(ARMY) < c.ARMY_ASSETS):
            return int(ARMY)
    def getNavyResources(self,c):
        NAVY = input("Enter number of navy assets between 0 and " + str(c.NAVY_ASSETS) + "\n")
        if(int(NAVY) < c.NAVY_ASSETS):
            return int(NAVY)
    def getAFResources(self,c):
        AF = input("Enter number of air force assets between 0 and " + str(c.AIR_FORCE_ASSETS) + "\n")
        if(int(AF) < c.AIR_FORCE_ASSETS):
            return int(AF)
    def getNCResources(self,c):
        NC = input("Enter number of nuclear assets between 0 and " + str(c.NUCLEAR_CAPABILITIES) + "\n")
        if(int(NC) < c.NUCLEAR_CAPABILITIES):
            return int(NC)
    # Game coefficients (subject to change as testing goes on)
    GDPc = 1
    ARMYc = .654
    NAVYc = 1
    AFc = 1
    MPc = 1
    NC = 0
    # Defines variable committed resources
    armyCommitments = 0
    navyCommitments = 0
    afCommitments = 0
    ncCommitments = 0
    # Sets up maneuver matrix
    maneuvers = np.zeros((11, 11))
    wb = load_workbook('MilitaryTactics.xlsx')
    source = wb.active
    ws = wb.copy_worksheet(source)
    for i in range(1, 11):
        for j in range(1, 11):
            maneuvers[i][j] = ws.cell(row=i, column=j).value
        # Records moves of both players to determine win probability
        move_player = 0
        move_comp = 0
class Main:

    M1 = Main()
    #Starts the game
    end_game = False
    # Countries Init
    print('Welcome to the the Battle Simulator')
    c1 = Reader.country_init(1)
    c2 = Reader.country_init(2)
    print("You have chosen to be " + c1.ID_TAG)
    print("Your opponent is " + c2.ID_TAG)
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
    print(M1.maneuvers[0][0])
    while (end_game == False):
        move_comp = np.random.uniform(0, 9)
        #Gets user move
        move_player = M1.getUserMoves()
        #Gets how much the user wants to commit
        M1.armyCommitments = M1.getArmyResources(c1)
        M1.navyCommitments = M1.getNavyResources(c1)
        M1.afCommitments = M1.getAFResources(c1)
        M1.ncCommitments = M1.getNCResources(c1)
        print("You committed " + str(M1.armyCommitments) + " ground units\n",
              "You committed " + str(M1.navyCommitments) + " naval units\n",
              "You committed " + str(M1.afCommitments) + " air units\n",
              "You committed " + str(M1.ncCommitments) + " nuclear missiles\n",
              "")
        p1 = M1.prob()
        print(M1.armyCommitments)
        print(M1.navyCommitments)
        #Set random values for computer
        M1.armyCommitments = int(np.random.uniform(0, c2.ARMY_ASSETS))
        M1.navyCommitments = int(np.random.uniform(0, c2.NAVY_ASSETS))
        M1.afCommitments = int(np.random.uniform(0, c2.AIR_FORCE_ASSETS))
        M1.ncCommitments = int(np.random.uniform(0, c2.NUCLEAR_CAPABILITIES))
        print(M1.armyCommitments)
        print(M1.navyCommitments)
        #player win percentage
        p2 = M1.prob()
        winner = M1.winner(p1,p2)
        print("There is an " + str(winner) +" percent of you winning")