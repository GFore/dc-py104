# Print a triangle consisting of * characters like this:
#    *              - ROW #1
#   ***             - ROW #2
#  *****
# *******           - ROW #[height]

# Each row consists of x spaces followed by y stars where:
#  x = height of the triangle minus the row number
#  y = (ROW# times 2) minus 1

char = '*'
height = 4
row = 1
spaces = height - 1     # set the number of spaces for row1

while row <= height:
    print(spaces * " ", end='')
    print((row * 2 - 1) * char)
    row += 1
    spaces -= 1
