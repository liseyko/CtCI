# Given an image represented by an MxN matrix, where each pixel in the image is 4 bytesm write a method to rotate the image by 90 degrees. [in place?]

def init_matrix(m,n):
    if min(m,n)<1:
        return False
    img = []
    for i in range(n):
        img.append([])
        for j in range(m):
            img[i].append(str(i)+str(j))
    return img

def print_img(img):
    if img:
        for n in range(len(img)):
            for m in range(len(img[n])):
                print(img[n][m], end = ' ')
            print()
    print()

def rotate_naive(img):
    """returns copy of a matrix"""
    new_img = []
    m = 0
    if img:
        m = len(img)
        if m>0:
            n = len(img[0])
    if n == 0:
        return

    for i in range(n):
        new_img.append([])
        for j in range(m-1,-1,-1):
            new_img[i].append(img[j][i])
    return new_img


def rotate(img): # inplace
    """rotates matrix in place"""
    n = len(img)
    m = len(img[0])

    def rotate_right(size):
        x,y = 0,0
        for step in range(size-1,0,-2):
            for i in range(step):
                tmp = img[x][y+i]
                img[x][y+i] = img[x+step-i][y]
                img[x+step-i][y] = img[x+step][y+step-i]
                img[x+step][y+step-i] = img[x+i][y+step]
                img[x+i][y+step] = tmp
            x+=1; y+=1

    rotate_right(min(n,m))

    if m > n: # case 1
        for j in range(n,m):
            img.append([])
        for j in range(m-1,n-1,-1):
            for i in range(n-1,-1,-1):
                img[j].append(img[i].pop(j))

    elif n > m: # case 2
        for i in range(m,n):
            for j in range(m-1,-1,-1):
                img[j].insert(0,img[m].pop(j))
            del img[m]

    return img
