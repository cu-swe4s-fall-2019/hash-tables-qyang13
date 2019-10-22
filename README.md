# Hash tables
Implementation of basic hash functions and collision handling strategy
## Highlights
The following features are included in this implementation:

|Hash Functions|Collision handling strategies|
| --- |--- |
|Ascii|Linear Probing|
|Rolling|Chained Hash|
|Sedgwicks|Quadratic Probing|

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
