# SETS

# Collection of well-defined objects

s1 = {23,2,2,2,2,2,2,2,6,5,4,2,3,5,5}
print(s1) # every element is printed only once : {2, 3, 4, 5, 6, 23}

s1.add(444444) # {2, 3, 4, 5, 6, 23, 444444}

s1.update([12,12,423,345,657,7897])  # {2, 3, 4, 5, 6, 12, 657, 23, 345, 7897, 444444, 423}

# LENGTH
print(len(s1))

# REMOVE
s1.remove(23)
# s1.remove(4567) # KeyError: 4567 because the element does not exist. Remove is strict(पता कर के आया करो ना है या नहीं )

# DISCARD
# To not get the above error, we use discard()
s1.discard(4567) # अगर है तो कर दो वरना कोई बात नहीं 
print(s1)

# POP -> Returns and removes a random element from the set, no guarantee if it is from beginning or end as opposed to the end when applied on a list
s1.pop()
s1.pop() # mostly removes from the beginning 
print(s1)

# CLEAR
s1.clear()
print(s1) # Output : set() Set has nothing

# DELETE 
# cannot use del to remove element at a particular index
del s1 # set named s1 is deleted, nothing exists
# print(s1)

# UNION & INTERSECTION

A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
  
print("Union :", A | B)
print("Intersection :", A & B)
  
# DIFFERENCE

print("Difference :", A - B)
print("Difference :", B - A)

# SYMMETRIC DIFFERENCE
print("Symmetric difference :", A ^ B)