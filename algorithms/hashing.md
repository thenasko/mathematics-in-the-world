## Hashing

Before we get to hashing, let's first take a look at *arrays* (also called *lists* in Python). Consider an array $$A$$ consisting of $$n \geq 1$$ elements (say numbers). We can access them as $$A[0], \dots, A[n-1]$$, and both reads and writes take constant time. We can think of the array as a map (function)
$$
A \colon\; \{ 0, \dots, n-1 \} \longrightarrow \textrm{Values}.
$$
While that sounds like a useful structure, it is also a very rigid one. What about adding or removing elements? What if we would like to use indexes other than the numbers from $$0$$ to $$n-1$$?

The [hash table](http://en.wikipedia.org/wiki/Hash_table) is a data structure which solves a lot of these problems. Without going into the inner workings of a hash table, we can think of such an object as a map
$$
B \colon\; \textrm{Keys} \longrightarrow \textrm{Values}.
$$
The keys (indexes) can be numbers, strings, or a variety of other objects. While allowing such diverse keys is often a plus, that also means that we have no sense of order between them. Put formally, the set of keys is non-ordered. On the positive side, reading, writing, adding, and removing elements are all constant time operations (on average).

Hash tables in Python are called *dictionaries*, and they are almost as easy to use as lists. For example, the following code creates an empty dictionary ```ages```, and adds to entries to it.
```
ages = {}
ages["cat"] = 4
ages["dog"] = 2
```
The same dictionary can equivalently be initialized directly in one line.
```
ages = { "cat": 2, "dog": 2 }
```


### Finding summands

> Given an array $$A$$ and an integer $$n$$, find elements $$a$$ and $$b$$ of $$A$$ such that $$a + b = n$$.


### Unique elements

> Given a list of integers, remove all duplicates from it.


### Word frequency

> Given an body of text, construct a list of all words that appear in it together with their frequencies.


### Finding anagrams

> Two words are called *anagrams( if one can be obtained from the other by rearranging its letters. For example, "listen" and "silent" are anagrams. Given a dictionary of words, split it into groups such that each consists of words that are anagrams of each other.
