
class Solution:
  def solveKnapsack(self, profits, weights, capacity):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return self.knapsack_recursive(dp, profits, weights, capacity, 0)


  def knapsack_recursive(self, dp, profits, weights, capacity, currentIndex):

    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
      return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
      return dp[currentIndex][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
      profit1 = profits[currentIndex] + self.knapsack_recursive(
        dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = self.knapsack_recursive(
      dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


