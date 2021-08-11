'''this program is designed to create pascal's triangle and print it out'''
#importing necessary functions
from algebra import createEmptyTriangle
from algebra import printTriangle
from algebra import generateTriangle

#creating the triangles
triangleSize = 10
print("creating empty triangle")
printTriangle(createEmptyTriangle(triangleSize))
print("Printing the", triangleSize, "rows Pascal's triangle")
printTriangle(generateTriangle(triangleSize,createEmptyTriangle(triangleSize)))