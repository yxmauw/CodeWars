# DESCRIPTION:
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

<img src=https://i.imgur.com/lk5vJ7sm.jpg>

Can you translate this drawing into an algorithm?

__You will be given two dimensions__

1. a positive integer length
1. a positive integer width \n
You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

## Examples in general form:
(depending on the language)
  ```
  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
 
  You can see examples for your language in **"SAMPLE TESTS".**
  ```
## Notes:
`lng == wdth` as a starting case would be an entirely different problem and the drawing is planned to be interpreted with `lng != wdth`. (See kata, [Square into Squares. Protect trees!](http://www.codewars.com/kata/54eb33e5bc1a25440d000891) for this problem).

When the initial parameters are so that `lng` == `wdth`, the solution `[lng]` would be the most obvious but not in the spirit of this kata so, in that case, return `None`/`nil`/`Null`/`Nothing`.
