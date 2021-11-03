def rotate_image(image):
    res = [[0 for i in range(len(image))] for j in range(len(image))]
    
    for i in range(len(image)):
        for j in range(len(image) - 1, -1, -1):
            res[j][i] = image[i][j]
            
    print(res)

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rotate_image(a)