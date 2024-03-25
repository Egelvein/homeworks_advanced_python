# Classes for matrix's operations

Solving tasks on creating classes for work with matrices

## Contents
- [Task 1](#task-1)
- [Task 2](#task-2)
- [Task 3](#task-3)

### Task 1
**Task:** 

You need to implement a small library for working with matrices
- Make a matrix class in which to define addition and multiplication operations (matrix and component-by-component) by overloading ```+, *, @``` operators (as in numpy). Call exceptions if the matrices on the input are of incorrect dimension (ValueError)
- Generate two matrices via ```np.random.randint(0, 10, (10, 10))``` with seed 0 and perform all three operations on them.
- Write the results to text files named ```matrix+.txt```, ```matrix*.txt```, ```matrix@.txt```, respectively. This will be an artifact of the task.

 
**Solution:**
Solution of this task are files in the folder ```artifacts/3.1```

### Task 2
**Task:**

- Using numpy mixins, make a class that will be able to perform all standard arithmetic operations.
- Also add through mixins: writing an object to a file, beautiful display in the console (__str__), getters and setters for class fields
- The classes themselves should have a minimum number of methods

 
**Solution:**
Solution of this task are files in the folder ```artifacts/3.2```

### Task 3
**Task:** 

The task is a continuation of task 1:
- To invent and implement the simplest hash function (give a brief text description in the comments in the code) for a matrix in the __hash__ method (put it in the mixins).
- Restriction on the hash function - it must be non-constant (not return always one number)
- Configure caching of the product of matrices by this hash function
- Find collision in the hash function (if the search is done by code, the code should also be posted).
- The artifact is 7 files:
- - ```A.txt```, ```B.txt```, ```C.txt```, ```D.txt``` are matrices such that ```(hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D))```
- - ```AB.txt``` is the result of the product ```A @ B```
- - ```CD.txt``` - the real result of ```C @ D```
- - ```hash.txt``` - hash of matrices ```AB``` and ```CD```


**Description:**
I failed to create a hash function so that ```A != C``` but ```hash(A) == hash(C)```. Also I don`t know how to add my hash function in the mixin.

I decided to use a hash function I invented myself, because the conditional method of mean squares seemed too simple to me: ```hash_value = value^3 + (seed - 2)*value``` 

But I managed to create a reverse hash function, which I also checked here (the file can be found in the solutions folder)
 
**Solution:**
Solution of this task are files in the folder ```artifacts/3.3```
