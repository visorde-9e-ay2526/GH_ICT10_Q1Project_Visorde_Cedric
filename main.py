#receipt_generator
from pyscript import display, document


def calculate_price(e):
    document.getElementById("result").innerHTML = ''
    smallNumber = 0
    smallNumber = float(document.getElementById("Egg1").value)
    smallPrice = smallNumber * 68 #total price of small eggs
    smallNumberA = float(document.getElementById("Egg4").value)
    smallPriceA = smallNumberA * 102
    mediumNumber = 0
    mediumNumber = float(document.getElementById("Egg2").value)
    mediumPrice = mediumNumber * 100 #total price of large eggs
    mediumNumberA = float(document.getElementById("Egg5").value)
    mediumPriceA = mediumNumberA * 150
    largeNumber = 0
    largeNumber = float(document.getElementById("Egg3").value)
    largePrice = largeNumber * 129 #total price of large eggs
    largeNumberA = float(document.getElementById("Egg6").value)
    largePriceA = largeNumberA * 193.5
    subtotal = smallPrice + smallPriceA + mediumPrice + mediumPriceA + largePrice + largePriceA #calculate subtotal
    Vat = subtotal * 0.12 #calculate vat value
    total = subtotal + Vat #calculate total

    #display values
    display(f'The subtotal is {subtotal}', target='result')
    display(f'VAT: {Vat}', target='result')
    display(f'The total is {total}', target='result')

def generate_sku(e):
    document.getElementById("result").innerHTML = ''
    item_quantity = document.getElementById("quantity").value
    item_size = document.getElementById("size").value

    display(f'SKU: EGG_{item_quantity}_{item_size}', target='result')