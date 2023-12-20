# Define a function to merge two lists and sort the combined list.
def mergeList(first, second):
    # Combine the two lists.
    combined = first + second
    # Sort the combined list.
    combined.sort()
    # Return the sorted combined list.
    return combined


# Create a list named 'group1' with some integers.
group1 = [11, 13, 18, 17, 56]
# Create another list named 'group2' with some integers.
group2 = [12, 15, 19, 43, 66]
# Call the 'mergeList' function with 'group1' and 'group2' as arguments and store the result in 'merged'.
merged = mergeList(group1, group2)
# Print the merged and sorted list.
print(merged)
