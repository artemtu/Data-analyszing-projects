# E-commerce. Prioritization of hypotheses and analysis of a/b - test

Tasks:
We should prioritize hypotheses and analyze the results of the a/b test

1. Prioritize hypotheses:
 * Prioritize hypotheses on the "ICE" and sort them in descending
 * Prioritize hypotheses on the "RICE" and sort them in descending
 * Which hypothesis is preferable? And why?
2. A/B - test:
 * Create a plot  of cumulative revenue by the groups
 * Create a plot of cumulative AOV by the groups
 * Create a plot with changes in cumulative revenue from group "B" to group "A"
 * Create a plot of cumulative conversion by the groups
 * Create a plot with changes in cumulative conversion  from group "B" to group "A"
 * Create a scatter plot quantity of orders by users
 * Count 95 and 99 percentiles of the quantity of the orders by a user. Choose a limit for anomalies users
 * Create a scatter plot of the order price
 * Count 95 and 99 percentiles of the orders price
 * Count statistical significance between conversion in the groups by "raw" data
 * Count statistical significance between AOV in the groups by "raw" data
 * Count statistical significance between conversion in the groups by processed data
 * Count statistical significance between AOV in the groups by processed data
3. Take a decision:
 * Finish the test, and fixate a victory of one group
 * Finish the test and fixate no difference between groups
 * Continue test

**Description of the data:** 
- hypothesis.csv - nine hypotheses with parameters: Reach, Impact, Confidence, Effort

- orders.csv and visitors.csv - results of the A/B -test

## Short conclusion

We can finish and fixate on the victory of group "B". This group has higher conversion and is stable. Group "A" has more AOV by 2% in processed data, but group "B" give us more buyers because conversion higher


