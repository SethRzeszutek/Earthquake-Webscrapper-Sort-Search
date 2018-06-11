'''
 Name of file: Rzeszutek_ch011_2

 Purpose: To complete the purpose of exercise 11.2.6

 Author: Seth A. Rzeszutek

 Date Created: Oct. 24th, 2017
'''


# all import statements
import csv
import urllib.request as web
import ssl
import timeit
# all functions, each function has a docstring


def queryQuakes(ids, data):
    '''
    Purpose: To search and list the data based on user input
    :param ids: List of Ids to be used
    :param data: Full list of data
    :return: NONE
    '''
    key = input('Earthquake ID (q to quit): ')
    while key != 'q':
        sorteddata=sorted(data, key=lambda x: x[11])        #sorts the list using the native Timsort in python by the 11th column in the data
                                                            #The lambda anonymous function was neccessary in order to sort based off of that column

        sortedIds = sorted(ids)                             #This sorts the list alphabetically using Timsort
        if key == 'list':
            x=0
            print("    ID                Location               Magnitude    Depth" + '\n' + "----------     ----------------------        ---------    -----")
            for i in range(len(ids)):                       #Nice pretty formatting
                print('{:<15s} {:<30s} {:<10s} {:<10s}'.format(sorteddata[x][11], str(", ".join(sorteddata[x][1:3])),str(sorteddata[x][4]),str(sorteddata[x][3])) )
                x+=1
            print("----------     ----------------------        ---------    -----" + '\n')
        else:
            index = binarySearch(sortedIds, key, 0, len(ids) - 1)           #Calls the binary search
            if index >= 0:                                  #Checks index then displaus the data associated in that index
                print('Location: ' + str(", ".join(sorteddata[index][1:3])) + '\n' +
                      'Magnitude: ' + str(sorteddata[index][4]) + '\n' +
                      'Depth: ' + str(sorteddata[index][3]) + '\n')
            else:
                print('An earthquake with that ID was not found.')
        key = input('Earthquake ID (q to quit): ')


def binarySearch(keys, target, left, right):
    """Recursively find the index of target in a sorted list of keys.

    Parameters:
        keys: a list of key values
        target: a value for which to search

    Return value:
        the index of an occurrence of target in keys
    """
    if left > right:              # base case 1: not found
        return -1
    mid = (left + right) // 2
    if target == keys[mid]:       # base case 2: found
        return mid
    if target < keys[mid]:        # recursive cases
        return binarySearch(keys, target, left, mid - 1)  # 1st half
    return binarySearch(keys, target, mid + 1, right)     # 2nd half



def getDataWeb():
    '''
    Purpose: Get data from url
    :return: A list of IDs and a list of all the data
    '''

    # This restores the same behavior as before.
    context = ssl._create_unverified_context()          #Mac needs this in order to read the website might be because it is .gov
    website = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv"
    website_data = web.urlopen(website, context = context)
    csv_file = csv.reader(website_data.read().decode('utf-8').splitlines())
    data = [row for row in csv_file]                    #puts the lines from teh csv file into the data
    IDs = []
    print(data[1][11])
    data.pop([0][0])                                    #gets rid of the titles of the data
    for i in data:                                      #this shows every list in data
        IDs.append(i[11])

    #print(IDs)

    return IDs, data





# main function, main needs a docstring, too
def main():
    '''
    Purpose: To call functions
    :param: NONE
    :return: NONE
    '''
    start = timeit.timeit()                             #I just wanted to time it to see how long it takes to grab the data, i thought it was lagging at first
    Id ,data = getDataWeb()
    end = timeit.timeit()
    print("It took",end - start, "of a second to read data from the URL.")

    queryQuakes(Id,data)                                #calls queryquake


# main function call
if __name__ == '__main__':
    main()
