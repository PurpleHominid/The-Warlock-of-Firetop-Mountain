class clsLocation:
    #this class provides the support for enumerated locations
    ROOM=0
    DOOR=1
    WALL=2



class clsPlayerState:
    #this class provides the functions to support the player state

    #define class based variables; common to all instances
    __playerCount=0 #create a common variable; use '__' to hide the variable


    def __init__(self, startState):
        #this function is automatically executed when a new class instance is created
        clsPlayerState.__playerCount+=1 #increase the hidden player count

        #define instance variables, specific to single instance
        self.location=startState #initialise the stating location


    def fnLocation(self, newLocation):
        #update the current location
        self.location=newLocation

    
    def fnUpdate(self):
        #this function updates the players state
        if self.location==clsLocation.ROOM: #at the room
            self.fnROOM() #create options for room
        elif self.location==clsLocation.DOOR: #at the door
            self.fnDOOR() #create options for door
        elif self.location==clsLocation.WALL: #at the wall
            self.fnWALL() #create options for wall


    def fnROOM(self):
        #describe the location
        print("You are at the room")
        #define the options
        while True:
            print("\nOptions available:\n'D' to move to the door\n'W' to move to the wall")
            choice=input("\nPlease enter your option: ")
            if choice=="D":
                self.location=clsLocation.DOOR
                break
            elif choice=="W":
                self.location=clsLocation.WALL
                break


    def fnDOOR(self):
        #describe the location
        print("You are at the door")
        #define the options
        while True:
            print("\nOptions available:\n'R' to move to the room\n'W' to move to the wall")
            choice=input("\nPlease enter your option: ")
            if choice=="R":
                self.location=clsLocation.ROOM
                break
            elif choice=="W":
                self.location=clsLocation.WALL
                break     


    def fnWALL(self):
        #describe the location
        print("You are at the wall")
        #define the options
        while True:
            print("\nOptions available:\n'R' to move to the room\n'D' to move to the door")
            choice=input("\nPlease enter your option: ")
            if choice=="R":
                self.location=clsLocation.ROOM
                break
            elif choice=="D":
                self.location=clsLocation.DOOR
                break



#begin the main code
insPlayer=clsPlayerState(clsLocation.ROOM) #initialise the player instance using the class

insPlayer.fnLocation(clsLocation.WALL) #update the players location
insPlayer.fnUpdate()

insPlayer.fnUpdate()

print("Thanks for playing...")
