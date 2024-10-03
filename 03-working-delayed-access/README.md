# Delayed access (fully working)

A quick search online will yield a few options for how to deal with circular type dependencies. Those include:

1. Wrapping the type in quotes.
2. Enabling postponed evaluation.

Those two methods work pretty much the same way: Type annotations are treated
by Python as strings until they are executed, and only the would the actual
type get evaluated.

For simplicity's sake, let's just wrap the type in quotes.

Once we do, we finally have everything a working example.

Running `main.py` works as expected and prints:
```
B(1)
A(2)
```
