# CSCI 310 Organ 
# Program #3: Procedural/Object-Oriented
# Author: Skyler Selfridge
# Date: 20 April 2018
#
# 
#-------------------------------------------------------------------------------------------
def hlbackwards(input_list):
    length = len(input_list)
    s = length
    new_list = [None]*length
    for item in input_list:
        s = s - 1
        new_list[s] = item
    return new_list
#-------------------------------------------------------------------------------------------

def llbackwards(input_list):
    reversed_list = []
    for sublist in input_list:
        if isinstance(sublist, list):
            reversed_list.append(llbackwards(sublist))
        else:
            reversed_list.append(sublist)

    reversed_list.reverse()
    return reversed_list

def is_list(input_list):
    return isinstance(input_list, list)
#-------------------------------------------------------------------------------------------

def palindrome(input_list):
   
    reversed_input_list = llbackwards(input_list)
  
    if input_list == reversed_input_list:
       return input_list
    else:
        head, *tail = reversed_input_list
        pal = input_list + tail
        return pal
#-------------------------------------------------------------------------------------------

def permutations(input_list):
    from itertools import permutations
    perms = []
    var = permutations(input_list)
    for perm in var:
        perms.append([perm])
    return  perms
#-------------------------------------------------------------------------------------------

# Helper function that does ionah
def doIonah(n,to,From,u):
    def print_move(From,to):
        print("Move disk from peg '{}' to peg '{}'".format(From,to))
    if n > 0:
        doIonah(n-1,u,From,to)
        print_move(From,to)
        doIonah(n-1,to,u,From)
# Main function that calls the helper
def ionah(n):
    doIonah(n,3,1,2)
#-------------------------------------------------------------------------------------------



def zsequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        N = 0
        N = 2 * zsequence(n - 1) + zsequence(n - 2)
        return N

def sequence(n):
    return xsequence(n,n)

# Main function
def xsequence(n,max):
    
    if n == 1:
        return [0]
    elif n == 2:
        return [1]
    elif n > 2:
        N = [zsequence(n)]
        seq_list = N + xsequence(n - 1,max)
    if n == max:
        #zero always occurs if n is greater than 2 so we should always add it
        return hlbackwards(seq_list + [0])
    else:
        return seq_list

#-------------------------------------------------------------------------------------------

def argue(sentence):
    if 'not' in sentence:
        sentence.remove('not')
        for i in range(0,len(sentence)):
            if sentence[i] == 'you':
                sentence[i] = 'i'
            elif sentence[i] == 'i':
                sentence[i] = 'you'
            elif sentence[i] == 'am':
                sentence[i] = 'are'
            elif sentence[i] == 'are':
                sentence[i] = 'am'
            elif sentence[i] == 'are':
                sentence[i] = 'am'
            elif sentence[i] == 'is':
                sentence[i] = 'is'
            elif sentence[i] == 'is':
                sentence[i] = 'is'
            elif sentence[i] == 'your':
                sentence[i] = 'my'
            elif sentence[i] == 'my':
                sentence[i] = 'your'
            elif sentence[i] == 'does':
                sentence[i] = 'does'
            elif sentence[i] == 'does':
                sentence[i] = 'does'
    else:
        for i in range(0,len(sentence)):
            if sentence[i] == 'you':
                sentence[i] = 'i'
            elif sentence[i] == 'i':
                sentence[i] = 'you'
            elif sentence[i] == 'am':
                sentence[i] = 'are'
                sentence.insert(i+1,'not')
            elif sentence[i] == 'are':
                sentence[i] = 'am'
                sentence.insert(i+1,'not')
            elif sentence[i] == 'are':
                sentence[i] = 'am'
            elif sentence[i] == 'is':
                sentence[i] = 'is'
                sentence.insert(i+1,'not')
            elif sentence[i] == 'is':
                sentence[i] = 'is'
            elif sentence[i] == 'your':
                sentence[i] = 'my'
            elif sentence[i] == 'my':
                sentence[i] = 'your'
            elif sentence[i] == 'does':
                sentence[i] = 'does'
                sentence.insert(i+1,'not')
            elif sentence[i] == 'does':
                sentence[i] = 'does'
                
    return sentence
#-------------------------------------------------------------------------------------------

def bubblesort(input_list):
    temp = []
    for nextNum in range(len(input_list) - 1, 0 , - 1):
        for i in range(nextNum):
            if input_list[i] > input_list[i + 1]:
                temp = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = temp

    return input_list
