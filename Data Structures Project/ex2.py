#!/usr/bin/python
""" Exercise 2 """
import glob
import os
from System import Array

runtime = 0

def listFiles(dirAddr):
    print("Directory path: " + dirAddr)
    files = glob.glob(dirAddr + "//*.txt")
    return Array[str](files)

def readFileDate(fileAddr):
    f = open(fileAddr, 'r')
    date = f.readline()
    f.close()
    strDate = date.Substring(6, 10)
    year = int(strDate.Substring(6, 4))
    month = int(strDate.Substring(3, 2))
    day = int(strDate.Substring(0, 2))
    dateStruct = [year, month, day]
    return Array[int](dateStruct)

def readFileLanguage(fileAddr):
    f = open(fileAddr, 'r')
    f.readline()
    lang = f.readline()
    endIndex = lang.find("</language>")
    lang = lang.Substring(10, endIndex - 10)
    return lang

def buildDatabase(dirAddr):
    print("Directory path: " + dirAddr)
    print("")
    fileList = Array[str](os.listdir(dirAddr))
    database = []
    i = 0
    print("Database build output:")
    print("Index\t|\tFile Name\t|\tDate\t\t|\tLanguage")
    print("---------------------------------------------------------------------------------------------------")
    for file in Array[str](fileList):
        fileProperties = [file, dirAddr + "\\" + file, readFileDate(dirAddr + "\\" + file), readFileLanguage(dirAddr + "\\" + file)]
        database.append(fileProperties)
        print(str(i) + "\t|\t"),
        print(fileProperties[0] + "\t|\t"),
        print(str(fileProperties[2][2]) + "/" + str(fileProperties[2][1]) + "/" + str(fileProperties[2][0]) + "\t|\t"),
        print(fileProperties[3])
        i = i + 1
    print("")
    return database

def buildLanguageDatabase(dirAddr):
    database = buildDatabase(dirAddr)
    langDatabase = []
    if len(database) > 0:
        for item in database:
           if item[3] not in langDatabase:
                langDatabase.append(item[3])
    langDatabase.sort()
    for lang in langDatabase:
        print(lang)
    return

def mergeSortByLang(arr):
    global runtime
    runtime = runtime + 1  
    if len(arr) == 1:
        runtime = runtime + 1  
        return arr  
      
    m = len(arr) / 2
    runtime = runtime + 1 
    l = mergeSortByLang(arr[:m])  
    r = mergeSortByLang(arr[m:])  
    runtime = runtime + 1 
    if not len(l) or not len(r):
        runtime = runtime + 1   
        return l or r  
          
    result = []  
    i = j = 0  
    runtime = runtime + 1 
    while (len(result) < len(r)+len(l)): 
        runtime = runtime + 1          
        if l[i][3] < r[j][3]:  
            result.append(l[i])  
            i += 1 
            runtime = runtime + 2 
        else:  
            result.append(r[j])  
            j += 1
            runtime = runtime + 2
        runtime = runtime + 1              
        if i == len(l) or j == len(r):              
            result.extend(l[i:] or r[j:])
            runtime = runtime + 1   
            break  
    runtime = runtime + 1       
    return result

def quickSortByLang(arr, start, end):
    global runtime
    runtime += 1
    if start < end:
        pivot = partitionByLang(arr, start, end)
        quickSortByLang(arr, start, pivot-1)
        quickSortByLang(arr, pivot+1, end)
        runtime += 3
    return arr

def partitionByLang(arr, start, end):
    global runtime
    pivot = arr[start]
    left = start+1
    right = end
    done = False
    runtime += 5
    while not done:
        runtime += 1
        while left <= right and arr[left][3] <= pivot[3]:
            left = left + 1
            runtime += 1
        while arr[right][3] >= pivot[3] and right >=left:
            right = right -1
            runtime += 1
        runtime += 1
        if right < left:
            done= True
            runtime += 1
        else:
            temp=arr[left]
            arr[left]=arr[right]
            arr[right]=temp
            runtime += 3
    temp=arr[start]
    arr[start]=arr[right]
    arr[right]=temp
    runtime += 3
    return right

