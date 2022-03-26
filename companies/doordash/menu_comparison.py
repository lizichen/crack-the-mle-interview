"""
https://leetcode.com/discuss/interview-question/1367130/doordash-phone-interview/1026887

At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree. A menu can have many categories; each category can have many menu_items; each menu_item can have many item_extras; An item_extra can have many item_extra_options…
"""


class Node:
    def __init__(self, key, val, active):
        self.key = key
        self.val = val
        self.active = active
        self.children = []
        
    def is_same(self, node):
        if not node:
            return False
        return self.key == node.key and self.val == node.val and self.active == node.active
    
    @staticmethod
    def get_children_map(node):
        m = {}
        if node is None:
            return m

        for ch in node.children:
            m[ch.key] = ch
        return m
    
    def __str__(self):
        return self.key + " " + str(self.val) + " " + str(self.active)
        
class Solution:
    def get_modified_items(self, old_menu, new_menu):
        
        if old_menu is None and new_menu is None:
            return 0
        
        total_diff = 0
        if old_menu is None or new_menu is None or not old_menu.is_same(new_menu):
            print(old_menu, new_menu)
            total_diff += 1
        
        old_children_map = Node.get_children_map(old_menu)
        new_children_map = Node.get_children_map(new_menu)
        
        # same key
        for old_key in old_children_map:
            if old_key in new_children_map:
                total_diff += self.get_modified_items(old_children_map[old_key], new_children_map[old_key])
        
        # missing key
        for new_key in new_children_map:
            if new_key not in old_children_map:
                total_diff += self.get_modified_items(None, new_children_map[new_key])
            
        return total_diff

"""
         Existing tree
            a(1, T)
          /         \
        b(2, T)   c(3, T)
      /       \
  d(4, T) e(5, T)

                New tree
                a(1, T)
             /          \
       b(2, T)         c(3, T)
      /                   \
 d(4, T)                   e(5, T)

"""

a = Node("a", 1, True)
b = Node("b", 2, True)
c = Node("c", 3, True)
d = Node("d", 4, True)
e = Node("e", 5, True)
g = Node("g", 7, True)

a.children.append(b)
a.children.append(c)

b.children.append(d)
b.children.append(e)

# //c.children.append(g);

a1 = Node("a", 1, True)
b1 = Node("b", 2, True)
c1 = Node("c", 3, True)
d1 = Node("d", 4, True)
e1 = Node("e", 5, True)
f1 = Node("f", 6, True)
g1 = Node("g", 7, False)

a1.children.append(b1)
a1.children.append(c1)

b1.children.append(d1);
# //b1.children.append(e1);
# //b1.children.append(f1);
c1.children.append(e1)



"""
Test:
"""
Solution().get_modified_items(a, a1)
