'''A program that randomly assigns a valid number of teams a letter and then organises the 
first round of games
'''
import random

def teams(numberOfTeams):
    #testing if the number of teams are valid
    if numberOfTeams%2 != 0 or numberOfTeams < 4 or numberOfTeams > 20:
        print("The number of teams are invalid for this program")
        exit()

    #initializing some variables
    alphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
    teamList = []
    games = []
    gameCounter = 1

    #assigning each team with an alphabet
    for index in range(numberOfTeams):
        teamList.append(alphabetList[index])
    print(teamList)

    
    #removes teams and pairs them up
    while len(teamList) > 0:
        gameList = []
        
        #chooses a random team and removes it from the teamsList so that it can't be chosen again
        firstTeam = random.randint(0, len(teamList) - 1)
        gameList.append(teamList[firstTeam])
        teamList.pop(firstTeam)

        #chooses a second random team to play in that game. I had to do an if/else due to the
        #random.randint function requiring a range to work
        if len(teamList) == 1:
            gameList.append(teamList[0])
            teamList.pop(0)
        else:
            secondTeam = random.randint(0, len(teamList) - 1)
            gameList.append(teamList[secondTeam])
            teamList.pop(secondTeam)

        games.append(gameList)
    
    #prints out the games list with a game number beside it
    for index in range(len(games)):
        print("Game " + str(gameCounter) + ") " + str(games[index]))
        gameCounter += 1
        
#activating the teams function
teams(20)