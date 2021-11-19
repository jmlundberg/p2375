## Generalisation of nth_element to a range of nths

#### P2375R0 2021-05-14

This is an ISO C++ proposal adding overloads to
[`std::nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element) and 
[`std::ranges::nth_element`](https://en.cppreference.com/w/cpp/algorithm/ranges/nth_element)
for a *range* of nths.

latest wg21 link:

- https://wg21.link/p2375r0

Tracker:

- https://github.com/cplusplus/papers/issues/1045

Contact lundberj@gmail.com, or at https://www.includecpp.org/discord/

#### Feedback on R0:

* Is there's a need to require `nths` be `sized_range`? (2021-11-19)

Reaction/Lundberg: I think that's correct. That is, `nths` in the new overloads for `std::ranges::nth_element` should be `sized_range`, not `random_access_range`.
