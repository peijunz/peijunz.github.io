---
title: Use C++ Template Programming to find int of least byte width
date: 2016-05-01
lang: en
tags: C++
---

Also see [gist](https://gist.github.com/peijunz/580c39932aed134c53c80d2c55101490)

```cpp
#include <iostream>
#include <cstdint>
template<int N>
struct least {
    static_assert(N < 9 && N > 1, "Length beyond range 1<N<9!");
    using int_ = typename least <N+1>::int_;
};
template<> struct least<1> {using int_ = int8_t;};
template<> struct least<2> {using int_ = int16_t;};
template<> struct least<4> {using int_ = int32_t;};
template<> struct least<8> {using int_ = int64_t;};

int main(){
    least<5>::int_ i5=666;
    printf("Size of i5 is %d\n", sizeof(i5));
}
```
