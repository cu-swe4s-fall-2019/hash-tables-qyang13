# Hash tables
Implementation of basic hash functions and collision handling strategy
## Highlights
The following features are included in this implementation:

|Hash Functions|Collision handling strategies|
| --- |--- |
|Ascii|Linear Probing|
|Rolling|Chained Hash|
|Sedgwicks (FOR EXTRA CREDIT)|Quadratic Probing (FOR EXTRA CREDIT)|

## Usage
### Hash function
Hash functions allow you to retrieve a key for each value being added
```
python hash_functions.py <FILE_NAME> <ALGORITHM> <HASH_TABLE_SIZE>
```

### Hash table
Hash table utilizes the hash function and insert elements into the newly created table. When collision is encountered, three different handling strategy can be used.
```
python hash_tables.py <SIZE> <HASH_FUNCTION> <COLLISION_STRATEGY> <INPUT_FILE> <NUMBER_OF_KEY_TO_ADD>
```

## Unit testing
The unit tests for functions implemented in `hash_functions.py` and `hash_tables.py` are written using python `unittest` package. You can run the uni test by:
```
python test_hash.py
```

## Function testing and Benchmarking
The function test utilizes the software package `ssshtest`, it will make sure the programs are executed properly. The benchmarking step will examine the hash efficiency and efficacy by testing all the combinations of hashing algorithms and collision handling strategy. Perform function testing and benchmarking by running the bash script (note this might take a few minutes):
```
bash functional_test_benchmark.sh
```
### Evaluation of hash functions
#### Ascii hash
##### Using Random set of words
The random word doesn't seemed to be hashed fully random using Ascii
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/ascii_hash_function_rand.png "ascii plot")
##### Using Non-random set of words
Non-random words tend to be hashed in blocks using this method
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/ascii_hash_function_non_rand.png "ascii plot")


In contrast, the other two hashing methods,  are able to better evenly hashing the elements either with random or non-random words:
#### Rolling hash
##### Using Random set of words
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/rolling_hash_function_rand.png "ascii plot")
##### Using Non-random set of words
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/rolling_hash_function_non_rand.png "ascii plot")

#### Sedgwicks hash
##### Using Random set of words
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_hash_function_rand.png "ascii plot")
##### Using Non-random set of words
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_hash_function_non_rand.png "ascii plot")

### Evaluation of collision strategies
Here, the hashing function is set to the Sedgwicks' hashing method, while collision strategies are compared. For additional collision handling plots using different hashing methods (ascii or rolling), please check inside the directory `./benchmark_plots`.
#### Linear Probing
##### Add
Addition using linear probing suffers from the load factor. The speed is drastically decreased as load factor approaches 1:
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_linear_Add_time.png "ascii plot")
##### Search
Similarly, the search time increase dramatically as the load factor approaches 1:
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_linear_search_time.png "ascii plot")

#### Chained Hash
##### Add
Different from linear probing, the add speed is not affected by the load factor when using chained hash:
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_chain_Add_time.png "ascii plot")
##### Search
Since the elements are inserted more dispersed, the search time varies independent of the load factor.
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_chain_search_time.png "ascii plot")

#### Quadratic Probing
##### Add
Because of the more efficient collision handling, adding elements using quadratic probing is much faster than chained hash or linear probing:
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_quadratic_Add_time.png "ascii plot")

##### Search
The search using quadratic probing is comparable to that of the chained hash. But it does seem to suffer a little more form the laod factor:
![alt text](https://github.com/cu-swe4s-fall-2019/hash-tables-qyang13/blob/master/benchmark_plots/sedgwicks_quadratic_search_time.png "ascii plot")
