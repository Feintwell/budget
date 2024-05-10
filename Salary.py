def main ():
  
    salary = getsalary ()
    electricity = getelectricity ()
    water = getwater()
    groceries = getgroceries()
    electric = calelectric (salary, electricity)
    waterbill = calwaterbill (water, salary)
    shopping = calgroceries (groceries, salary)
    expense = calexpense (groceries, water, electricity)
    deduct = caldeduct (expense, salary)



   
    displayelectric (electric)
    displaywater (waterbill)
    displayshopping (shopping)
    displayexpense (expense)
    displaydeduct (deduct)


def getsalary (): 
    salary = int(input("Please enter your monthly salary: "))
    return salary

#get the electricity
def getelectricity ():
    electricity = int(input("Please enter your electricity bill: "))
    return electricity

#get the water
def getwater ():
    water = int(input("Please enter your water bill: "))
    return water

#get the groceries 
def getgroceries ():
    groceries = int(input("Please enter your groceries bill: "))
    return groceries


#Calculate the electric hours
def calelectric (salary, electricity):
    electric = salary - electricity
    return electric

#Calculate water pay
def calwaterbill (water, salary) :
    waterbill = salary - water
    return waterbill

#Calculate groceries pay
def calgroceries (groceries, salary) :
    shopping = salary - groceries
    return shopping

'''
#Calculate deductions
def caldeduct (weeklypay) :
    deduct = weeklypay * (5/100)
    return deduct

#Calculate deductions
def caldeducti (after) :
    afterde = after * (10/100)
    return afterde

'''

#Calculate deductions
def calexpense (groceries, water, electricity) :
    expense = groceries + water + electricity
    return expense


#Calculate weekly deduction
def caldeduct (expense, salary) :
    deduct = salary - expense
    return deduct


  
#output deduction
def displayelectric (electric):
    print (f"Your salary after paying the electricity bill is ${electric}")

#output contribution
def displaywater (waterbill) :
    print (f"Your salary after paying the water bill is ${waterbill}")

#output weekly pay
def displayshopping (shopping) :
    print (f"Your salary after groceries pay is ${shopping}")


#output weekly pay
def displayexpense (expense) :
    print (f"Your total expense is ${expense}")

#output weekly pay
def displaydeduct (deduct) :
    print (f"Your savings is ${deduct}")

main ()