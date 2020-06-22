'''
Created on Apr 11, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System
'''
import sys
musicFile = 'musicrecplus.txt' 
data = {} 

def menu():
    return '''Enter a letter to choose an option:
r - enter preferences
e - get recommendations
p - show most popular artists
h - how popular is the most popular
m - which user has the most likes
q - save and quit'''

def read(file):
    '''reads from file'''
    F = open(file,'r')
    for line in F:
        if line != '\n' and line != '':
            s = line.strip().split(':')
            name = s[0]
            artists = s[1].split(',')
            data[name] = artists
    F.close()

def write(file):
    '''writes from file'''
    s = ""
    F = open(file, 'w')
    for item in data:
        prefs = ''
        for a in data[item]:
            prefs = prefs + a + ','
        s += item + ":" + prefs[:-1] + "\n"
    F.write(s)
    F.close()

def loadUsers(fileName):
    ''' Stores user names'''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

def getName():
    '''Gets the users name'''
    name = input("Enter username (or E to exit): ")
    name = name.strip()
    name = name.title()
    return name

def getArtists():
    '''Returns list of artists'''
    L = []
    while(1):
        artist = input("Enter artist (or E to exit): ")
        if artist == "E":
            break
        artist = artist.strip().title()
        L += [artist]
    return L

def getPrefs():
    '''Saves input of get artist'''
    read(musicFile)
    while(True):
        name = getName()
        if name == "E":
            return "Done editing preferences."
        else:
            fav_music = getArtists()
            data[name] = fav_music
    write(musicFile)

def numMatches(list1, list2):
    ''' Find matching element count of two lists'''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def findBestUser(currUser, prefs, userMap):
    ''' Return user who matches the closest '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1 '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    while j < len(list2):
        list3.append(list2[j])
        j += 1
    return list3

def getRecommendations(currUser, prefs, userMap):
    '''Gets recommendations using above functions'''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations

def recommendations():
    '''Return recommendations if user is in data, if not gets prefs'''
    user = input("What's your name? \n")
    if user not in data:
        print("We don't have you in the system") 
        return getPrefs()
    else:
        userMap = loadUsers(musicFile)
        return getRecommendations(user, data[user], userMap)

def mode(L):
    '''Find most common element in list'''
    artists = {}
    for item in L:
        if item not in artists: 
            artists[item] = 1
        else: 
            artists[item] += 1
    x = []
    y = []
    for item in artists:
        x += [item]
        y +=[artists[item]]
    return x[y.index(max(y))]

def mostPopular():
    '''Returns artist that appears most in users preferences.'''
    L = []
    for item in data:
        L += data[item]
    return mode(L)
def howPopular():
    '''Returns number of users that likes the most popular artist.'''
    x = 0
    L = []
    for item in data:
        L += data[item]
    for item in L:
        if item == mode(L): 
            x += 1
    return x

def mostLikes():
    '''Return the user that likes the most artists, only if they have not opted out'''
    L = []
    for item in data:
        L += [data[item]]
    L = map(len, L)
    for item in data:
        if max(L) == len(data[item]):
            if item[-1] == '$':
                return 'user opted out'
            else:
                return item

def main():
    '''Initiates the music recommender'''
    read(musicFile)
    while(1):
        print(menu())
        i = input("Choice: ")
        if i == "e":
            print(getPrefs())
        elif i == "r":
            print(recommendations())
        elif i == "p":
            print("The most popular artist is ", mostPopular())
        elif i == "h":
            print("The most popular artists is liked by ", howPopular(), "users")
        elif i == "m":
            if mostLikes() != "user opted out":
                print(mostLikes(), " has the most likes and they like:", data[mostLikes()])
            else:
                print(mostLikes())
        elif i == "q":
            print("Have a nice day!")
            break
        else:
            print("Invalid Choice, try again!")
    write(musicFile)

if __name__ == "__main__": main()