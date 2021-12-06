
class Node:
    def __init__(self, value, child) -> None:
        self.value = value
        self.child = child


def list_to_linked_list(values):
    if not len(values): 
        return None
    else:
        return Node(values[0], list_to_linked_list(values[1:]))

def print_linked_list(linked_list, depth = 0):
    if not linked_list: return None
    print((' '*depth) + '↳' + str(linked_list.value))
    print_linked_list(linked_list.child, depth + 1)

# TODO
def reverse_linked_list(linked_list):
    pass



def test():
    ll = list_to_linked_list([3, 6, 3, 6, 8])
    print_linked_list(ll)

test()
