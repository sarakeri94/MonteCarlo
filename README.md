## Simulations
A simulation is an approximate imitation of the operation of a process or system that represents its operation over time.

In the context of data science, simulations are quite useful for performance tuning or optimizing a model.
This repositary includes different examples of simulations being used to solve puzzles and business cases

### Coins from a bag without replacement

Coins with values 1 through N (inclusive) are placed into a bag. All the coins from the bag are iteratively drawn (without replacement) at random. For the first coin, you are paid the value of the coin. For subsequent coins, you are paid the absolute difference between the drawn coin and the previously drawn coin.

For example, if you drew 5,3,2,4,1, your payments would be 5,2,1,2,3 for a total payment of 13.

'montecarlo_bag.py' proivides the Mean, SD and Distribution of this activity for any value 'N'
