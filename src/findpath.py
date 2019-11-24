def binaryTreePaths(root):
    # write your code here
    result = []
    path=""
    if root!=None:
        findpath(root,path,result)
    return list;

def findpath(root,path,result):
    if root==None:
        return;
    if root.left==None and root.right==None:
        result.append(path)
        return;
    if root.left!=None:
        path=path+"->"+root.left.val
        findpath(root.left,path,result)
        path=path[0:-3]
    if root.right!=None:
        path=path+"->"+root.right.val
        findpath(root.left,path,result)
        path=path[0:-3]

print(binaryTreePaths({1,2,3,'#',5}))