import argparse
import sys
import hash_functions
import time
import random
import os


class LinearProbe:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        '''
        Function to add key and value to the hash table
        '''
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        '''
        Function to search for key and value in the hash table
        '''
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


class ChainHashTable:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        '''
        Function to add key and value to the hash table
        '''
        hash_slot = self.hash(key, self.N)
        self.T[hash_slot].append((key, value))
        self.M += 1
        return True

    def search(self, key):
        '''
        Function to search for key and value in the hash table
        '''
        hash_slot = self.hash(key, self.N)

        for k, v in self.T[hash_slot]:
            if key == k:
                return v
        return None


class QuadraticProbing:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N   # Size of the hash
        self.T = [None for i in range(N)]
        self.M = 0   # Number of elements
        self.K = []  # Addiitonal array to store key separately

    def quadraticProbing(self, pos):
        # limit variable is used to restrict the function from going into
        # infinite loop limit is useful when the table is 80% full
        limit = 50
        i = 1
        # start a loop to find the pos
        while i <= limit:
            # calculate new position by quadratic probing
            newPos = pos + (i**2)
            newPos = newPos % self.N
            # if newPos is empty then break out of loop and return new Position
            if self.T[newPos] is None:
                break
            else:
                # as the position is not empty increase i
                i += 1
        return newPos

    def add(self, key, value):
        '''
        Function to add key and value to the hash table
        '''
        hash_slot = self.hash(key, self.N)

        # checking if the position is empty
        if self.T[hash_slot] is None:
            # empty position found , store the element and print the message
            self.T[hash_slot] = (key, value)
            self.M += 1
            self.K.append(key.strip('\n'))
        # collision occured hence we do linear probing
        else:
            hash_slot = self.quadraticProbing(hash_slot)
            self.T[hash_slot] = (key, value)
            self.M += 1
            self.K.append(key.strip('\n'))
        return True

    # method that searches for an element in the table
    # returns position of element if found
    # else returns False
    def search(self, key):
        '''
        Function to search for key and value in the hash table
        '''
        hash_slot = self.hash(key, self.N)
        if self.T[hash_slot] is None:
            return None
        elif self.T[hash_slot][0] == key:
            return (self.T[hash_slot][1])
        # if element is not found at position returned hash function
        # then we search element using quadratic probing
        else:
            limit = 50
            i = 1
            newSlot = hash_slot
            # start a loop to find the position
            while i <= limit:
                # calculate new position by quadratic probing
                newSlot = hash_slot + (i**2)
                newSlot = newSlot % self.N
                # if element at newPosition is equal to the required element
                if self.T[newSlot] is None:
                    return None
                    break
                elif self.T[newSlot][0] == key:
                    return (self.T[newSlot][1])
                    break
                else:
                    # as the position is not empty increase i
                    i += 1
            return None


def reservoir_sampling(new_val, size, V):
    '''
    Function to subsample the given reservoir by provided size
    '''
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='self-defined hash table objects')
    parser.add_argument('size', type=int, help='Hash table size')
    parser.add_argument('hash_function', type=str, help='Hash function'
                        'ascii | rolling | sedgwicks')
    parser.add_argument('collision_strategy', type=str,
                        help='Choose collision handling strategy'
                        'linear | chain | quadratic')
    parser.add_argument('input', type=str, help='Input filename')
    parser.add_argument('num_key', type=int, help='Number of key to add')

    args = parser.parse_args()

    if args.size <= 0:
        raise ValueError('Invalid hash table sizes')
    if not os.path.exists(args.input):
        raise FileNotFoundError('Input file not found')
    if args.hash_function not in ['ascii', 'rolling', 'sedgwicks']:
        raise ValueError('Specified hash function does not exist')
    if args.collision_strategy not in [
                        'linear', 'chain', 'quadratic']:
        raise ValueError('Specified collision strategy does not exist')
    if args.num_key <= 0:
        raise ValueError('Invalid key number')

    N = args.size
    hash_alg = args.hash_function
    collision_strategy = args.collision_strategy
    data_file_name = args.input
    keys_to_add = args.num_key

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_ascii)
        elif collision_strategy == 'quadratic':
            ht = QuadraticProbing(N, hash_functions.h_ascii)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_rolling)
        elif collision_strategy == 'quadratic':
            ht = QuadraticProbing(N, hash_functions.h_rolling)

    elif hash_alg == 'sedgwicks':
        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_sedgwicks)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_sedgwicks)
        elif collision_strategy == 'quadratic':
            ht = QuadraticProbing(N, hash_functions.h_sedgwicks)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('add', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)
