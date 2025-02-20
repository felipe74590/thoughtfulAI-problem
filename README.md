# thoughtfulAI-problem

## Coding Assessment
 The coding assessment can be found in ```problem.py``` and can be ran with ```python problem.py```. At the bottom of the file you can find an example of how to call the function.

 Unittest can be found in ```test_sort.py``` , edge cases are covered to verify that all conditions are met and covered. To run use
 ```python -m unittest test_sort.py```


## Live Coding Assessment
 By reading the description of the problem, you can notice that they emphazie working with data. They ask you to process data from a csv file, transform the data so that it can be analyzed, and then displayed after calculations have been made on the transfomed data. The solution for the live coding assessment will also use the ```sort()``` function in ```problem.py```.

 * One of the best tools used in python programing for this is ```pandas```.
    * With Pandas this data can be sorted, cleaned, updated or transformed, and prepared for display. For example it has it's own read_csv function
    * Using Pandas we can simplify the functionaliy in ```assessment.clean_data``` and ```assessment.read_from_csv```.
