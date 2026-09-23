"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        current = head
        copyList = Node(current.val)
        currentCopyList = copyList
        listDict = { head: copyList }

        while current:
            nxt = current.next
            random = current.random

            if nxt:
                if not listDict.get(nxt):
                    currentCopyList.next = Node(nxt.val)
                    listDict[nxt] = currentCopyList.next
                else:
                    currentCopyList.next = listDict[nxt]
            if random:
                if not listDict.get(random):
                    currentCopyList.random = Node(random.val)
                    listDict[random] = currentCopyList.random
                else:
                    currentCopyList.random = listDict[random]

            current = nxt
            currentCopyList = currentCopyList.next
        
        return copyList
