import cv2

image = cv2.imread('bird.jpg')

# Task 4
r, g, b = cv2.split(image)

cv2.imshow('Red Channel', r)
cv2.imshow('Green channel', g)
cv2.imshow('Blue Channel', b)

# Task 6
g.fill(0)

# Task 7
blue_red_image = cv2.merge((r, g, b))
cv2.imshow('Image without green', blue_red_image)

cv2.waitKey(0)
# cv2.destroyAllWindows()
