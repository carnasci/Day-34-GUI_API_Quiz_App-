#Type Hints and Arrows

#Declaring data types of variables
# age: 12
# name: str
# height: float
# is_human: bool

#Declaring type and using arrow in method for hints when creating a method
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(12):
    print("You may pass")
else:
    print("Pay fine")