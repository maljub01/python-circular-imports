# Things get messy

The combination of type checking import guards and delayed imports worked great
for our toy example. We got it working and even saved ourselves from having to
import `A` except when we really need it.

However, in the real world, things can get pretty complicated:
1. We often need to use the same dependency in lots of places. It's not going to
   make sense for us to repeat the same import statement everywhere we need to
   use one. Things can get messy really quickly.
2. We don't really have a good systematic way to figure out whether an import
   should be a normal one or a delayed one. We probably start out with all
   imports being regular imports until we hit a circular import, at which point
   we would switch some of them to be delayed imports in order to fix the issue.

In this example, we add a new module `c.py`. `C` depends on `A` in a couple of
locations. Seems simple enough.

We even use `C` in our `main.py`. We run it and confirm that everything is
working:

```
B(1)
A(2)
A(3)
```
