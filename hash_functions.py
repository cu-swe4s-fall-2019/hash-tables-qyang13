import sys

def h_ascii(key, N):
    '''
    A basic ascii hash function that assign the key based on ascii values
    '''
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_rolling(key, N, p=53, m=2**64):
    '''
    p a prime number roughly equal to the number of characters in the input alphabe
    m should be a large number, since the probability of two random strings colliding is
    about 1/m. Sometimes m=2^64 is chosen
    '''
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N

if __name__ == '__main__':

    for l in open(sys.argv[1]):
        if sys.argv[2] == 'ascii':
            print(h_ascii(l, 1000))
        elif sys.argv[2] == 'rolling':
            print(h_rolling(l, 1000))
