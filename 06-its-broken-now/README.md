# It's broken now

Turns out, `B` will also need to have a small runtime dependency on `C`.

That should be a relatively simple change.

However, after we make the change, we hit that same circular import issue again:

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from a import A
  File "a.py", line 1, in <module>
    from b import B
  File "b.py", line 3, in <module>
    from c import C
  File "c.py", line 1, in <module>
    from a import A
ImportError: cannot import name 'A' from partially initialized module 'a' (most likely due to a circular import) (a.py)
```

Now what?
