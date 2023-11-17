```
Q1

Write an assert statement that triggers an AssertionError if the variable
spam is an integer less than 10.

Ans: asssert spam > 10, "Value of spam is less than 10"
```
```
2. Write an assert statement that triggers an AssertionError if the variables
eggs and bacon contain strings that are the same as each other, even if
their cases are different (that is, 'hello' and 'hello' are considered the
same, and 'goodbye' and 'GOODbye' are also considered the same).

Ans:  assert eggs.upper() != bacon.upper(), 'variable eggs and bacon have the same value'   

```
```
3. Write an assert statement that always triggers an AssertionError.

Anns: assert False, 'always triggers as assertionerror'

```
```
4. What are the two lines that your program must have in order to be able
to call logging.debug()?

Ans: import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```
```
5. What are the two lines that your program must have in order to have
logging.debug() send a logging message to a file named programLog.txt?

Ans: import logging
     logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
```
```
6. What are the five logging levels?

Ans:  DEBUG
      ERROR
      WARNING
      INFO
      CRITICAL

```
```
7. What line of code can you add to disable all logging messages in
your program?

Ans:logging.disable(logging.CRITICAL)
```
```
8. Why is using logging messages better than using print() to display
the same message?

Ans: Beacuse you can remove th logging messages without having to remove all the fucntion calls just by disabling them .
```
```
9. What are the differences between the Step Over, Step In, and Step
Out buttons in the debugger?

Ans:While using step in if the next line of code is a function call, the
debugger will “step into” that function and jump to the first line of code of
that function.

While using step over if the next line of code is a function call, the
Step Over button will “step over” the code in the function. The function’s
code will be executed at full speed, and the debugger will pause as soon as
the function call returns
```
```
10. After you click Continue, when will the debugger stop?

Ans:When it reaches a breakpoint or when the program ends.

```
```
11. What is a breakpoint?

Ans:A breakpoint can be set on a specific line of code and forces the debugger to
pause whenever the program execution reaches that line

```
```
12. How do you set a breakpoint on a line of code in Mu?

Ans: To set a breakpoint, click the line number in the file editor to cause a red dot
to appear, marking the breakpoint.

```

