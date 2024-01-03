V, E = map(int, input().split())
edges = list(map(int, input().split()))

left = [0] * (V + 1)
right = [0] * (V + 1)
ancestors = [0] * (V + 1)

for i in range(E):
    parent, child = edges[i * 2 : i * 2 + 2]
    if not left[parent]:
        left[parent] = child
    else:
        right[parent] = child
    ancestors[child] = parent

root = None
for j in range(1, V+1):
    if ancestors[j] == 0:
        root = j
        break

def preorder(node):
    if node < 1:
        return
    
    print(node, end=' ')
    preorder(left[node])
    preorder(right[node])

def inorder(node):
    if node < 1:
        return
    
    inorder(left[node])
    print(node, end=' ')
    inorder(right[node])

def postorder(node):
    if node < 1:
        return
    
    postorder(left[node])
    postorder(right[node])
    print(node, end=' ')

preorder(root)
print()
inorder(root)
print()
postorder(root)


