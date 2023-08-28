def postOrder(root, list):
    if root==None:
            return 
    postOrder(root.left,list)
    postOrder(root.right, list)
    list.append(root.val)
    return list
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        res = []
        res = postOrder(root, res)
        return res
