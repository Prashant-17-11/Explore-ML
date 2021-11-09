# This is the second project in CodeCademy Data Science Learning Path
# We will optimize the previous project using the knowledge of functions

# code given as starting format

# Task 1
# Observe the code to see how insurance costs for two individuals Maria and Omar is calculated

# Task 2
# observe that the code for estimating the insurance costs for both the candidates is similar and being repeated
# create a function calculate_insurance_cost()

# Task 3
# create a variable called estimated_cost and set it to 1000
# add print statement that prints estimated_cost
# return estimated_cost

# Task 4
# adding parameters to function
# parameters: age, sex, bmi, num_of_children, smoker

# Task 5
# replace the 1000 in estimated_cost to the formula for insurance cost

# Task 6
# go to section of code that estimates Maria's insurance cost
# rename insurance_cost as maria_insurance_cost and set it equal to calculate_insurance_cost() with appropriate values for Maria

# Task 7
# remove the print statement for Maira
# remove the initial variables for Maria

# Task 8
# repeat steps 6-7 for Omar

# Task 9
# add another parameter name to function definition

# Task 10
# modify the print statement to include name

# Task 11
# Update the function calls to add name

# Task 12
# to see the reusability calculate insurance cost for yourself using the function

# Task 13
# here we learned the reusability of functions and how a clean and modular code is more better than repetitive code
# Happy Coding!


# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker,name):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for "+name+" is "+str(estimated_cost)+" dollars.")
    return estimated_cost

# Initial variables for Maria 

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28,0,26.2,3,0,"Maria")

# Initial variables for Omar

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35,1,22.2,0,1,"Omar")

my_insurance_cost = calculate_insurance_cost(20,1,24.3,0,0,"Prashant")