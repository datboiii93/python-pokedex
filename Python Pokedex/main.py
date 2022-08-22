#from PIL import Image
import mysql.connector
import requests
import json
import os
#from io import BytesIO

mydb = mysql.connector.connect(
    host = "localhost",
    user="test",
    password="testdasql",
    database="mydatabase"
)

mycursor = mydb.cursor()


os.system('cls')
response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151")
poke = response.json()

pokeParty = []

#Set a list of all pokemon for later search
print("Starting program")
pokeList = []
for x in poke['results']:
    pokeList.append(x['name'])
print("\n Welcome to the Python Pokedex!")
username = input("What is your name? ")
userdex = username.lower() + "dex"
print(userdex)

#Check if table exists
stmt = "SHOW TABLES LIKE '{0}'".format(userdex)
mycursor.execute(stmt)
result = mycursor.fetchone()
if result:
    print("Welcome back, ", username, "!")
    #exists = True
else:
    print("No pokedex found - creating pokedex.")
    mycursor.execute(f"CREATE TABLE {userdex} (number VARCHAR(255), name VARCHAR(255))")
    print(f"Created pokedex for {username}")


#Prints the Pokemon party nicely
def NicePokeParty():
    print("\n Your current party is:")
    for p in pokeParty:
        print(p)
    if len(pokeParty) == 0:
        print("No pokemon in party yet")

#Prompts the user on the main menu
def WhatDo():
    print("\n What would you like to do?")
    print("1 - See all Pokemon")
    print("2 - add a Pokemon to your party")
    if (len(pokeParty) > 0):
        print("3 - take a Pokemon from your party")
    print("Exit - Exit the program")
    
#Displays all 151 pokemon (we're purists here)
def PrintAll():
    i = 0
    for x in poke['results']:
        i+=1
        print(i, "\t", x['name'])

def Praise():
    #os.system('cls')
    print("All hail Bidoof!")
    print("""\
                                                                                        
                                                                                
                                                          .%@&@/                
                                                       &///*///////(            
                                              .((#((##//////////////(           
                                              %#((((((/////////////&#////#.     
                                      /&(*///////////%&#/////////(//////((((,   
              /#***%           ,&///////////////////////////&(//(///////(((((   
           *********/&      %///////////////////(%#(/////////////(//////((((#   
          ,//////////,  ./&&%&%%#(//////////&/*/******%////////////%(((((##%    
          .((//////(*///**/******//////%///(////*//////(/////////////(&         
             &%**********************//////(///////((((//////////////(///       
           ./*******/%,.......#//*///////////(#((#%#//////////////((((((((%     
         .////***//#.............%//////////////@/(////(/(/(((((((((((((((((    
        */*////...................(/...,#/////////(((((((((((((((((((((((((/(,  
    *(%%////(............................(/////////(((((((((((((((((((((((((((* 
 ,******///#..(@@/.................(@@/...(///////****/*%/(((((((((((((((((((((.
 //****////(...,,..*%%(((((##%&#*.,./,....#////////***////@(((((((((((((((((((((
 %//////////%.*&((((#,//&(((####%%#%%....#////////////////%((((((((((((#(//((((#
   ,#///////&#(((((#####%##(#####%%%%%%&/(//////////////##((//////((((((((/((((#
 (/////////@#((((((((((######%%%%%%%%%#%&//////////////(//////////((((#((((##(#%
///////////%%%#%#######%%%%%%%%%%%%%%%%%%((//////////(((%((((((((((#%##########%
 &///////((/%&%%#%%%%%%%#%#######%#%%%%%&(((((((((((((((&########%(&#%%%%%%###% 
    .#((((((((&&&%%%%@**(&%%%%%%%@%%%%@((((((((((((((###%%#%&#(/(@%%%%%%%%####  
    *((((((((((((#          .  .##(((((((((((((((%%%%%#%%((((%,    #%%%%%%#%    
     @(((###((((((.            ,(((((((((((((((((%%%%##@&.          &&&&&%&@    
        ...#(((((#&     *      @((((((((((((((((%%%##%             /* *&&( *@   
            #((((((((#%&@&&&&&&(((((((((%%%%%%%%#%#%.                           
             *&@(((%@.        *(((((((&  #%%%%%#@*                              
               (%,  (.                   %&&&&&&&%%                             
                                             .                                  
                                                                                

        """)

#Add a pokemon to the user's party
def AddPoke():
    add = input("\n Which pokemon would you like to add to your party? (name or number)")
    if add in pokeList:
        pokeParty.append(add)
    else:
        print("Not found in pokedex - please try again")

#Remove a pokemon from a user's party
def RemovePoke():
    print("\n Remove from your party")
    rem = input("\n Which pokemon would you like to remove from your party? (name or number)")
    if rem in pokeParty:
        pokeParty.remove(rem)
    else:
        print("Not found in Party - please try again")


def main():
    while True:
        NicePokeParty()
        WhatDo()
        ans = input("\n Type a number: ")
        if ans == "1":
            PrintAll()
        elif ans == "2":
            AddPoke()
        elif ans == "3":
            RemovePoke()
        elif ans == "praise":
            Praise()
        elif ans == "Exit" or ans == "exit" or ans == "e":
            exit()
    
main()
