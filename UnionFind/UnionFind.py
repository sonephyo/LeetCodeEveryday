# Python3 program to implement Disjoint Set Data Structure.

class Solution:
    def __init__(self, n):
        # Constructor: Initialize sets of n items.
        # rank: Store the depth of trees (used for union by rank).
        self.rank = [1] * n
        # parent: Store the parent of each item. Initially, every item is its own parent.
        self.parent = [i for i in range(n)]

    def find(self, x):
        # If x is not its own parent, then it's not the representative of its set.
        if self.parent[x] != x:
            # Path Compression: Connect x directly to its set's representative.
            self.parent[x] = self.find(self.parent[x])
        # Return the representative of the set.
        return self.parent[x]

    def Union(self, x, y):
        # Find the representatives (or the root nodes) for x and y.
        xset = self.find(x)
        yset = self.find(y)

        # If x and y are already in the same set, return.
        if xset == yset:
            return

        # Union by Rank:
        # Attach the tree with a smaller rank under the root of the tree with a larger rank.
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        # If ranks are the same, choose one tree and increment its rank.
        else: 
            self.parent[yset] = xset
            self.rank[xset] += 1

# Driver code
if __name__ == "__main__":
    # Create a disjoint set data structure with 5 elements.
    obj = Solution(5)
    # Merge sets that contain 0 and 2.
    obj.Union(0, 2)
    # Merge sets that contain 4 and 2.
    obj.Union(4, 2)
    # Merge sets that contain 3 and 1.
    obj.Union(3, 1)
    # Check if 4 and 0 are in the same set.
    if obj.find(4) == obj.find(0):
        print('Yes')
    else:
        print('No')
    # Check if 1 and 0 are in the same set.
    if obj.find(1) == obj.find(0):
        print('Yes')
    else:
        print('No')
