```
Question 1:

What is the function that creates Regex objects?

Answer:re.compile()

```
```
Question 2:

Why are raw strings often used when creating Regex objects?
What does the search() method return?

Answer:Raw strings are particularly useful when working with regular expressions, as they allow you to specify patterns that may contain backslashes without having to escape them.search() method returns a match object .

```
```
Question 3:

How do you get the actual strings that match the pattern from a
Match object?

Answer: using the group() method.

```
```
Question 4:

In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does
group 0 cover? Group 1? Group 2?

Answer:group(0) covers whole '(\d\d\d)-(\d\d\d-\d\d\d\d)', group(1) covers '(\d\d\d)'
group(2) covers '(\d\d\d-\d\d\d\d)'.

```
```
Question 5:

Parentheses and periods have specific meanings in regular expression
syntax. How would you specify that you want a regex to match actual
parentheses and period characters?

Answer:By using backslash before the parentheses and period

```
```
Question 6:

The findall() method returns a list of strings or a list of tuples of
strings. What makes it return one or the other?

Answer: If there are no groups in the regular expression then finall() will return a list of strings 
but, if there are groups in the regular expression then findall() will return a list of tuples.

```
```
Question 7:

What does the | character signify in regular expressions?

Answer:| is called pipe You can use it anywhere you want to match
one of many expressions

```
```
Quesiton 8:

What two things does the ? character signify in regular expressions?

Answer: question mark can have two meanings in regular expres-
sions: declaring a non-greedy match or flagging an optional group.

```
```
Question 9:

What is the difference between the + and * characters in regular
expressions?

Answer: *  matches zero or more of the preceeding group.
        + matches one or more of the preceeding group.

```
```
Question 10:

What is the difference between {3} and {3,5} in regular expressions?

Answer:{3} matches exactly 3 of the preceeding group.
       {3, 5} matches atleast 3 and atmost 5 preceeding groups

```
```
Question 11:

What do the \d, \w, and \s shorthand character classes signify in
regular expressions?

Answer:\d siginifies a digit, \w siginifies word and \s signifies space.

```
```
Question 12:

What do the \D, \W, and \S shorthand character classes signify in
regular expressions?

Answer:\D, \W, and \S match anything except a digit, word, or space character,
respectively.

```
```
Question 13:

What is the difference between .* and .*??

Answer: .* matches in a greedy way where as .* matches in a non greedy way.

```
```
Question 14:

What is the character class syntax to match all numbers and
lowercase letters?

Answer: 
```
```
Question 15:

How do you make a regular expression case-insensitive?

Answer: By pasing  re.IGNORECASE or re.I as a second argument to
re.compile()
```
```
Question 16:

What does the . character normally match? What does it match if
re.DOTALL is passed as the second argument to re.compile()?

Answer:. matches everything until a newline charecter is encountered wheras when r.DOTALL is passed . will match everything including the newline charectors.

```
```
question 17:

If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers,
11 pipers, five rings, 3 hens') return?

Answer:
```
```
Question 18:

What does passing re.VERBOSE as the second argument to re.compile()
allow you to do?

Answer:It tells the re.compile() function
to ignore whitespace and comments inside the regular expression string

```
````
Question 20:

How would you write a regex that matches a number with commas for
every three digits? It must match the following:
• '42'
• '1,234'
• '6,368,745'
but not the following:
• '12,34,567' (which has only two digits between the commas)
• '1234' (which lacks commas)

Answer: re.compile(r'^(\d{1,3}(,\d{3})*)$')
```
```
Question 21:

How would you write a regex that matches the full name of someone
whose last name is Watanabe? You can assume that the first name that
comes before it will always be one word that begins with a capital letter.
The regex must match the following:
• 'Haruto Watanabe'
• 'Alice Watanabe'
• 'RoboCop Watanabe'
but not the following:
• 'haruto Watanabe' (where the first name is not capitalized)
• 'Mr. Watanabe' (where the preceding word has a nonletter character)
• 'Watanabe' (which has no first name)
• 'Haruto watanabe' (where Watanabe is not capitalized)

Answer:re.compile(r'^[A-Z][a-z]*\sWatanabe'')


```
```
Question 22:

How would you write a regex that matches a sentence where the first word
is either Alice, Bob, or Carol; the second word is either eats, pets, or throws;
the third word is apples, cats, or baseballs; and the sentence ends with a
period? This regex should be case-insensitive. It must match the following:
• 'Alice eats apples.'
• 'Bob pets cats.'
• 'Carol throws baseballs.'
• 'Alice throws Apples.'
• 'BOB EATS CATS.'
Pattern Matching with Regular Expressions   185but not the following:
• 'RoboCop eats apples.'
• 'ALICE THROWS FOOTBALLS.'
• 'Carol eats 7 cats.'

Answer: re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|basballs)\.', re.I) .
```
