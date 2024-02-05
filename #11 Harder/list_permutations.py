
def get_permutation(lst):
    # For an empty list, there is no permutation
    if len(lst) == 0:
        return []
    # A list with one element will have only one permutation
    if len(lst) == 1:
        return [lst]
    # Create an empty list to store permutations
    perms = []
    for i in range(len(lst)):
        # Extract the current element from the list
        current = lst[i]
        # Recursively call get_permutation for the remaining list
        rem_list = lst[:i] + lst[i+1:]
        rem_perm = get_permutation(rem_list)
        # Generate permutations by adding the current element to each permutation of the remaining list
        for p in rem_perm:
            perms.append([current] + p)
    return perms

# Test the function with a list of data
data = [1, 2, 3]
for perm in get_permutation(data):
    print(perm)
