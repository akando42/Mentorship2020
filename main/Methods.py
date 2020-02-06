def prob(self, c):
    prob = (self.GDPc * c.GDP) + (self.ARMYc * self.armyCommitments) + (self.NAVYc * self.navyCommitments) + (
                self.AFc * self.afCommitments) + (self.NC * self.ncCommitments)
    prob *= self.maneuvers[self.move_player][self.move_comp]
    return prob


def winner(a, b):
    if (b != 0):
        return 100 * (a / b)
    else:
        return print("Error")


def getUserMoves(n):
    n = 1
    move_player = -1
    military_type = input("Entering the following number for:\n[0] Offense\n[1] Defense\n")
    if (military_type == '0'):
        maneuver = input(
            "Pick one of the following offensive maneuvers: \n[0] Push Middle\n[1] Flank Right\n[2] Flank Left\n[3] Pincer\n[4] Push Equally\n[5]Trap on Two Fronts\n[999] Go back to beginning\n")
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
    if (int(ARMY) < c.ARMY_ASSETS):
        return int(ARMY)


def getNavyResources(c):
    NAVY = input("Enter number of navy assets between 0 and " + str(c.NAVY_ASSETS) + "\n")
    if (int(NAVY) < c.NAVY_ASSETS):
        return int(NAVY)


def getAFResources(c):
    AF = input("Enter number of air force assets between 0 and " + str(c.AIR_FORCE_ASSETS) + "\n")
    if (int(AF) < c.AIR_FORCE_ASSETS):
        return int(AF)


def getNCResources(c):
    NC = input("Enter number of nuclear assets between 0 and " + str(c.NUCLEAR_CAPABILITIES) + "\n")
    if (int(NC) < c.NUCLEAR_CAPABILITIES):
        return int(NC)