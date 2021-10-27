# Name: Anders Nelson
# # A Python program to find the volume and surface area of a cylinder.
import math

def prompt():
    print("------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CYLINDER")
    print("------------------------------------------------------")
    radius = eval(input("Please enter the radius: "))
    height = eval(input("Please enter the height: "))
    print()
    print("The surface area of a Cylinder = ", round(surface_area(radius, height), 2))
    print("The volume of a Cylinder = ", round(volume(radius, height), 2))
    print("Lateral surface area of a Cylinder = ", round(lateral_surface_area(radius, height), 2))
    print("Top OR bottom surface area of a Cylinder = ", round(top_bottom_surface_area(radius), 2))
    print("-------------------------------------------------------")

def surface_area(radius, height):
    surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
    return surface_area

def volume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume

def lateral_surface_area(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height
    return lateral_surface_area

def top_bottom_surface_area(radius):
    top_bottom_surface_area = math.pi * (radius**2)
    return top_bottom_surface_area

if __name__ == '__main__':
    prompt()