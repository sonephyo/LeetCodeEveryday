"""
Problem 2: Pair Up Animals for Shelter
In an animal shelter, animals are paired up to share a room. Each pair has a discomfort level, which is the sum of their individual discomfort levels. The shelter's goal is to minimize the maximum discomfort level among all pairs to ensure that the rooms are as comfortable as possible.

Given a list discomfort_levels representing the discomfort levels of n animals, where n is even, pair up the animals into n / 2 pairs such that:

Each animal is in exactly one pair, and
The maximum discomfort level among the pairs is minimized. Return the minimized maximum discomfort level after optimally pairing up the animals.
Return the minimized maximum comfort level after optimally pairing up the animals.

def pair_up_animals(discomfort_levels):
  pass
Example Usage:

print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 
Example Output:

7
8
"""

def pair_up_animals(discomfort_levels):
    # sort the list
    # initiallize max
    # have two pointers at the start and at the end
    # while left < right
    #   sum and get the max
    #   increment left pointer and decrement right pointer
    
    
    discomfort_levels = sorted(discomfort_levels)
    max_discomfort_level = 0
    left_pointer, right_pointer = 0,len(discomfort_levels) - 1
    while left_pointer < right_pointer:
        max_discomfort_level = max(max_discomfort_level, discomfort_levels[left_pointer] + discomfort_levels[right_pointer])
        left_pointer += 1
        right_pointer -= 1
        
    return max_discomfort_level

print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 


"""
Problem 3: Rearrange Animals and Slogans
You are given a string s that consists of lowercase English letters representing animal names or slogans and brackets. The goal is to rearrange the animal names or slogans in each pair of matching parentheses by reversing them, starting from the innermost pair.

After processing, your result should not contain any brackets.

def rearrange_animal_names(s):
  pass
Example Usage:

print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 
Example Output:

dogcatbird
Ilovecats!
adoptapettoday!
"""
def rearrange_animal_names(s):
    # create a main stack
    stack = []
    
    # put all elements in the stack until we see ")"
    for i in s:
        temp = []
        if i == ")":
            while stack[-1] != "(":
                element = stack.pop()
                temp.append(element)
            stack.pop()
            stack.extend(temp)
        else:
            stack.append(i)
            
    return "".join(stack)

print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 
    
"""
Problem 4: Append Animals to Include Preference
You are managing an animal adoption center, and you have two lists of animals: available and preferred, both consisting of lowercase English letters representing different types of animals.

Return the minimum number of characters that need to be appended to the end of the available list so that preferred becomes a subsequence of available.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

def append_animals(available, preferred):
  pass
Example Usage:

print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))
Example Output:

2
0
4"""
def append_animals(available, preferred):
    count = 0
    for i in range(len(preferred)):
        if available[i] != preferred[i]:
            count += 1
    
    return count
        
