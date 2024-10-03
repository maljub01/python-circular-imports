# Delayed access at the point of failure

One way we can try to fix this issue is to address the immediate problem at hand.

We can't import `A` from module `a`, because it still has not been fully
evaluated yet. So why not just `import a` for now and only access `a.A` when we
need it?

This version of the code does exactly that by patching `b.py` to make the relevant change.

However, even after making this change, we will still hit the same problem. Our
code tries to access `a.A` while defining `get_a` and that fails for the same
reason:

```
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/Users/marwan/gist.github.com/python-circular-imports/02-delayed-access-still-broken/main.py", line 1, in <module>
    from a import A
  File "/Users/marwan/gist.github.com/python-circular-imports/02-delayed-access-still-broken/a.py", line 1, in <module>
    from b import B
  File "/Users/marwan/gist.github.com/python-circular-imports/02-delayed-access-still-broken/b.py", line 4, in <module>
    class B:
  File "/Users/marwan/gist.github.com/python-circular-imports/02-delayed-access-still-broken/b.py", line 8, in B
    def get_a(self) -> a.A:
                       ^^^
AttributeError: partially initialized module 'a' has no attribute 'A' (most likely due to a circular import)
```

We may notice at this point that we don't *really* need to use `a.A` here
though. It's just a type annotation.

Surely, there must be a way to resolve circular type dependencies.
