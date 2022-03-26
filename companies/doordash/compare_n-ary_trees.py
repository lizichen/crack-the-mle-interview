"""
https://www.1point3acres.com/bbs/thread-779975-1-1.html

树的结构如下：
class TreeNode(object):
  key = str
  value = str
  children = List[TreeNode]
def compute_diff(old_tree: TreeNode, new_tree: TreeNode) -> int:
  pass
一些判定规则如下（面试时请与面试官clarify，不要上来就说是这样，至少要会演）：
1. 如果node key一样，value一样，视为同一个节点。
2. 如果node key一样，value不同，视为不同节点，但树的结构保持不变。
3. 如果node key不同，则视为完全不同的两棵树，答案应该返回这两棵树里一共有多少节点。
4. children数组里的顺序无关。

"""

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

class Solution:
    def findDiffNode(self, root1, root2):
        if root1 is None and root2 is None:
            return 0
        
        if root1 is None or root2 is None or root1.key != root2.key:
            return self.countNode(root1) + self.countNode(root2)
        
        diff = 0
        
        if root1.value != root2.value:
            diff += 2
        
        child1_map = {}
        for child in root1.children:
            child1_map[child.key] = child
        
        child2_map = {}
        for child in root2.children:
            child2_map[child.key] = child

        all_children_key = set(child1_map.keys()).union(set(child2_map.keys()))
        for child_key in all_children_key:
            diff += self.findDiffNode(child1_map[child_key], child2_map[child_key])
        
        return diff
        

    def countNode(self, node):
        if node is None:
            return 0
        
        count = 1
        for child in node.children:
            count += self.countNode(child)
        
        return count
