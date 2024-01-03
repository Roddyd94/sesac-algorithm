N = int(input())


def alpha_to_int(ch: str) -> int:
    return ord(ch) - ord("A")


def int_to_alpha(n: int) -> str:
    return chr(n + ord("A"))


ati = alpha_to_int
ita = int_to_alpha

ancestor = [-1] * N
left = [-1] * N
right = [-1] * N

for _ in range(N):
    parent, l, r = map(ati, input().split())

    if l >= 0:
        ancestor[l] = parent
        left[parent] = l
    if r >= 0:
        ancestor[r] = parent
        right[parent] = r


def preorder(node):
    print(ita(node), end="")
    if left[node] != -1:
        preorder(left[node])
    if right[node] != -1:
        preorder(right[node])


def inorder(node):
    if left[node] != -1:
        inorder(left[node])
    print(ita(node), end="")
    if right[node] != -1:
        inorder(right[node])


def postorder(node):
    if left[node] != -1:
        postorder(left[node])
    if right[node] != -1:
        postorder(right[node])
    print(ita(node), end="")


preorder(0)
print()
inorder(0)
print()
postorder(0)
