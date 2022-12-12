
def get_shape():
    shapes = ""
    valid_shapes = ["pyramid", "square", "triangle","rhombus","inverted_triangle","rectangle"]
    while shapes not in valid_shapes:
        shapes = input("Shape?: ").lower()
    return shapes
    

def get_height():
    shape_height = False  
    while not shape_height < 80 or shape_height < 1:
        shape_height = input ("Height?: ")
        if shape_height.isnumeric() :
            shape_height = int(shape_height)
        else :             
            shape_height = False
    return shape_height 



def draw_pyramid(height, outline):
    if outline == False:
        for i in range(1,height+1):
            print(" "*(height-1)+ "*" *(2*i-1))
            height-= 1


    if outline == True:
        for i in range(1,height+1):
            for j in range(1,height+i):
                if i+j==height+1 or j-i==height-1 or i==height:
                    print('*' ,end='')
                else:
                    print(end=' ')
            print()
                

def draw_square(height, outline):  
    if outline == False :  
        for i in range (height):
            for j in range(height):
                print("*",end= "")
            print()  
    elif outline == True:
            for i in range(0, height):
                for j in range(0,height):
                    if  i== 0 or i == height-1 or j== 0 or j== height-1:
                         print("*",end="")
                    else:
                        print(" ",end="")
                print() 


def draw_triangle(height, outline):
    if outline == False:
        for i in range(1,height+1):
            print(""*(height-i)+"*"*i)
    
    elif outline == True:
        for i in range(1,height+1):
            for j in range(1,i+1):
                if i == 1 or i == height or j == 1 or j == i:
                 print("*",end="")
                else:
                    print(" ",end="")
            print()    

def draw_rhombus(height, outline):
    if outline == False :
        for i in range(height):
            for j in range(i):
                print("*",end="")
            for k in range(height):
                 print("*", end='')
            print()
    
    if outline == True:
        for i in range(height):
            for j in range(i):
                print(" ", end="")
            for k in range(height):
                print("*",end='')
            print()
    

def draw_inverted_triangle(height, outline):
    if outline == False:
        for c in range(height):
            print(" "*c+"*"*(height-c))
        print()
    if outline == True:
        for row in range(height):
            for col in range(height):
                if row==0 or col==(height-1) or row==col:
                    print("*", end='')
                else:
                        print(end=" ")
            print()

def draw_rectangle(height, outline):
    if outline == False:
        for a in range(0, height):
            for b in range(height*4):
                print('*',end="")
            print()

    if outline == True:

        for i in range(1,height+1):
            for j in range(1,(height)**2):
                if i == 1 or i ==height or j == 1 or j==(height**2)-1:
                    print("*",end="")
                else:
                    print(end=" ")
            print()

def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'rhombus':
        draw_rhombus(height, outline)
    elif shape == 'inverted_triangle':
        draw_inverted_triangle(height, outline)
    elif shape == 'rectangle' :
        draw_rectangle(height, outline)   
    


def get_outline():
    selected_type= input("Outline only? (y/n): ")
    if selected_type == "y":
        return True
    elif selected_type == "n" or selected_type == " ":
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

