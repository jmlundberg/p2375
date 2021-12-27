# Generalisation of nth_element to a range of nths

## P2375

This is an ISO C++ proposal adding overloads to
[`std::nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element) and
[`std::ranges::nth_element`](https://en.cppreference.com/w/cpp/algorithm/ranges/nth_element)
for a *range* of nths.

#### Latest published version:

- https://wg21.link/p2375r0

#### Latest draft:

https://isocpp.org/files/papers/D2375R1.pdf (remember to refresh your browser)

Draft R1 incorporates: Added clarifications and more background, explanations, wording clarifications,
references, summarized performance study, applications, more questions/answers.

#### Tracker:

- https://github.com/cplusplus/papers/issues/1045

#### Contact

lundberj@gmail.com , or at https://www.includecpp.org/discord/, or https://www.linkedin.com/in/johanml/

### What even *is* nth_element !?

As an example data, consider the permuted integers [100,126) at index [0,26) and the sorted counterpart:

<img width="59%" src="plotting/figs/rnd.png?raw=true">

<img width="59%" src="plotting/figs/sort.png?raw=true">

#### Single-nth nth_element

What the current-standard {std::nth_element} does is to arrange and partition the data (as described in the standard and in P2375). For example, with {nth = begin+7}, the element in the position pointed to by nth is the element that  would  be  in  that position if the whole range were sorted, and all subsequent values are no less than that value:

<img width="59%" src="plotting/figs/1a.png?raw=true">,

or for {nth = begin+20}:

<img width="59%" src="plotting/figs/1b.png?raw=true">.

#### Multi-nth nth_element

This proposal adds the possibility to provide a range of nths, such as {begin+7,begin+20} :

<img width="59%" src="plotting/figs/2.png?raw=true">

or at {7,12,20}:

<img width="59%" src="plotting/figs/3.png?raw=true">

or  at {5,6,14,15}:

<img width="59%" src="plotting/figs/qs.png?raw=true">

### Performance study

A basic **performance study** is done at
https://github.com/jmlundberg/nth_element_material/blob/main/PERFORMANCE.md.

### Example: Histogram / Data / Image Equalization (not mention in R0)

Found at https://github.com/jmlundberg/nth_element_material/blob/main/plotting/examples/partition_based_image_equalization.md

Orgininal vs image equalization using `range-of-nths`, `m=5`

<img width="38%" src="plotting\examples\forsen_roundtrip.small.jpg?raw=true" /> <img width="38%" src="plotting\examples\forsen_partition5.small.jpg?raw=true" />

## Older material relating to version R0

Many thanks to all who commented. I'd be happy to mention you with your permission.*

**This material has been incorporated (in slightly different and fewer words) in R1 but is kept here for reference.** The older material was moved to [OLDER_MATERIAL.md](OLDER_MATERIAL.md).
