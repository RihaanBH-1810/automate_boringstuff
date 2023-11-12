```
Question 1:

Why are functions advantageous to have in your programs?

Answer: A major purpose of functions is to group code that gets executed mul-
tiple times. Without a function defined, you would have to copy and paste
this code each time.Functions are the primary way to compartmentalize your code into logical
groups. Since the variables in functions exist in their own local scopes, the
code in one function cannot directly affect the values of variables in other
functions. This limits what code could be changing the values of your vari-
ables, which can be helpful when it comes to debugging your code.


```
```
QUestion 2:

When does the code in a function execute: when the function is
defined or when the function is called?

Answer: The code in the function is executed when the function s called.
```

```
Question 3:

What statement creates a function?

Answer: A def statement creates a function.
```
```
Question 4:

What is the difference between a function and a function call?

Answer: A function is a block of code which is declared , wheareas when a function call is encountered the funcion is executed.
```
```
Question 5:

How many global scopes are there in a Python program? How many
local scopes?

Answer: Only one global scope exists in a python program. But, there is no reriction in the number of local scopes in a python program.
```
```
Question 6:

What happens to variables in a local scope when the function
call returns?

Answer: When the function call returns the local scope is destroyed and the variables in that scope won't exist.
```
```
Question 7:

What is a return value? Can a return value be part of an expression?

Answer: The value that a function call evaluates to is
called the return value of the function.

When an expression is used with a return statement, the return value
is what this expression evaluates to.

```
```
Question 8:

If a function does not have a return statement, what is the return
value of a call to that function?

Answer: None 
```
``` 
Question 9:

How can you force a variable in a function to refer to the
global variable?

Answer:By using the global statement ie. global variable_name

```
```
Question 10;

What is the data type of None?

Answer: NoneType 
```
```
Question 11:

What does the import areallyourpetsnamederic statement do?

Answer: This statement imports the module named areallyourpetsnamederic .
```
```
Question 12:

If you had a function named bacon() in a module named spam, how
would you call it after importing spam?

Answer: spam.bacon()
```
```
Question 13:

How can you prevent a program from crashing when it gets an error?

Answer: By using exception handling.
```
```
Question 14:

What goes in the try clause? What goes in the except clause?

Answer: The code that could have a potential error is put in a try clause and the code that is to be executed when an error is encountered is put in the exception clause.
```
