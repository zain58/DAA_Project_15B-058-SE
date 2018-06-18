# DAA_Project_15B-058-SE
inventory planning
The Rinky Dink Company makes machines that resurface ice rinks. The demand for such products varies from month to month, and so the company needs to develop a strategy to plan its manufacturing given the fluctuating, but predictable, demand. The company wishes to design a plan for the next n months. For each month i, the company knows the demand di, that is, the number of machines that it will sell. Let D = ?ni=1 (di) be the total demand over the next n months.

The company keeps a full-time staff who provide labor to manufacture up to m machines per month. If the company needs to make more than m machines in a given month, it can hire additional, part-time labor, at a cost that works out to c dollars per machine. Furthermore, if, at the end of a month, the company is holding any unsold machines, it must pay inventory costs. The cost for holding j machines is given as a function h(j) for j = 1,2,...,D, where h(j) >= 0 for 1 <= j <= D and h(j) <= h(j+1) for 1 <= j <= D-1.

In INVENTORY-PLANNINGINVENTORY-PLANNING, we build the solution month by month, starting from month nn, moving backward toward month 11. First, we solve the subproblem for the last month, for all surpluses. Then, for each month and for each surplus entering that month, we calculate the cheapest way to satisfy demand for that month based on the solved subproblems of the next month.
•	f is the number of machines that we try to manufacture in month k.
•	cost[k,s] holds the cheapest way to satisfy demands of months k,…,n with a net surplus of s left over at the beginning of month k
•	make[k,s] holds the number of machines to manufacture in month k and the surplus s of an optimal plan. We will use this table to reconstruct the optimal plan.
We first initialize the base cases, which are the cases for month n starting with surplus s, for s=0,…,D. If dn>s, it suffices to manufacture dn−s machines, since we need not keep any surplus after month n. If dn≤s we need not manufacture any machines at all.
We then calculate the total cost for month n as the sum of hiring extra labor c⋅max(f−m,0)and the inventory costs for leftover surplus h(s+f−dn), which can be nonzero if we had started out with a large surplus.
The outer for loop of the next block of code runs down from month n−1 to 1, thus ensuring that when we consider month k, we have already solved the subproblems of month k+1.
The next inner for loop iterates through all possible values of ff as described.
For every choice of ff for a given month k the total cost of (k,s) is given by the cost of extra labor (if any) plus the cost of inventory (if there is a surplus) plus the cost of the subproblem (k+1,s+f−dk). This value is checked and updated. Finally, the required answer is the answer to the subproblem (1,0), which appears in cost[1,0]cost[1,0]. That is, it is the cheapest way to satisfy all the demands of months 1,…,nwhen we start with a surplus of 0.
The running time of INVENTORY-PLANNINGINVENTORY-PLANNING is clearly O(nD2). The space requirement is O(nD). We can improve upon the space requirement by noting that we need only store the solution to subproblems of the next month. With this observation, we can construct an algorithm that uses O(n+D) space.




Instruction:
this is a python code it will run on pycharm software.