def sortByLangMergeSort(dirAddr):
    global runtime
    runtime = 0
    database = buildDatabase(dirAddr)
    sortedDatabase = mergeSortByLang(database)
    i = 0
    print("Database sorted by language output:")
    print("Index\t|\tFile Name\t|\tDate\t\t|\tLanguage")
    print("---------------------------------------------------------------------------------------------------")
    for item in sortedDatabase:
        print(str(i) + "\t|\t"),
        print(item[0] + "\t|\t"),
        print(str(item[2][2]) + "/" + str(item[2][1]) + "/" + str(item[2][0]) + "\t|\t"),
        print(item[3])
        i = i + 1
    print("Runtime: " + str(runtime))
    print("")
    return sortedDatabase

def sortByLangQuickSort(dirAddr):
    database = buildDatabase(dirAddr)
    sortedDatabase = quickSortByLang(database, 0, len(database) - 1)
    i = 0
    print("Database sorted by language output:")
    print("Index\t|\tFile Name\t|\tDate\t\t|\tLanguage")
    print("---------------------------------------------------------------------------------------------------")
    for item in sortedDatabase:
        print(str(i) + "\t|\t"),
        print(item[0] + "\t|\t"),
        print(str(item[2][2]) + "/" + str(item[2][1]) + "/" + str(item[2][0]) + "\t|\t"),
        print(item[3])
        i = i + 1
    print("Runtime: " + str(runtime))
    print("")
    return sortedDatabase

def sortByDay(arr):
    if len(arr) == 1:  
        return arr
    
    aux_arr = []
    for i in range(31):
        aux_arr.append([])
    for item in arr:
        aux_arr[item[2][2] - 1].append(item)
    result = []
    for i in range(30):
        for item in aux_arr[i]:
            result.append(item)

    return result

def sortByMonth(arr):
    if len(arr) == 1:  
        return arr
    
    aux_arr = []
    for i in range(12):
        aux_arr.append([])
    for item in arr:
        aux_arr[item[2][1] - 1].append(item)
    result = []
    for i in range(12):
        for item in aux_arr[i]:
            result.append(item)

    return result

def sortByYear(arr):
    if len(arr) == 1:  
        return arr
    
    aux_arr = [] * 56
    for i in range(56):
        aux_arr.append([])
    for item in arr:
        aux_arr[item[2][0] - 1960].append(item)
    result = []
    for i in range(56):
        for item in aux_arr[i]:
            result.append(item)

    return result

def sortByDate(dirAddr):
    database = buildDatabase(dirAddr)
    sortedDatabase = sortByDay(database)
    sortedDatabase = sortByMonth(sortedDatabase)
    sortedDatabase = sortByYear(sortedDatabase)
    i = 0
    print("Database sorted by date output:")
    print("Index\t|\tFile Name\t|\tDate\t\t|\tLanguage")
    print("---------------------------------------------------------------------------------------------------")
    for item in sortedDatabase:
        print(str(i) + "\t|\t"),
        print(item[0] + "\t|\t"),
        print(str(item[2][2]) + "/" + str(item[2][1]) + "/" + str(item[2][0]) + "\t|\t"),
        print(item[3])
        i = i + 1
    print("")
    return sortedDatabase

def compareSortsByLang(dirAddr):
    global runtime
    runtime = 0
    database = buildDatabase(dirAddr)
    sortedDatabase = mergeSortByLang(database)
    mergeRuntinme = runtime
    runtime = 0
    sortedDatabase = quickSortByLang(database, 0, len(database) - 1)
    if (mergeRuntinme == runtime):
        print ("Both quick sort and merger sort runtime is:" + str(runtime))
        print("")
    else:
        print("Merge sort runtime is: " + str(mergeRuntinme))
        print("Quick sort runtime is: " + str(runtime))
        if (mergeRuntinme > runtime):
            print("Quick sort algorithm is faster by " + str(float(mergeRuntinme) / float(runtime)) + " times")
            print("")
        else:
            print("Merge sort algorithm is faster by " + str(float(runtime) / float(mergeRuntinme)) + " times")
            print("")
    return