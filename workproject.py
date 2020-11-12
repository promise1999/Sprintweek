"""
You’ve been contracted by a local math tutoring center who is trying to introduce students to graphing
functions. The center would like for students to be able to enter the name of a particular type of
function, and then see a sample graph plotted of that variety. The program should first take in the name
of a function, for example “quadratic”, the program should prompt for any necessary coefficients, then
the program should then ask the user if they want to display the graph right away, or if they want to
save it to a file. If they choose to save it to a file, the program should prompt for a file name to save it to,
and then the program should save a picture of the graph to the specified file name. The full list of graphs
that you should implement are listed below:
Graph Name Formula
linear f(x) = a*x+b
quadratic f(x) = a*x^2 + b*x + c
cubic f(x) = a*x^3 + b*x^2 + c*x + d
quartic f(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e
exponential f(x) = a*b^(c*x + d)
logarithmic f(x) = a*log(b*x + c)
sine f(x) = a*sin(b*x + c)
cos f(x) = a*cos(b*x + c)
square root f(x) = a*sqrt(b*x + c)
cube root f(x) = a*(b*x + c)^(1/3)
Note that in each case, you should take in parameters to fill in the formula’s coefficients. For
example, if the user types “linear” you should prompt for values of a and b. For quadratic, prompt for
a, b, and c. For cubic prompt for a, b, c, and d. For quartic, prompt for values of a, b, c, d, and e. For
exponential, prompt for values of a, b, c, and d. For log, sin, cos, square root, and cube root, prompt
for a, b, and c.
In all cases, you should prompt for the range to plot the graph between. For example, let’s say I
wanted to plot the graph f(x) = x from -10 to 10. To do this, I’d use the program like so:
"""
import numpy as npy
import matplotlib.pyplot as plt
import math


graph_style = (["linear"], ["quadratic"],["cubic"], ["quartic"],["exponential"],["log,sin,cos,square root, cube root"] )  


