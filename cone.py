# Name: Anders Nelson
# # A Python program to find the volume and surface area of a cone.
import math

def volume(radius, height):
    volume = math.pi * (radius**2) * (height/3)
    return volume

def slant(radius, height):
    slant = math.sqrt(height**2 + radius**2)
    return slant

def surface_area(radius, height):
    surface_area = math.pi * radius * (radius + (math.sqrt(height**2 + radius**2)))
    return surface_area

def lateral_surface_area(radius, height):
    lateral_surface_area = radius * math.pi * (math.sqrt(height**2 + radius**2))
    return lateral_surface_area

def prompt():
    print("------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CONE")
    print("------------------------------------------------------")
    radius = eval(input("Please enter the radius: "))
    height = eval(input("Please enter the height: "))
    # vol = volume(radius, height)
    print("The volume of a Cone = ", round(volume(radius, height), 2))
    print("Length of a Side (Slant) of a Cone = ", round(slant(radius, height), 2))
    print("The surface area of a Cone = ", round(surface_area(radius, height), 2))
    print("Lateral surface area of a Cone = ", round(lateral_surface_area(radius, height), 2))
    print("-------------------------------------------------------")

if __name__ == '__main__':
    prompt()