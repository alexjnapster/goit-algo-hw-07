# Реалізація функцій для двійкового дерева пошуку (BST) та AVL-дерева
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для знаходження найбільшого значення у двійковому дереві пошуку
def find_maximum(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

# Функція для знаходження найменшого значення у двійковому дереві пошуку
def find_minimum(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

# Функція для знаходження суми всіх значень у двійковому дереві пошуку
def find_sum(node):
    if node is None:
        return 0
    return node.val + find_sum(node.left) + find_sum(node.right)

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.right = TreeNode(35)

print("Найбільше значення у дереві:", find_maximum(root))  # Виведе 35
print("Найменше значення у дереві:", find_minimum(root))   # Виведе 5
print("Сума всіх значень у дереві:", find_sum(root))       # Виведе 115


# Реалізація структури даних для системи коментарів
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, comment):
        self.replies.append(comment)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent=0):
        print(' ' * indent + f"{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 4)


# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()

# Виведення:
# Бодя: Яка чудова книга!
#     Цей коментар було видалено.
#         Сергій: Не книжка, а перевели купу паперу ні нащо...
#     Марина: Що в ній чудового?