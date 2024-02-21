import math

p1 = [4, 0]
p2 = [6, 6]

# Calculate the distance between the two points using the distance formula.
# The formula computes the Euclidean distance in a 2D space.
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

# Print the calculated distance.
print(distance)