import math

def main():
    width,ratio,diameter=0,0,0
    
    #width
    check_val=True
    while(check_val):
        width=int(input("Enter the width of the tire in mm: "))
        check_val=check(width)
    
    #ratio
    check_val=True
    while(check_val):
        ratio=float(input("Enter the aspect ratio of the tire: "))
        check_val=check(ratio)
    
    #diameter
    check_val=True
    while(check_val):
        diameter=float(input("Enter the diameter of the wheel in inches: "))
        check_val=check(diameter)

    #volume calculating function
    vol=volume(width,ratio,diameter)
    print("volume of the tire: ", vol)


def volume(width,ratio,diameter):
    output=((math.pi)*(math.pow(width,2))*ratio*((width*ratio)+2540*diameter))
    val=output/10000000000
    return val

def check(data):
    if data>0:
        return False
    else:
        print("Negative values are not accepted- re-enter ")
        return True

if __name__ == "__main__":
    main()