x_values = []
y_values = []
user_num=[]
alpha = ["A","B","C","D","E"]
x=0
# create an infinite loop for all graph input required
while True:
    graph_required = input("Please select a graph requried: ")

    if graph_required.upper() == "LINEAR":
        print("Linear graphs are in the form: f(x) = a*x+b \n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        start_range = float(input("please enter a start range:  "))
        end_range= float(input("please enter an end range:  "))
        
        x=start_range
        while x < end_range:
            y = value_a * x + value_b
            
            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("linear.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
    # collecting input values for selected graph
    elif graph_required.upper() == "QUADRATIC":
        print("Quadratic Graphs are in the form: f(x) = a*x^2 + b*x + c \n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        start_range = float(input("please select a range for start_range: "))
        end_range = float(input("please select a range for end range: "))
        
        #calculating quadratic equation and plotting it graph 
        x=start_range
        while x < end_range:
        
            y = value_a*x**2 + value_b*x + value_c
            
            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("quad.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
    # collecting values, calculating and plotting cubic graph     
    elif graph_required.upper() == "CUBIC":
        print(" cubic f(x) = a*x^3 + b*x^2 + c*x + d \n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        value_d = float(input("please provide a value D: "))
        start_range = float(input("please select a start range for graph: "))
        end_range = float(input("please select a end range for graph: "))
        
        x=start_range
        while x < end_range:
            y = value_a *x**3 + value_b *x**2 + value_c*x + value_d
            
            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("cub.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d" or display.lower() != "s":
            print("Here is your graph display ")
        else:
            print("create a file name ")
        
        file_name = input("would you like to call your file cub.png? Y or N ")
        if file_name.lower() != "y":
            print("this file is not saved")
        
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
    # collecting input values, calculating quartic equation and plotting it graph     
    elif graph_required.upper() == "QUARTIC":
        print("quartic f(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e \n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        value_d = float(input("please provide a value D: "))
        value_e = float(input("please provide a value E: "))
        start_range = float(input("please select a range for graph: "))
        end_range = float(input("please select a range for graph: "))
        
        x=start_range
        while x < end_range:
            y = value_a *x** 4 + value_b *x**3 + value_c *x**2 + value_d*x + value_e 
            
            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("quartic.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d":
            print("Here is your graph display ")
        else:
            print("this file is not save")
        
        file_name = input("would you like to call your file quartic.png? Y or N ")
        if file_name.lower() != "y":
            print("create a file name ")
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
        
    # collecting input values, calculating for exponential and plotting it graph                
    elif graph_required.upper() == "EXPONENTIAL":
        print("exponential f(x) = a*b^(c*x + d) \n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        value_d = float(input("please provide a value D: "))
        start_range = float(input("please select a range for start_range for graph: "))
        #if start_range > -10:
            #print("start_range must be less than -10. Try again! ")
        #else:
            #break
        end_range = float(input("please select an end range for graph: "))
        #if end_range >= 10:
            #print("end_range must be 10 or less. ")
        #else:
            #break
        
        x=start_range
        while x < end_range:
            y = value_a * value_b **(value_c * x + value_d)
            
            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("expo.png")
        
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d" or display.lower() != "s":
            print("Here is your graph display ")
        else:
            print("create a file name ")
        
        file_name = input("would you like to call your file expo.png? Y or N ")
        if file_name.lower() != "y":
            print("this file is not saved")
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
    # collecting input values, calculating for log and plotting it graph     
    elif graph_required.upper() == "LOG":
        print("sine f(x) = a*log(b*x + c)\n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        
        while True:
            try:
                start_range = float(input("please select a start_range for graph: "))
                y = math.log(start_range)
            except:
                print("No negative values please")
            else:
                break
            
        while True:
            try:
                end_range = float(input("please select a end_range for graph: "))
                y = math.log(end_range)
            except:
                print("No negative values please")
            else:
                break
        
        x=start_range
        while x < end_range:
            
            y = value_a*math.log(value_b *x + value_c)

            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("log.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d" or display.lower() != "s":
            print("Here is your graph display ")
        else:
            print("create a file name ")
        
        file_name = input("would you like to call your file log.png? Y or N ")
        if file_name.lower() != "y":
            print("this file is not saved")
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
    # collecting input values, calculating for sin and plotting it graph      
    elif graph_required.upper() == "SIN":
        print("sine f(x) = a*sin(b*x + c)\n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        start_range = int(input("please select a start_range for graph: "))
        end_range = int(input("please select a end_range for graph: "))
        
        x=start_range
        while x < end_range:
            y = value_a*math.sin(value_b *x + value_c)

            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("sine.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d" or display.lower() != "s":
            print("Here is your graph display ")
        else:
            print("create a file name ")
        
        file_name = input("would you like to call your file sine.png? Y or N ")
        if file_name.lower() != "y":
            print("this file is not saved")
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
    # collecting input values, calculating for cos and plotting it graph    
    elif graph_required.upper() == "COS":
        print("cos f(x) = a*cos(b*x + c)\n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        start_range = int(input("please select a start_range for graph: "))
        end_range = int(input("please select a end_range for graph: "))
        
        x=start_range
        while x < end_range:
            y = value_a*math.cos(value_b *x + value_c)

            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("cos.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d" or display.lower() != "s":
            print("Here is your graph display ")
        else:
            print("create a file name ")
        
        file_name = input("would you like to call your file cos.png? Y or N ")
        if file_name.lower() != "y":
            print("this file is not saved")
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
    
    # calculating for square root and plotting it graph     
    elif graph_required.upper() == "SQUARE ROOT":
        print("square root f(x) = a*sqrt(b*x + c)\n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        start_range = int(input("please select a start_range for graph: "))
        end_range = int(input("please select a end_range for graph: "))
        
        x=start_range
        while x < end_range:
            y = value_a*math.sqrt(value_b *x + value_c)

            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("sqrt.png")
        
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d" or display.lower() != "s":
            print("Here is your graph display ")
        else:
            print("create a file name ")
        
        file_name = input("would you like to call your file sqrt.png? Y or N ")
        if file_name.lower() != "y":
            print("this file is not saved")
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break
        
    # calculating for cube root and plotting graph    
    elif graph_required.upper() == "CUBE ROOT":
        print("cube root f(x) = a*(b*x + c)^(1/3) \n")
        value_a = float(input("please provide a value A: " ))
        value_b = float(input("please provide value B: " ))
        value_c = float(input("please provide a value C: "))
        start_range = int(input("please select a start_range for graph: "))
        end_range = int(input("please select a end_range for graph: "))
        
        x=start_range
        while x < end_range:
            y = value_a*(value_b *x + value_c)**(1/3)
            
            x_values.append(x)
            y_values.append(y)
            
            x+=1
            
        plt.plot(x_values,y_values)
        plt.show()
        plt.savefig("cuberoot.png")
    
        display = input("Would you like to diaplay your graph or save, D OR S ")
        if display.lower() == "d" or display.lower() != "s":
            print("Here is your graph display ")
        else:
            print("create a file name ")
        
        file_name = input("would you like to call your file cuberoot.png? Y or N ")
        if file_name.lower() != "y":
            print("this file is not saved")
        cont = input("Do you wish to continue Y or N ")
        if cont.lower() != "y":
            break