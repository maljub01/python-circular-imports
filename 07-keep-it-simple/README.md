# Keep it simple

Instead of relying on a manually curated, ad-hoc combination of delayed
imports, we can go back to the solution we had in the 3rd example.

Let's also enable postponed evaluation everywhere so we don't have to worry
about putting quotes around types. We do this by adding `from __future__ import
annotations` to the top of every file we have.

Our code is now much more sensible and readable. We don't have to worry about
whether any particular import needs to be delayed or not, and we also don't
have to worry about runtime or definition circularlity causing our app to
crash!

The only cost here is that imported names are slightly longer now, but that
doesn't seem so bad compared to what we had to deal with before.
