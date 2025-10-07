```bash
****************** Printing Vector Unit Statistics *******************
Vector Width:              2
Total Vector Instructions: 177512
Vector Utilization:        88.6%
Utilized Vector Lanes:     314616
Total Vector Lanes:        355024
****************** Printing Vector Unit Statistics *******************
Vector Width:              4
Total Vector Instructions: 102068
Vector Utilization:        83.6%
Utilized Vector Lanes:     341240
Total Vector Lanes:        408272
****************** Printing Vector Unit Statistics *******************
Vector Width:              8
Total Vector Instructions: 55374
Vector Utilization:        80.9%
Utilized Vector Lanes:     358600
Total Vector Lanes:        442992
****************** Printing Vector Unit Statistics *******************
Vector Width:              16
Total Vector Instructions: 28839
Vector Utilization:        79.7%
Utilized Vector Lanes:     367816
Total Vector Lanes:        461424
```

As the `VECTOR_WIDTH` increases, the vector utilization decreases. Because the larger vector width, the more likely the last vector lanes will have more masked positions. As the original masked position number in one SIMD instruction will be VECTOR_WIDTH-rem, where rem=N%VECTOR_WIDTH.

Besides, during computation, as the exponent value are not the same across different in one SIMD instruction, the masked position will become more when those scarce positions still have relatively large exponent values.