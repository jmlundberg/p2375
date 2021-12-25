# Generalisation of nth_element to a range of nths

## P2375R0 2021-05-14

This is an ISO C++ proposal adding overloads to
[`std::nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element) and
[`std::ranges::nth_element`](https://en.cppreference.com/w/cpp/algorithm/ranges/nth_element)
for a *range* of nths.

latest wg21 link:

- https://wg21.link/p2375r0

Tracker:

- https://github.com/cplusplus/papers/issues/1045

Contact

lundberj@gmail.com , or at https://www.includecpp.org/discord/, or https://www.linkedin.com/in/johanml/


### Meta: is there a draft for R1 ?

Yes: https://isocpp.org/files/papers/D2375R1.pdf

Draft R1 incorporates: Added clarifications and more background, explanations, wording clarifications,
references, summarized performance study, applications, more questions/answers.

### Performance study

A basic **performance study** is done at
https://github.com/jmlundberg/nth_element_material/blob/main/PERFORMANCE.md.

### Example: Histogram / Data / Image Equalization (not mention in R0)

Found at https://github.com/jmlundberg/nth_element_material/blob/main/plotting/examples/partition_based_image_equalization.md

Orgininal vs image equalization using `range-of-nths`, `m=5`

<img alt="alt_text" width="38%" src="https://github.com/jmlundberg/nth_element_material/blob/main/plotting/examples/forsen.png?raw=true" /> <img alt="alt_text" width="38%" src="https://github.com/jmlundberg/nth_element_material/blob/main/plotting/examples/forsen_partition5.png?raw=true" />

## Older material relating to version R0

Many thanks to all who commented. I'd be happy to mention you with your permission.*

**This material has been incorporated (in slightly different and fewer words) in R1 but is kept here for reference.** The older material was moved to [OLDER_MATERIAL.md](OLDER_MATERIAL.md).
