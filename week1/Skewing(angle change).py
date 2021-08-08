from math import *
from cs1media import *
img = load_picture(r"C:\Users\c_zho\Desktop\Kaist_Python\Kaist-Map\gurumi.png" )
w,h = img.size()
        
        
        
def skew(img, direction, angle):
    if not (direction == "vertical") and not (direction == "horizontal") :
        return print("Wrong input!!")
    if not (-89<= angle <=89) :
        return print("Wrong input!!!")
        
    #vertical
    if direction == "vertical":
        new_w = int(w + h * tan(radians(abs(angle))))
        new_h = h
        new_img =  create_picture(new_w, h)
        if angle >=0 :
            for y in range(h):
                for x in range(w):
                    new_img.set(x + int((new_h-y)*tan(radians(angle))), y, img.get(x,y))

        elif angle < 0 :
            for y in range(h):
                for x in range(w):
                    new_img.set(x + int(y*tan(radians(-angle))), y, img.get(x,y))
    #horizontal
    elif direction == "horizontal":
        new_w = w
        new_h = int(h + w * tan(radians(abs(angle)))) # <--- 이 부분 수정
        new_img =  create_picture(w , new_h)
        if angle>=0 :
            for y in range(h):
                for x in range(w):
                        new_img.set(x, y+int((new_w-x)*tan(radians(angle))), img.get(x,y))

        elif angle < 0 :
            for y in range(h):
                for x in range(w):
                    new_img.set(x , y+int(x*tan(radians(-angle))), img.get(x,y))


    new_img.show()

direction = input("direction : ")
angle = int(input("angle : "))

skew(img , direction , angle)