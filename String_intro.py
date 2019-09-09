#Let's Print String

# #With Single Quotes
# my_string = 'this is my first string'

# print(my_string)

# #With Double Quotes

# my_string = "this is my first string"
# print(my_string) #It's Same As Single Quotes


# #With Multiple Quotes

# my_string = """this is' my first string"""
# print(my_string) 

#Print in Next Line (\n) NewLine Character
#in Plain Langauge, it Means That We Are inserting A Break and A New Row, a New Line in Our Text.

#Inserting The backslashes  is called the escaping the new line character.

# my_string = '''this
# is
# my
# first
# string'''

# print(my_string) # For Print The Value in Next Line
# #Another Example of (\n)

# my_string = '''this\
# is\
# my\
# first\
# string'''

# print(my_string) 
# #Output (thisismystring)

#Indexing 

#Python Uses Index to Mark the Position of an element Within a Sequence of Elements.
#When Using The Indexes,Remembers to Always Start With 0.
#And From Right to left the First Index will be -1.

string1 = "cisco router"

# print(string1[0]) #Output = c #Python Start With Zero
# print(string1[4]) #Output = o
# print(string1[5]) #Spaces Count Characters Too


#For Negative Indexes

# print(string1[-1]) #Output  = r

# print(string1[-3]) #output = t

# print(string1[-8]) #output = o


#Length() Function
print(len(string1)) #Looks Like String1 Have 12 Character

#What if we Enter The Invaid  Character in Index?
print(len(string1[20])) #Output = String Index Out of Range.
