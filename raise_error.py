
def word(texts):
    if not texts.isalpha():
        raise NameError("pls enter a character!")
    rr=(f"{texts}@gmail.com")
    return rr



def recharge(network,number):
    if len(number) > 11:
        raise ValueError("number entered is over the limit")
    elif not network.isalpha():
        raise TypeError("incorrect character")
    final=f"the {network} number is this {number}"
    return final

#print(recharge("Glo","08034061357"))

def grade_score():
    grade=input("pls enter a grade A or B")
    if grade == "A":
        print("90%")
    elif grade == "B":
        print("45%")
    else:
        raise ValueError("incorrect input character")


