```
Question 1:

What are escape characters?

Answer:Escape charectors let you use charectors that are otherwise not possible to put in a string

```
```
Question 2:

What do the \n and \t escape characters represent?

Answer:\n is for newline charector  and \t is for horizontal tab.

```
```
Question 3:

How can you put a \ backslash character in a string?

Answer: \\ 
```
```
Question 4:

The string value "Howl's Moving Castle" is a valid string. Why isn’t it a prob-
lem that the single quote character in the word Howl's isn’t escaped?

Answer:Because it is enclosed in double quotes.
```
```
Question 5:

If you don’t want to put \n in your string, how can you write a string
with newlines in it?

Answer: We can use multiline strings which are enclosed between three double quotes or single quotes on both sides.

```
```
Question 6:

What do the following expressions evaluate to?
• 'Hello, world!'[1]
• 'Hello, world!'[0:5]
• 'Hello, world!'[:5]
• 'Hello, world!'[3:]

Answer :
• 'Hello, world!'[1] = 'e'
• 'Hello, world!'[0:5] = 'Hello'
• 'Hello, world!'[:5] = 'Hello'
• 'Hello, world!'[3:] = 'lo, world'
```
```
Question 7:

What do the following expressions evaluate to?
• 'Hello'.upper()
• 'Hello'.upper().isupper()
• 'Hello'.upper().lower()

Answer:
• 'Hello'.upper() = 'HELLO'
• 'Hello'.upper().isupper() = TRUE
• 'Hello'.upper().lower() = 'hello'
```
```
Question 8:

What do the following expressions evaluate to?
• 'Remember, remember, the fifth of November.'.split()
• '-'.join('There can be only one.'.split())

Answer:'Remember, remember, the fifth of November.'.split() = ['Remember',', ','remember', ', ', 'the', 'fifth', 'of', 'November.']
        '-'.join('There can be only one.'.split()) = 'There-can-be-only-one.'
```
```
Question 9:

What string methods can you use to right-justify, left-justify, and center
a string?

Answer:rjust(), ljust(), center()

```
```
Question 10:

How can you trim whitespace characters from the beginning or end of
a string?

Answer:USing the lstrip() method to trim whitespace from the beginning and rtstrip() method to trim from the end.

```
