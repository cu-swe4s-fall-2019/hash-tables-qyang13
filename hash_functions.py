import os
import argparse


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
    p a prime number roughly equal to the number of characters in the
    input alphabe
    m should be a large number, since the probability of two random strings
    colliding is about 1/m. Sometimes m=2^64 is chosen
    '''
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N


def h_sedgwicks(key, N):
    '''
    A hash function mentioned in Robert Sedgwicks's Algorithm in C. Optimized
    to speed up the process
    '''
    b = 378551
    a = 63689
    s = 0
    for i in range(len(key)):
        s = s * a + ord(key[i])
        a = a * b
    return s % N


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hash functions')

    parser.add_argument('input', type=str,
                        help='Input filename')

    parser.add_argument('algorithm', type=str,
                        help='Hash functions')

    parser.add_argument('size', type=int,
                        help='Size of hash table')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError('Invalid inputfile')
    if args.algorithm not in ['ascii', 'rolling', 'sedgwicks']:
        raise ValueError('Invalid hash algorithm selection')
    if args.size <= 0:
        raise ValueError('Invalid hash table sizes')

    for l in open(args.input):
        if args.algorithm == 'ascii':
            print(h_ascii(l, args.size))
        elif args.algorithm == 'rolling':
            print(h_rolling(l, args.size))
        elif args.algorithm == 'sedgwicks':
            print(h_sedgwicks(l, args.size))
