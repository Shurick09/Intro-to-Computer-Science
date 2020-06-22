'''
Created on Mar 6, 2017

@author: Shurick

Alexander Rozenblit and Mitchell Gutman

I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1


# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def compress(s):
    '''Takes in a 64 bit string of 0's and 1's and returns the compressed version of that '''
    if s == []:
        return 0
    elif s[0] == '1':
        return  '00000' + converter(s)
    else:
        return converter(s)

def start(x):
    ''' Figures out if the first character in the list is a 0 or 1 '''
    if x[0] == '0':
        return count_0(x)
    else:
        return count_1(x)

def count_0(x):
    '''Counts the amount of consecutive 0's at the beginning of the string'''
    if x == '':
        return 0
    elif x[0] != '0':
        return 0
    else:
        return count_0(x[1:]) + 1
    
def count_1(x):
    '''Counts the amount of consecutive 1's at the beginning of the string'''
    if x == '':
        return 0
    elif x[0] != '1':
        return 0
    else:
        return count_1(x[1:]) + 1
   
def converter(x):
    ''' Converts the string into pieces of compressed code'''
    if x == '':
        return ''
    elif start(x) <= MAX_RUN_LENGTH:
        return (str(((COMPRESSED_BLOCK_SIZE - len(numToBinary(start(x)))) * '0') + str(numToBinary(start(x)))) + str(converter(x[start(x):])))
    else:
        return (str('1' * COMPRESSED_BLOCK_SIZE) + '00000') + converter(x[MAX_RUN_LENGTH:])

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return (n%2 != 0)

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n/2) + '0'
    
def uncompress(c):
    '''Reverses the function of compress by taking in a string and returning the full version of it '''
    return uncompress_1(c)

def uncompress_1(x):
    ''' Uncompresses the first set of bits'''
    if x == '':
        return ''
    else:
        return binaryToNum(x[:COMPRESSED_BLOCK_SIZE]) * '0' + uncompress_2(x[COMPRESSED_BLOCK_SIZE:])

def uncompress_2(x):
    ''' Alternates with uncompress_1 to work out each part of the compressed string '''
    if x == '':
        return ''
    else:
        return binaryToNum(x[:COMPRESSED_BLOCK_SIZE]) * '1' + uncompress_1(x[COMPRESSED_BLOCK_SIZE:])

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binaryToNum_helper(s,c):
        if s == '':
            return 0
        else:
            return binaryToNum_helper(s[:-1],c+1) + int(s[-1])* 2**c
    return binaryToNum_helper(s,0)

def compression(s):
    ''' Takes in a 64 bit string and returns the ratio of the length of the compressed string with the original string'''
    return len(compress(s)) / len(s)


'''
The largest string to compress would be '10' repeated 32 times. This is the longest because it needs to start with a certain
amount of 0's and then has to alternate between a 1 and a 0 after every digit. The compressed version of that string would be 325
bits.

I added two test cases to further test my program. They both yielded compression ratios of about 0.4.

Professor Lai's algorithm guaranteeing that the compressed version of the string will always be shorter than the uncompressed
version can not exist. It can not exist, because when the string being compressed is 1's and 0's alternating or '10' * 32 the 
compressed string will need to switch between 1's and 0's every digit. No matter what the k value this will cause a larger
compressed string than uncompressed string. This example of a string is why Professor Lai's algorithm can not exist.
'''

print(count_0('000'))
print(count_1('111'))
print(start('0000000000000000000000000000000000000000000000000000000000000000'))        
print((numToBinary(start('00000000000000000000000000000000000000000000000000000000000000000'))))
print (str(((COMPRESSED_BLOCK_SIZE - len(numToBinary(start('00')))) * '0') + str(numToBinary(start('00')))))
print(compress('0000000000000000000000000000000000000000000000000000000000000000')) 
print(compress('00'))
print(compress('0101010101010101010101010101010101010101010101010101010101010101'))
print(compress('00000000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000000000000000000000'))
print(compress('11111111111111111111111111111111111111111111111111111111111111100000000000000000000000000000000000000000000000000000000000000011'))
print(compress('1111111111111111111111111111111111111111111111111111111111111111'))
print (uncompress('11111000001111100000000100'))     
print(uncompress(compress('0000000000000000000000000000000000000000000000000000000000000000')))
print(COMPRESSED_BLOCK_SIZE * '0')
print(compress('1111111111111111111111111111111100000000000000000000'))
print(len(compress('1010101010101010101010101010101010101010101010101010101010101010')))
print(compression('1111111111111111111111111111111111111111111111111111111111111111'))
print(compression('1111111111111111111111111111111100000000000000000000'))