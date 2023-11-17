```
Question 1:

Does PyInputPlus come with the Python Standard Library?

Answer: No, you will have to install it with pip
```
```
Question 2:

Why is PyInputPlus commonly imported with import pyinputplus as pyip?

Answer: It helps save time as we are not required to type pyInputplus again and again in our code to use the module.
```
```
Question 3:

What is the difference between inputInt() and inputFloat()?

Answer: inputInt() accepts only integer values whereas inputFloat accepts integers(for eg it stores 19 as 19.0) and float values
```
```
Question 4:

How can you ensure that the user enters a whole number between 0 and
99 using PyInputPlus?

Answer: response = pyip.inputInt(min = 0, max =99)

```
```
Question 5:

What is passed to the allowRegexes and blockRegexes keyword arguments?

Answer: A list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.
```
```
Question 6:

What does inputStr(limit=3) do if blank input is entered three times?

Answer:It will raise a RetryLimitException
```
```
Question 7:

What does inputStr(limit=3, default='hello') do if blank input is entered
three times?

Answer:The function will simply return 'hello'.
```
