# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        print(self.val, "[")
        for n in self.neighbors:
            print(n.val)
        print("]")

class Solution(object):
    def cloneGraph(self, node):

        dict = {}
        return self.clone(node, dict)


    def clone(self, node, dict):
        if not node:
            return

        if node in dict:
            return dict[node]

        copy = Node(node.val)
        dict[node] = copy

        for n in node.neighbors:
            copy.neighbors.append(self.clone(n, dict))

        return copy

            
        

solution = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

print(solution.cloneGraph(node1))