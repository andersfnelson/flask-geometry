#Name: Anders Nelson
#A program that outputs the volume and surface area of a sphere.
import math
def prompt():

    print("-------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF SPHERE")
    print("-------------------------------------------------")
    radius = eval(input("Please enter the radius: "))
    print("The surface area of the sphere = ", round(surface_area(radius), 2))
    print("The volume of the sphere = ", round(volume(radius), 2))
    print("--------------------------------------------------")

def surface_area(radius):
    surface_area = 4 * math.pi * radius**2
    return surface_area

def volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

if __name__ == '__main__':
    prompt()