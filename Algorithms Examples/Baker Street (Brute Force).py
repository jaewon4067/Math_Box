"""

Suppose there is a heavy rain around Baker street Station. It's raining a lot, which is like a disaster movie, so high-rise buildings are submerged in water.
When that happens, I'd like to know how much rainwater can be contained between the building. I want to write a function 'trapping_rain' that calculates it.
The function trapping_rain receives the building list that holds the building height information as a parameter, and returns the total amount of rainwater.
For example, [3, 0, 0, 2, 0, 4] comes in as the building parameters, this means that there are buildings 3 high in index 0, 2 high in index 3, and 4 high in index 5. 
There are no buildings in indexes 1, 2, and 4.
Then, a total of 10 rainwater can be contained. Therefore, the trapping_rain function returns 10.

Let's say [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] is in the building parameters this time. 
Then, a total of 6 amount of rainwater can be contained. So the trapping_rain function returns 6.

"""

# According to the method below, you can calculate the amount of rainwater in each index.

# Find the height of the tallest building on the left side of the current index.
# Find the height of the tallest building on the right side of the current index.
# Find the height of the lower building.
# Subtract the height of the building currently in the index from that height.

def trapping_rain(buildings):
    # total rainwater 
    total_height = 0

    # In each index, find the amount of rainwater.
    # no need to calculate 0th index and the last index.
    for i in range(1, len(buildings) - 1):
        # Find the tallest building on both sides of the current index.
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # The height of the rainwater of the current index.
        upper_bound = min(max_left, max_right)

        # Calculate the rainwater in the current index.
        # If upper_bound is not bigger than the height of the current building, the rainwater of current index is 0.
        total_height += max(0, upper_bound - buildings[i])

    return total_height

# Test
print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

"""

Let's say the length of the input building n.
First of all, the For Loop is proportional to n, which is O(n). 
And the longest part of the loop is the max (buildings [:i]) or max (buildings [i:]). Let's check one of them.
The worst case of buildings[:i] is O(n). The maximum value using a max function for the sliced list is also O(n). It's 2O(n), so it's O(n).
Therefore, the time complexity of the trapping_rain function is O(n^2).

There is a more efficient way to solve this question in terms of time copmlexity. 

"""

# We found the height of the tallest building on the left side and right side of the current index
# These two steps took O(n) each. Can this part be more efficient?


def trapping_rain(buildings):
    # total rainwater
    total_height = 0 
    n = len(buildings)

    # Create lists for the max value of left and right hand side. 
    left_list = [0] * n
    right_list = [0] * n

    # Each index in the list, save the max value of the left hand side.
    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i - 1], buildings[i])
                
    # Each index in the list, save the max value of the right hand side.
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i])

    # From the saved values, calculate the total rainwater.
    for i in range(n):
        # The height of the rainwater of the current index.
        upper_bound = min(right_list[i], left_list[i])
        
        # Calculate the rainwater in the current index.
        # If upper_bound is not bigger than the height of the current building, the rainwater of current index is 0.
        total_height += max(0, upper_bound - buildings[i])

    return total_height

#test
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

"""

Let's say the length of the input buildings n.
The number of For Loops is proportional to n. The time complexity of the trapping_rain function is 3 * O(n), which is O(n). 
Since we used two lists proportional to n, the space complexity becomes 2 * O(n),which is O(n).

By using two more lists, the the space complexity became O(n), whereas, the time complexity became O(n) from O(n^2). 
"""
