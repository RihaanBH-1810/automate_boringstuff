import pyinputplus as Pyip

def get_sandwich():
    Breads = ["wheat", "white", "sourdough"]
    prs = ["chicken", "turkey", "ham","tofu"]

    print("""Welcome to the shop! 
          PLease enter your preferences for the sanwich:""")
    breadtype = Pyip.inputMenu(prompt="Bread Type : \n", choices=Breads, numbered=True,)
    protien_type = Pyip.inputMenu(prompt="Protien type : \n", choices=prs, numbered=True)
    cheese = Pyip.inputYesNo(prompt="Cheese ? : \n")
    no = Pyip.inputInt(prompt="How many sandwiches do you want ? : \n")

    exp  = {"wheat" :10, "white": 20, "sourdough": 30, "chicken" :10, "turkey" : 40, "ham" : 20 ,"tofu" : 20}
    
    price = 0
    price += exp[breadtype]
    price += exp[protien_type]
    if cheese:
        price += 30
    
    price *= no

    print(f"Your total bill is {price} rs.")

get_sandwich()
    