#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_pystyle pycodestyle *.py
assert_exit_code 0

run bad_input python hash_functions.py Idontexist.txt rolling 1000
assert_in_stderr 'Invalid inputfile'

run bad_algorithm python hash_functions.py rand_words.txt Idontexist 1000
assert_in_stderr 'Invalid hash algorithm selection'

run bad_size python hash_functions.py rand_words.txt ascii -1000
assert_in_stderr 'Invalid hash table sizes'

run bad_size python hash_tables.py -10000 rolling linear rand_words.txt 100
assert_in_stderr 'Invalid hash table sizes'

run bad_algorithm python hash_tables.py 10000 Idontexist linear rand_words.txt 100
assert_in_stderr 'Specified hash function does not exist'

run bad_collision python hash_tables.py 10000 rolling Idontexist rand_words.txt 100
assert_in_stderr 'Specified collision strategy does not exist'

run bad_input python hash_tables.py 10000 rolling linear Idontexist.txt 100
assert_in_stderr 'Input file not found'

run bad_key python hash_tables.py 10000 rolling linear rand_words.txt -100
assert_in_stderr 'Invalid key number'

# Benchmarking step, generates all possible plots
declare -a arr_alg=("ascii" "rolling" "sedgwicks")
declare -a arr_col=("linear" "chain" "quadratic")

for hash_function in "${arr_alg[@]}"
do
    # Random words
    python hash_functions.py rand_words.txt ${hash_function} | python scatter.py ${hash_function}_hash_function_rand.png "Hashed word" "Hashed value"
    # Non-random words
    python hash_functions.py non_rand_words.txt ${hash_function} | python scatter.py ${hash_function}_hash_function_non_rand.png "Hashed word" "Hashed value"

    for collision_strategy in "${arr_col[@]}"
    do
        for M in $( seq  1000 1000 10000 ); do
            python hash_tables.py 10000 ${hash_function} ${collision_strategy} rand_words.txt $M >  ${hash_function}_${collision_strategy}_rand.$M.txt
        done

        # Add
        grep add ${hash_function}_${collision_strategy}_rand.*.txt | cut -d " " -f2,3 | python scatter.py ${hash_function}_${collision_strategy}_Add_time.png "Load factor" "Add time"

        # Search
        (for M in $( seq  1000 1000 10000 ); do
            load_factor=$(bc -l <<< "$M/10000")
            echo -n "$load_factor "
            grep search ${hash_function}_${collision_strategy}_rand.$M.txt | cut -d " " -f2 | python mean.py
        done) | python scatter.py ${hash_function}_${collision_strategy}_search_time.png "Load factor" "Search time"
    done
    rm *_rand.*.txt
done
