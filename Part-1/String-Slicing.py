#Here we will learn about slicing of strings
# Case 1 slicing string from starting to end
"""
a="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean "
print(a[1:])
"""



#Case 2 How to skip the character of strings at regular interval here we are taking after 2nd interval i.e. even index character of our string b

"""
b="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. "

#Here we tell in string b [start: end : interval]
print(f"{b[0::2]}")
"""

# Case 3 Here we slicing from random to till any middle
"""
a="modo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes"
print(a[:9])
"""

#Case printing Use negative indexes to start the slice from the end of the string:


a="modo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes"
#Here we count from last to as first
print(a[-22:-12])
