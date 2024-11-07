############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: 

# main() FUNCTION

def new(letterGrade,modifier):

# Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    elif modifier == "":
            numericGrade
            return numericGrade

def main():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

     #Gather user inputs
    PROG1700=input("Please enter a letter grade for PROG1700:")
    PROG1700mod=input("Please enter a modifier (+, - or nothing) :")
    PROG=new(PROG1700,PROG1700mod)
    NETW1700=input("Please enter a letter grade for NETW1700:")
    NETW1700mod=input("Please enter a modifier (+, - or nothing) :")
    NETW=new(NETW1700,NETW1700mod)
    OSYS1200=input("Please enter a letter grade for OSYS1200:")
    OSYS1200mod=input("Please enter a modifier (+, - or nothing) :")
    OSYS=new(OSYS1200,OSYS1200mod)
    WEBD1000=input("Please enter a letter grade for WEBD1000:")
    WEBD1000mod=input("Please enter a modifier (+, - or nothing) :")
    WEBD=new(WEBD1000,WEBD1000mod)
    COMM1700=input("Please enter a letter grade for COMM1700:")
    COMM1700mod=input("Please enter a modifier (+, - or nothing) :")
    COMM=new(COMM1700,COMM1700mod)
    DBAS1007=input("Please enter a letter grade for DBAS1007:")
    DBAS1007mod=input("Please enter a modifier (+, - or nothing) :")
    DBAS=new(DBAS1007,DBAS1007mod)
    avg=(PROG+NETW+OSYS+WEBD+COMM+DBAS)/6
    
    print("The numeric value for PROG1700 is: ",PROG)
    print("The numeric value for PROG1700 is: ",NETW)
    print("The numeric value for PROG1700 is: ",OSYS) 
    print("The numeric value for PROG1700 is: ",WEBD)
    print("The numeric value for PROG1700 is: ",COMM)
    print("The numeric value for PROG1700 is: ",DBAS)
    print("Your grade point average for the semester is:",avg)
main()