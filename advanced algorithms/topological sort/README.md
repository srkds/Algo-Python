## Topological sort

**Defination**

Given a directed acyclic graph, topological sort is ordering of vertices of this graph suh that for every edge `u`,`v` going from `u` to `v`, `u` should always appear before `v` in the ordering.

**Application**

One of the application of topological sort is build systems.

Let's say `package D` depends on `package B` and `package A`.

How build system knows which package to build first?

So what it does is builds a graph of packages and apply topological sorting and creates the ordering.

And then builds packages in these order like first build `package A`, then `package B`, and then `package D`.
