```
Question 1:

What is []?

Answer : [] is an empty list.
```
```
Question 2 

How would you assign the value 'hello' as the third value in a list stored
in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

Answer : spam.insert(2, 'hello')

```
```
For the following three questions, let’s say spam contains the list ['a',
'b', 'c', 'd'].
```
```
Question 3:

What does spam[int(int('3' * 2) // 11)] evaluate to?

Answer : 'd'

```
```
Question 4:

What does spam[-1] evaluate to?

Answer : 'd'
```
```
Question 5:

What does spam[:2] evaluate to?

Answer : ['a', 'b']

```
```
For the following three questions, let’s say bacon contains the list
[3.14, 'cat', 11, 'cat', True].
```
```
Question 6:
What does bacon.index('cat') evaluate to?

Answer: 1
```
```
Question 7:

What does bacon.append(99) make the list value in bacon look like?

Answer: [3.14, 'cat', 11, 'cat', True, 22]
```
```
Question 8:

What does bacon.remove('cat') make the list value in bacon look like?

Answer: [3.14, 11, 'cat', True]
```
```
Question 9:

What are the operators for list concatenation and list replication?

Answer: + is the operator for list concantination and * is the operator for list replication.

```
```
Question 10:

What is the difference between the append() and insert() list methods?

Answer: append is used to add a new value to list from the back and insert is used to add a value at a specific index in the list
```
```
Question 11:

What are two ways to remove values from a list?

Answer: list_name.remove(element) this is to remove a specific element
        list_name.pop() this is to remove the last element 
```
```
Question 12:

Name a few ways that list values are similar to string values.

Answer: We can access specific charecters using index like we access elements of list 
        zero based indexing 
```
```
Question 13:

What is the difference between lists and tuples?

Answer: tuples are declared with () instead of [] like in lists. 
        tuples are immutable while lists are not
```
```
Question 14:

How do you type the tuple value that has just the integer value 42 in it?

Answer: a = (42, )
```
```
Question 15:

How can you get the tuple form of a list value? How can you get the list
form of a tuple value?

Answer: Using the list() function .

```
```
Question 16:

Variables that “contain” list values don’t actually contain lists directly.
What do they contain instead?

Answer:They contain references to the list.
```
```
Question 17:
What is the difference between copy.copy() and copy.deepcopy()?

Answer: copy.copy() is used to make a copy of mutable value like list or dictionary,
we use copy.deepcopy() when the list we want to copy contains lists in it as elements.
```


