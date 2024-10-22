
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

# Example usage:
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  # Output should be [5, 4, 3, 2, 1]
