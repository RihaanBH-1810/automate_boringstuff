```
Question 1:

What are the two values of the Boolean data type? How do you
write them?

Answer : True and False are the two types of Boolean data types. They written as True and False ie. First letter should be in caps.
```
```
Question 2:

What are the three Boolean operators?

Answer : The three Boolean operators are :
    1.and
    2.or
    3.not

```
```
Question 3:

Write out the truth tables of each Boolean operator (that is, every
possible combination of Boolean values for the operator and what
they evaluate to).

Answer :
Truth table for or operator:
| A    | B    | A or B  |
|------|------|---------|
| True | True | True    |
| True | False| True    |
| False| True | True    |
| False| False| False   |

Truth table for and operator:
| A    | B    | A and B |
|------|------|---------|
| True | True | True    |
| True | False| False   |
| False| True | False   |
| False| False| False   |

Truth table for not operator:
| A    | not A |
|------|-------|
| True | False |
| False| True  |

```
```
Question 4:

What do the following expressions evaluate to?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

Answer :
    (5 > 4) and (3 == 5) evaluates to False
    not (5 > 4) evaluates to False
    (5 > 4) or (3 == 5) evaluates to True
    not ((5 > 4) or (3 == 5)) evaluates to False
    (True and True) and (True == False) evaluates o False
    (not False) or (not True) evaluates to True
```
```
Question 5:

What are the six comparison operators?

Answer : The six ccomparison operators are :
    1. == 
    2. <=
    3. >=
    4. <
    5. >
    6. !=

```
```
Quesion 6:

What is the difference between the equal to operator and the assignment operator?

Answer : The == operator checks if the right and left operands are equal
         The = operator asssigns the value of the right operand to the left operand
    

```
```
Question 7:

Explain what a condition is and where you would use one.

Answer : Conditions are just boolean expressions they are used in flow control statements.
```

```
Question 8:

Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')  
    else:
        print('ham')
    print('spam')
print('spam')


Answer : Three blocks are 1.One main if block 
                          2.Nested if block 
                          3.Nested else block
```  

```
Question 9:

Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
stored in spam, and prints Greetings! if anything else is stored in spam.

Answer:

spam = 1
if spam == 1:
        print("Hello")
elif spam == 2:
        print("Howdy")
else:
        print("Greetings!")
        
```

```
Question 10:

What keys can you press if your program is stuck in an infinite loop?

Answer:Press Ctrl+C

```

```
Question 11:

What is the difference between break and continue?

Answer: When a break statement is encountered in a loop it directly exits the loop whereas when a continue statement is encountered it only skips the execution of the lines following it and jumps to the next iteration.

```
```
Question 12:

What is the difference between range(10), range(0, 10), and range(0, 10, 1)
in a for loop?

Answer:There is no difference between them 
```
```
Question 13:

Write a short program that prints the numbers 1 to 10 using a for loop.
Then write an equivalent program that prints the numbers 1 to 10 using
a while loop.

Answer: 

Using for loop :

for(i in range(1, 11)):
    print(i)

Using while loop :

i = 1
while True:
    print(i)
    i += 1
    if i == 11:
        break

```

```
Question 14:
If you had a function named bacon() inside a module named spam, how
would you call it after importing spam?

Answer: spam.bacon()

```
