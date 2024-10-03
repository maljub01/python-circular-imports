# A simple but broken example

This is a simple motivating example. It shows a couple of simple classes that have a circular dependency.

Notice, however, that this is not a circular dependency in terms of evaluation
(i.e. there is no circular logic anywhere in terms of evaluation). However, it
is a circular dependency in terms of definitions.

Attempting to run `main.py` will result in the following error:

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from a import A
  File "a.py", line 1, in <module>
    from b import B
  File "b.py", line 1, in <module>
    from a import A
ImportError: cannot import name 'A' from partially initialized module 'a' (most likely due to a circular import) (a.py)
```

This happens because, while evaluating `b.py`, we encounter the statement `from a import A`.
However, we only got as far as line 1 when evaluating A, which means that the name 'A' has
not yet been added to that module, and is therefore not available for us to import.

There are several options available for us here. Let's explore them.
