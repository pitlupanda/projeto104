import cv2
img = cv2.imread('solar-system.jpg')
cv2.putText(img,"sol", (100, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.putText(img,"mercurio", (60, 250), cv2.FONT_HERSHEY_PLAIN, 2, (26, 232, 81))
cv2.putText(img,"venus", (180, 180), cv2.FONT_HERSHEY_PLAIN, 2, (242, 12, 200))
cv2.putText(img,"terra", (220, 300), cv2.FONT_HERSHEY_TRIPLEX, 2, (215, 232, 28))
cv2.putText(img,"marte", (320, 170), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (10, 242, 250))
cv2.putText(img,"jupiter", (500, 40), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (247, 184, 74))
cv2.putText(img,"saturno", (700, 350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (83, 33, 219))
cv2.putText(img,"urano", (950, 290), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (41, 240, 193))
cv2.putText(img,"netuno", (1070, 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (33, 219, 49))
cv2.imshow('resultado',img)
cv2.waitKey(0)
cv2.imwrite('Solar_systemwithname.jpg',img)
