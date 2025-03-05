# Race 2 - ID3 Parameters, Optimization

DUE: 3/16

## REQUIREMENTS

We will be improving upon the algorithm from race 1 by adding parameters, and performing a grid search against one another.

As before, your algorithm must perform ID3 properly - that is, evaluate all required splits and evaluate based on entropy.

However, you must implement 5 additional parameters for your tree, and then perform a tuning run FROM SCRATCH to maximize performance.

The following parameters MUST be implemented, encoded in a std::map that is passed into your tree:

`min_samples_split` - integer, number of samples needed to generate a split. If the number of samples being considered is lower, then 
you must generate a leaf.

`min_samples_leaf` - integer, number of samples in both leaves when splitting in order to actually create a split. To be clear - all 
resulting branches must have at least this number of samples for the split to be considered valid.

`max_depth` - integer, pretty self explanator - the tree can only grow to a max depth of this value.

`max_features` - either SQRT or NONE. The number of features considered at any split point - if SQRT, then only a random subset of valid
remaining possible features of size SQRT(<number of total features>) can be considered.

`splitter` - either BEST or RANDOM. If random, then you must implement a top-k split selection method, with k being statically set to 3 for this race.
This means that every time a split is selected, you must randomly choose between the top k, if splitter is set to random.

For hyperparameter tuning, you can use any method that you desire, though we will be restricting total runtime on the validation set
to 10 minutes. Any optimization target is allowed. Ensure your configs are trained FROM SCRATCH.

## REFERENCE
No outside reference is allowed for parameter details or implementations. The wikipedia page on hyperparameter tuning is permitted.
https://en.wikipedia.org/wiki/Hyperparameter_optimization

## TESTING
All 4 of the same datasets from Race 1 will be considered once again.

## SCORING

The exact scoring breakdown will not be revealed prior to the race. However, the following measurements will be considered: 
Hyperparameter optimization time. Mean Train time. Mean Inference time. Train-Test-Split Accuracy. Each metric will be calculated
as the average number of standard deviations each tree is from the highest scoring time in that category - with the lowest value being 0.
Lowest weighted score will win.

Additionally, 4 configurations will be provided 24 hours before the beginning of the race - you must confirm your tree can run correctly
and prove that those 4 configurations are being applied to qualify for racing. 


## SUBMISSION

The file `tree.hpp` has been provided, outlining the required API you must implement. The exact submission code will be released at a later date,
but the general flow is as follows:
- Call (and time) Tuning Code (ms)
- Generate and infer for 1000 iterations on train test split, similar to race 1. (us)

No computation may be performed outside of the outlined functions.


