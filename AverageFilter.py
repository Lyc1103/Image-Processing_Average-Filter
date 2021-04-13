import numpy as np
import cv2 as cv

img_name = input("Please enter the image you want to do by average filter : ")
img_color = cv.imread(img_name)
cv.imwrite('ColoerImage_' + img_name + '.jpg', img_color)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imwrite('GrayImage_' + img_name + '.jpg', img_gray)

img_row_size, img_col_size = img_gray.shape

mask = np.ones([3, 3], dtype=int)
mask = mask / 9

average_color = np.zeros((img_row_size, img_col_size, 3))
average_gray = np.zeros((img_row_size, img_col_size))
unsharp_color = np.zeros((img_row_size, img_col_size, 3))
unsharp_gray = np.zeros((img_row_size, img_col_size))

for i in range(1, img_row_size-1):
    for j in range(1, img_col_size-1):
        average_gray[i, j] = img_gray[i-1, j-1]*mask[0, 0] + img_gray[i-1, j]*mask[0, 1] + img_gray[i-1, j+1]*mask[0, 2] +\
            img_gray[i, j-1]*mask[1, 0] + img_gray[i, j]*mask[1, 1] + img_gray[i, j+1]*mask[1, 2] +\
            img_gray[i+1, j-1]*mask[2, 0] + img_gray[i+1, j] * \
            mask[2, 1] + img_gray[i+1, j+1]*mask[2, 2]
        unsharp_gray[i][j] = img_gray[i][j] - average_gray[i][j]/255

        average_color[i][j][0] = img_color[i-1][j-1][0]*mask[0, 0] + img_color[i-1][j][0]*mask[0, 1] + img_color[i-1][j+1][0]*mask[0, 2] +\
            img_color[i][j-1][0]*mask[1, 0] + img_color[i][j][0]*mask[1, 1] + img_color[i][j+1][0]*mask[1, 2] +\
            img_color[i+1][j-1][0]*mask[2, 0] + img_color[i+1][j][0] * \
            mask[2, 1] + img_color[i+1][j+1][0]*mask[2, 2]
        average_color[i][j][1] = img_color[i-1][j-1][1]*mask[0, 0] + img_color[i-1][j][1]*mask[0, 1] + img_color[i-1][j+1][1]*mask[0, 2] +\
            img_color[i][j-1][1]*mask[1, 0] + img_color[i][j][1]*mask[1, 1] + img_color[i][j+1][1]*mask[1, 2] +\
            img_color[i+1][j-1][1]*mask[2, 0] + img_color[i+1][j][1] * \
            mask[2, 1] + img_color[i+1][j+1][1]*mask[2, 2]
        average_color[i][j][2] = img_color[i-1][j-1][2]*mask[0, 0] + img_color[i-1][j][2]*mask[0, 1] + img_color[i-1][j+1][2]*mask[0, 2] +\
            img_color[i][j-1][2]*mask[1, 0] + img_color[i][j][2]*mask[1, 1] + img_color[i][j+1][2]*mask[1, 2] +\
            img_color[i+1][j-1][2]*mask[2, 0] + img_color[i+1][j][2] * \
            mask[2, 1] + img_color[i+1][j+1][2]*mask[2, 2]
        unsharp_color[i][j][0] = img_color[i][j][0] - \
            average_color[i][j][0]/255
        unsharp_color[i][j][1] = img_color[i][j][1] - \
            average_color[i][j][1]/255
        unsharp_color[i][j][2] = img_color[i][j][2] - \
            average_color[i][j][2]/255


average_gray = average_gray.astype(np.uint8)
cv.imwrite('GrayImageMadeByAverageFilter_' + img_name + '.jpg', average_gray)
average_color = average_color.astype(np.uint8)
cv.imwrite('ColorImageMadeByAverageFilter_' + img_name + '.jpg', average_color)

unsharp_gray = unsharp_gray.astype(np.uint8)
cv.imwrite('GrayImageMadeByAverageFilterUnsharped_' +
           img_name + '.jpg', unsharp_gray)
unsharp_color = unsharp_color.astype(np.uint8)
cv.imwrite('ColorImageMadeByAverageFilterUnsharped_' +
           img_name + '.jpg', unsharp_color)

cv.imshow("Origianl Color Image", img_color)
cv.imshow("Original Gray Image", img_gray)
cv.imshow("Gray Image Made By Average Filter", average_gray)
cv.imshow("Color Image Made By Average Filter", average_color)
cv.imshow("Color Image Made By Average Filter & Unsharped", unsharp_color)
cv.imshow("Gray Image Made By Average Filter & Unsharped", unsharp_gray)
cv.waitKey(0)
cv.destroyAllWindows()
