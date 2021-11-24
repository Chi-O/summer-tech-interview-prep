# NOTE: image is n x n
def rotate_image(image):
    # transpose then reflect image
    transpose(image)
    reflect(image)

# flip on the diagonal
def transpose(image):
    n = len(image)

    for i in range(n):
        for j in range(i, n):
            image[i][j], image[j][i] = image[j][i], image[i][j]


# flip on mirror line
def reflect(image):    
    n = len(image)

    for i in range(n):
        for j in range(n // 2):
            image[i][j], image[i][- j - 1] = image[i][- j - 1], image[i][j]

image = [[1,2,3],
         [4,5,6],
         [7,8,9]]

rotate_image(image)

print(image)