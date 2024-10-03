# An even better delayed access

At this point, we may be pretty happy with ourselves and decide to optimise things even more.

We may notice that we only need `a.A` when `get_a` is called. So why not avoid
importing the module `a` altogether until we *really* need it.

To do this, we:
1. Quote the type to avoid Python trying to evaluate it at definition time.
1. Have a top-level import for `A`, but only when type checking to stop type checkers from complaining that they can't find it.
2. Import `A` when running `get_a`.

We find that this approach also works pretty well:
```
B(1)
A(2)
```
