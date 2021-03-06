# SENG3110 Software Testing
# 
# Project: Geometry Calculator Web App
#
# Sample Code for the Python Flask Web App Implementation of the Geometry Calculator
#
# Author: Joe Axberg
# Orig Date: 9/22/2021
# cylinder, sphere, cube, cone
# imports
from flask import Flask, request, render_template, redirect, url_for
import cylinder #<--why?
import cone
import sphere
#flask plumbing
app = Flask(__name__)

#flask route for the index page
#uses html template for user selection
@app.route("/", methods = ["GET", "POST"])
def mainForm():
   if request.method == "POST":
      try:
         selection = request.form['select']
         # print("Selection was: ", sphere, cylinder) #prints to command line for trouble shooting
         if selection == "cone":
            print("User selected cone") #prints to command line for trouble shooting
            return redirect(url_for('coneForm'))
         elif selection == "cylinder":
            print("User selected cylinder") #prints to command line for trouble shooting
            return redirect(url_for('cylinderForm'))
         elif selection == "sphere":
            print("User selected sphere") #prints to command line for trouble shooting
            return redirect(url_for('sphereForm'))
         else:
            pass
      except:
         pass
   return render_template("index.html")

#flask route for the cylinder calculations page
@app.route("/cylinder", methods = ["GET", "POST"])
def cylinderForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       height = request.form.get("hgt") 
       vol = cylinder.volume(int(radius), int(height))
       sa = cylinder.surface_area(int(radius), int(height))
       lsa = cylinder.lateral_surface_area(int(radius), int(height))
       tbsa = cylinder.top_bottom_surface_area(int(radius))
       return render_template("cylinder.html", vol=vol, sa=sa, lsa=lsa, tbsa=tbsa, radius=radius, height=height)
   return render_template("cylinder.html")

#more code here for the rest of the calculators: sphere, cube, etc.

@app.route("/cone", methods = ["GET", "POST"])
def coneForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       height = request.form.get("hgt") 
       vol = cone.volume(int(radius), int(height))
       slant = cone.slant(int(radius), int(height))
       sa = cone.surface_area(int(radius), int(height))
       lsa = cone.lateral_surface_area(int(radius), int(height))
      #  return "User entered: Radius "+ str(radius) + " and Height: " + str(height) + ". <p>The Volume is: " + str(vol)
       return render_template("cone.html", vol=vol, sa=sa, lsa=lsa, slant=slant, radius=radius, height=height)
   return render_template("cone.html")

@app.route("/sphere", methods = ["GET", "POST"])
def sphereForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       vol = sphere.volume(int(radius))
       sa = sphere.surface_area(int(radius))
      #  return "User entered: Radius "+ str(radius) + " and Height: " + str(height) + ". <p>The Volume is: " + str(vol)
       return render_template("sphere.html", vol=vol, sa=sa, radius=radius)
   return render_template("sphere.html")
  
if __name__=='__main__':   #more flask plumbing so the environment starts correctly
   app.run(host='0.0.0.0', debug=True)
