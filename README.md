# Python circular imports

Sometimes, different modules can end referring to one another in a circular manner. Most of the time, those circular
dependencies are caused by circular type annotations rather than genuinely circular logic.

The goal here is to explain why this problem happens, demonstrate an example of it and use it to explore some options
for dealing with it, before settling on the best one.

## How imports work

It is important to first keep in mind how Python imports work.

When a module is imported in Python:
1. First, `sys.modules` is checked to confirm if that module has already been imported before.
   * We skip the rest of the importing logic if the module has been imported before and
     make the newly imported module reference point at `sys.modules[name]`.
3. Otherwise, a new `module` object is created and added to `sys.modules`.
5. The module's code is then immediately evaluated, including any transitive imports.
   * While evaluating the module, every new top-level definition gets added to the module's `module` object.


During evaluation, modules will attempt to access definitions from each other. Python allows this to happen
even when those modules have not been fully initialized. However, if an attempt is made to access a definition
from a partially initialized module, and the name is not found. Python will throw an `ImportError` and explain
that this is likely to have been caused by a circular import.
