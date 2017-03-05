class clsLocation:
    #this class provides the support for enumerated locations
    ROOM=0
    DOOR=1
    WALL=2

#some more changes went here before the start of the service
#
#

#this branch is called development 01
#this is another branch here


class clsPlayerState:
    #this class provides the functions to support the player state

    #define class based variables; common to all instances
    __playerCount=0 #create a common variable; use '__' to hide the variable


    def __init__(self, startState):
        #this function is automatically executed when a new class instance is created
        clsPlayerState.__playerCount+=1 #increase the hidden player count

        #define instance variables, specific to single instance
        self.location=startState #initialise the stating location

    
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


    def fnDOOR(self):
        #describe the location
        print("You are at the door")        


    def fnWALL(self):
        #describe the location
        print("You are at the wall")



#begin the main code
insPlayer=clsPlayerState(clsLocation.ROOM) #initialise the player instance using the class
insPlayer.fnUpdate()
