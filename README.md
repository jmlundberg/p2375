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

## Topics and discussion of comments on revision R0:

*Many thanks to all who commented. I'd be happy to mention you with your permission.* Dates are question dates. I'm updating this page continuously.

### Meta: is there a draft for R1 ?

No. Still gathering comments. At the time of this writing I don't yet have something I know I should change in some specific way. Specific suggestions for R1 are very welcome!

### Is there's a need to require `nths` be `sized_range`? (2021-11-19)

Not sure, I don't think so. The example implementation does not use .size(). I first had a different answer to this but updated after further comments.

### Request for motivation. Performance benefits. (2021-11-21)

A basic **performance study** is done at
https://github.com/jmlundberg/nth_element_material/blob/main/PERFORMANCE.md.

### How should the `nths` be provided? (2021-11-21)

The current-standard single-nth version uses a single iterator `nth` to designate the location in the range. A range of iterators seems to me the most natural way to designate multiple arbitrary locations in a range.

To me, this is *least-surprise* and offers flexibility as well as natural combination with other operations (such as seen in the examples here and in the proposal). Python uses indices rather than iterators to express locations in lists and arrays, and its incarnation of the proposed algorithm uses range-of-indices (or a single value) to specify the partition point(s): [numpy.partition](https://numpy.org/doc/stable/reference/generated/numpy.partition.html).


### Request for motivation. What is the use of this. (2021-11-21)

The comment is appreciated.

Let's start with a description and motivation for the existence of the single `std::nth_element` that has been in the
C++ standard since the origins of the Standard Template Library. [STL, Stepanov and Lee 1995: The Standard Template Library](http://stepanovpapers.com/STL/DOC.PDF). There is no explicit motivation for each of the algorithms from this time, but the motivation can be stated as: Significantly faster sorting (often many times faster), when you don't need the whole container sorted.
In this specific sense it's in the same category as `std::partial_sort`.

An interesting discussion of `std::sort` vs single-nth `std::nth_element` and `std::partial_sort` is found at [CppCon 2018: Fred Tingaud "A Little Order: Delving into the STL sorting algorithms"](https://www.youtube.com/watch?v=-0tO3Eni2uo)

*This* proposal extends the usability of `std::nth_element` to multiple `nths`. Just as with the current standard single-nth version of `nth_element` the purpose is **faster operation**, but just as with the single-nth version, there is
additional **semantic clarity** in performing only the required partitioning. The paper shows examples of various
partitioning problems.

The semantics of the algorithm is that it partitions a range (let's say a vector v) into any number of partitions. The range (v) is arranged so that at the partition points, the elements are such as if the whole range was sorted. The elements are also arranged so that the elements before any partition point are less than or equal to the value at that partition point. That is, the data (v) is arranged into groups of pre-determined sizes based on some specified ordering, but the order within each partition (between the partition points) is not specified.

The examples below are taken from the paper (P0) with some additional comments. Additional examples are marked as such.
**Current alternatives to *this* proposal are either at least somewhat hard to write correctly and/or less performant**.
Note: [performance study](https://github.com/jmlundberg/nth_element_material/PERFORMANCE.md).

#### Application example 1

Eg: Partitioning a bunch
of ponies into several *age* groups, then sort *one* group by *name*.

```
struct Pony{
  double littleness;
  chrono::duration age;
  string name;
};
auto end=nth_elements(v, nths, std::greater{}, Pony::age);
std::sort(nths[3], nths[4], std::less{}, Pony::name);
```

#### Application example 2

Context: partitioning into a fixed number of slots
```
vector<decltype(v)::iterator> nths;
for(size_t slot=1; slot<16 ; ++slot){
  nths.push_back(v.begin()+ min(slot*2048,N));
}
```
or at some other arbitrary iterators in the inclusive range `[first,last]` such as
`auto nths=vector{v.begin()+25,v.begin()+100,v.begin()+1000};`

##### "After" Simple and O(N)

With this proposal, the partitioning is:
```
nth_elements(v, nths, pred);
```

The partitions can then be independently processes further as each pair of consecutive iterators in `nths` span an ordinary half-open range of that partition.

##### "Before - Alternative 1a": Hand-wired bisection for nths of known size. O(N) but messy

```
nth_element(v.begin(), nths[1], v.end(), pred);
nth_element(v.begin(), nths[0], nths[1], pred);
nth_element(nths[1]+1, nths[2], v.end(), pred);
```

Did we get this right? Is it correct for repeated nths or empty v?

##### "Before - Alternative 1b": Hand-wired for size 3. O(N ·M)

```
nth_element(v.begin(), nths[0],v.end(), pred);
nth_element(nths[0], nths[1], v.end(), pred);
nth_element(nths[1], nths[2], v.end(), pred);
```

Did we get this right?

##### "Before - Alternative 2": Simple but O(N log N):

```
sort(v,pred);
```

#### Outlier filtering (not mentioned in R0)

With two partitioning points, the lowest a, and highest b elements are excluded from a range in constant time with a single call to the proposed extension.

#### Pagination, visiting sorted subset. (not mention in R0)

A small sorted windows into a large data set can be selected as if sorted by partitioning at two points. For example, if `j` items fit on a display page, we can jump to page `k`, that is, into the range from `a=v.begin()+j*k` to `b=v.begin()+j*(k+1)`:
```
std::nth_element({a,b}, v);
processPage(a,b); // May also now sort the small subrange with std::sort(a,b);
```
An option is to pre-partition into all pages, exactly as the *slots* example above.

#### Partitioning with interpolation. Quantiles. Percentiles. Median. (further comments here in addition to R0)

The paper also explains how the proposal can be used to implement calculation of quantiles.

Further comments:

The current standard single-nth `std::nth_element` is actually not enough to calculate even a single quantile point, such as the median. At least not in the way that is often preferred: For example the [median](https://en.wikipedia.org/wiki/Median) of an even number of elements is typically taken  to be the mean of the two central elements. With the range-of-nth `nth_element` version single or multiple quantiles can be calculated efficiently.

It's also a common situation to calculate more than one quantile, such as min, 25%, 50% (median), 75%, max. This requires 5 to 8 partition points depending on the size of the data. With *this* proposal this can be done in `O(N)`. Also note wikipedia on [Percentiles](https://en.wikipedia.org/wiki/Percentile), and [Estimating quantiles from a sample](https://en.wikipedia.org/wiki/Quantile#Estimating_quantiles_from_a_sample).

#### Example: Histogram / Data / Image Equalization (not mention in R0)

Found at https://github.com/jmlundberg/nth_element_material/blob/main/plotting/examples/partition_based_image_equalization.md

Orgininal vs image equalization using `range-of-nths`, `m=5`

<img alt="alt_text" width="38%" src="https://github.com/jmlundberg/nth_element_material/blob/main/plotting/examples/forsen.png?raw=true" /> <img alt="alt_text" width="38%" src="https://github.com/jmlundberg/nth_element_material/blob/main/plotting/examples/forsen_partition5.png?raw=true" />
