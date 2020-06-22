'''
Created on Apr 6, 2017

@author: Shurick
'''

list1 = ['A','B','D','F']
list2 = ['E','C','B','A']

def num_matches(list1,list2):
    '''Returns the number of elements that are both in list1 and list2'''
    list1.sort()
    list2.sort()
    matches = 0
    i= 0
    j = 0
    while i < len(list2) and j < len(list2):
        if list1[i] == list2[j]:
            matches = matches + 1
            i = i + 1
            j = j + 1
        elif list1[i] < list2[j]:
            i = i + 1
        else:
            j = j + 1
    return matches

def keep_matches(list1,list2):
    '''Returns the number of elements that are both in list1 and list2'''
    list1.sort()
    list2.sort()
    result = []
    i= 0
    j = 0
    while i < len(list2) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i = i + 1
            j = j + 1
        elif list1[i] < list2[j]:
            i = i + 1
        else:
            j = j + 1
    return result

def drop_matches(list1,list2):
    '''Returns the number of elements that are both in list1 and list2'''
    list1.sort()
    list2.sort()
    result = []
    i= 0
    j = 0
    while i < len(list2) and j < len(list2):
        if list1[i] == list2[j]:
            i = i + 1
            j = j + 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i = i + 1
        else:
            result.append(list2[j])
            j = j + 1
    while i < len(list1):
        result.append(list1[i])
        i = i + 1
    while j < len(list2):
        result.append(list2[j])
        j = j + 1
    return result

print(num_matches(list1,list2))
print(keep_matches(list1,list2))
print(drop_matches(list1,list2))