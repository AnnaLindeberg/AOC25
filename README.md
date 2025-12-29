# Advent of Code 2025
December has started, I forgot, but let's go! The initial idea was to learn Rust by doing but now I think that will take too much time. Instead, It'll be python, hacky and fast. 

## Day 1: Secret Entrance
Day one and mistake one: open the big input file and do not assume your integers lie in the range [0,99].

## Day 2: Gift Shop
OK I completely overenginered the first part and then wrote a reasonable 15 lines of code to solve both parts instead. A little bit bruteforce-ing all possible invalid IDs and then checking if they appear in one of the ranges but that's, on the other hand, fast enough to work and easy to grasp.

## Day 3: Lobby
Actually easier than both day 1 and 2.

## Day 4: Printing Department
First graph problem on day four is nice. It's also easy to solve with networkx!

## Day 5: Cafeteria
I "merged" the given ranges to check containment and length of the ranges. I'm pretty sure that I've written the merging-code for AOC some earlier year... 

## Day 6: Trash Compactor
This was mostly about parsing strings, which is maybe not the most fun part of AOC. Python has no `prod` function (unlike built-in `sum`), I wonder why? Maybe it's just useful for this type of recreational coding, though...

## Day 7: Laboratories
This was a fun one! The first part I calculated top-down, keeping track of the beam-positions in the row above only and simply counting each time a beam split. For the second part, I work bottom-up instead, keeping an array consisting of the number of different paths that exist below a certain x-position. These initialize to 1, and then get zero'd when they are right under a splitter. Right above a splitter, the number of paths is just the sum of the number of paths going left resp. right. Quite neat and straightforward – dynamic programming I'd say, or?

## Day 8: Playground
Ahh hm my slowest solve so-far this year, and mostly because I misinterpreted how to count to the first 10/1000 added connections. When I figured that out, the second part was more or less just an additional if-clause. The runtime is rather slow though, due to the computation of *all* pairwise distances. I think one can use the triangle inequality and some tricks to avoid computing some of them but I couldn't be bothered...

## Day 9: Movie Theatre
I have a very clear recollection that AOC has stumped me with these polygon-shape things before! First part is an easy solve but the solution to part 2 is way to slow to compute. 

Update: came back and "compressed" the given coordinates, so that each coordinate correspond to a rectangle in the actual input. This was just barely enough to get it to run in ~30 seconds, which is good enough for me. In particular it means that I didn't have to exploit that the input polygon had a very particular shape...

## Day 10: Factory
First part with a BFS run. Second part is unfeasable to do that way, probably need some linear programming. For another time...

Update: indeed so! Since I don't think I've ever bothered with trying to approach LP I just read the scipy-docs for `optimization` and solved with a neat `mips` function. Cool!

## Day 11: Reactor
A straight-off graph problem that I can solve! Nice


## Day 12: Christmas Tree Farm
Sounded completely ridiculous to solve (like ever) but I scrolled passed some jokes on the AOC subreddit and just did the bare bone check of wheter so-and-so many 3x3 blocks fit in each given region. That's the answer and I have my first full advent of code! Granted, only 12 days, but still!

