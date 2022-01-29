
def word(texts):
    name=input("enter a name:")
    if not name.isalpha():
        raise NameError("pls enter a character!")
    rr=(f"{name}@gmail.com")
    return rr

print(word("isreal"))

#def recharge(network,number):
    #if len(number) > 11:
        #raise ValueError("number entered is over the limit!")
    #final=f"the {network} number is this {number}"
    #return final

#print(recharge(GLO,"08034061357"))

def grade_score(grade):
    grade=input("pls enter a grade A or B")
    if grade == "A":
        print("90%")
    elif grade == "B":
        print("45%")
    else:
        raise ValueError("incorrect input character")

grade_score("60")
