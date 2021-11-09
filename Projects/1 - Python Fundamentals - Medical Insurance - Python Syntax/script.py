# This is the first progject in Codecademy Data Science Learning Path
# All the instructions given have been documented for easy comprehension

# Suppose you are a medical professional curious about how certain factors contribute to medical insurance costs. Using a formula that estimates a person's yearly insurance costs, you will investigate how different factors such as age, sex, BMI, etc. affect the prediction

# Task 1
# Setting up Factors
# Our first step is to create the variables for each factor we will consider when estimating medical insurance costs.
# create the following varibales for a 28 - year - old, nonsmoking woman who has three children and a BMI of 26.2

# age - age of the individual in years
age = 28
# sex - 0 for female, 1 for male
sex = 0
# bmi - individual's body mass index
bmi = 26.2
# num_of_children - number of children the individual has
num_of_children = 3
# smoker - 0 for a non-smoker, 1 for a smoker
smoker = 0

# Task 2
# Working with the Formula
# After the declaration of the variables, create a variable called insurance_cost that utilizes the following formula:
# insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Task 3
# Let's print out this value in an informative way.
print("This person's insurance cost is "+str(insurance_cost)+" dollars.")

# Task 4
# Looking at Age Factor
# We have seen how our formula can estimate costs for one individual. Now let's play with some individual factors to see what role each one plays in our estimation!
# Let's start with the age factor. Using a plus-equal operator add 4 years to our age variable.

age += 4

# Task 5
# Now that we have changed our age value, we want ot recalculate our insurance cost. Declare a new variable called new_insurance_cost underneath the expression that increased age by 4
# Make sure to leave the line with the insurance_cost variable the same. We will use it later in our program!
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Task 6
# Next we want to find the difference betweenour new_insurance_cost and insurance_cost. To do this, let's create a new variable called change_in_insurance_cost and set it equal to the difference between new_insurance_cost and insurance_cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# "People who are four years older have estimated insurance costs that are "+change_in_insurance_cost+" dollars differnet, where the sign of "+change_in_insurance_cost+" tells us whether the cost is higher or lower.");

# Task 7
# we want to display the information in an informative way similar to the output from instruction 3. On the next line, print the follwoing string:
# The change in cost of insurance after increasing the age by 4 years is change_in_insurance_cost dollars.
print("The change in cost of insurance after increasing the age by 4 years is "+str(change_in_insurance_cost)+" dollars.")

# Task 8
# Looking at BMI factor
# Now that you have looked at the age factor, let's move onto another one: BMI. First we have to redefine our age variable to be its original value.
# Set age to 28 following your last piece of code. This will reset its value and allows us to focus on just the change in the BMI factor moving forward.
age = 28
# On the next line, using the plus-equal operator, add 3.1 to our bmi variable
bmi += 3.1

# Task 9
# Now lets find out how a change in BMI affects insurance costs. Our next steps are pretty much the same as we have done before when looking at age.
# Below the line where bmi was increased by 3.1 rewrite the insurance cost formula and assign it to the variable name new_insurance_cost
# Save the difference between new_insurance_cost and insurance_cost in a variable called change_in_insurance_cost
# Display the following string in the output 
# The change in estimated insurance cost after increasing BMI by 3.1 is change_in_insurance_cost dollars.
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost of insurance after increasing BMI by 3.1 is "+str(change_in_insurance_cost)+" dollars.")

# Task 10
# Looking at Male vs. Female Factor
# Let's look at the effect sex has on medical insurance costs. Before we make any additional changes, firrst reassign your bmi to original value 26.2
# on a new line of code, reassign the value of sex to 1
bmi = 26.2
sex = 1

# Task 11
# Perform the steps below
# rewrite the insurance cost formula and assign it to the variable name new_insurance_cost
# Save the differnce between new_insurance cost and insurance_cost in a variable called change_in_insurance_cost
# Display the following string in the output terminal
# The change in estimated cost for being male instead of female is change_in_insurance_cost dollars.
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is "+str(change_in_insurance_cost)+" dollars.")

# Task 12
# Notice that this time you got a negative value for change_in_insurance_cost. Let's think about what this means. We changed the sex variable from 0 to 1 (female to male) and it decreased the estimated insurance costs.
# This means that men tend to have lower medical costs on average than women. Reflect on the other findings you hae dug up from this investigation so far

# Task 13
# Extra Practice
# Great Job on the Project!!!
# So far we have looked at 3 of the 5 factors in the insurance costs fromula. The two remaining are smoker and num_of_children. If you want to keep challenging yourself, spend some time investigating these factors!

# resetting sex to 0 female
sex = 0

num_of_children += 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for 4 children instead of 3 is "+str(change_in_insurance_cost)+" dollars.")

# resetting no of children to 3
num_of_children = 3

smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being a smoker is "+str(change_in_insurance_cost)+" dollars.")
