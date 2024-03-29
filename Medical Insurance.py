age = 28
sex = 0  #female
bmi = 26.2
num_of_children = 3
smoker = 0

# insurance estimate 
insurance_cost = 250 * age - 128 * sex + 370 *bmi + 425 *num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 *bmi + 425 *num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 *bmi + 425 *num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Male vs. Female Factor
bmi = 26.2
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 *bmi + 425 *num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")


# Using function 
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria",28,0,26.2,3,0)
 
# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar",35,1,22.2,0,1)