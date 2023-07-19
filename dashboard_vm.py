# Izzura Malindo - Python Backend X Data Engineer at Axrail
# Wednesday, July 19, 2023.

import streamlit as st #import library to running the app with streamlit 

st.title("AXRAIL Coffee Vending Machine")

st.text("Hello! Are You Ready for A Coffee Today? ;) ")

from PIL import Image
image = Image.open('vm.jpg')
st.image(image, caption='source: Unsplash.com')

#create 5 beverages for the vending machine
Beverage_info = [
   {
      "b_id": 1,
      "b_name": "Cinnamon Caramel Cream Cold Brew",
      'b_price': 19,
   },{
      "b_id": 2,
      "b_name": "Iced Americano",
      'b_price': 11,
   },{
      "b_id": 3,
      "b_name": "Iced Caramel Macchiato",
      'b_price': 16,
   },{
      "b_id": 4,
      "b_name": "Iced Caffe Mocha",
      'b_price': 15,
   },{
      "b_id": 5,
      "b_name": "Iced Dark Chocolate Mocha",
      'b_price': 18,
   },
]

def sum_order_by_cust(item):
    sumItems = 0
    for i in item:
        sumItems += i["b_price"]
    return sumItems

def createReceipt(item):
    receipt = "COFFEE NAME -- COST"
    for i in item:
        receipt += f"\n{i['b_name']} -- {i['b_price']}"
    receipt += f"\nTotal --- {sum_order_by_cust(item)}"
    return receipt

#create function for the logic of VM 
def vendingMachine(Beverage_info):
    item = []

    options = [f"{beverage['b_name']} - RM {beverage['b_price']}" for beverage in Beverage_info]
    buyItem = st.selectbox("Select the Coffee you want to buy:", options)

    buyItemIndex = options.index(buyItem)
    item.append(Beverage_info[buyItemIndex])

    receiptValue = st.radio("Choose an option:", ("Print the bill", "Print the total price of my order"))
    if receiptValue == "Print the bill":
        total_amount = sum_order_by_cust(item)
        receipt = createReceipt(item)
        st.text(receipt)
        amount_paid = st.number_input("Enter the amount you are paying:", min_value=0, step=1)
        change = amount_paid - total_amount
        st.text(f"\nChange to be returned: RM {change}")
        if change > 0:
            notes = [100, 50, 20, 10, 5, 1]  # Money notes in MYR without coins

            for note in notes:  # using if else condition to get the least amount of money notes
                num_notes = change // note
                change %= note
                if num_notes > 0:
                    st.text(f"RM {note} notes: {num_notes}")
    elif receiptValue == "Print the total price of my order":
        st.text(sum_order_by_cust(item))
    else:
        st.text("INVALID")

if __name__ == "__main__":
    vendingMachine(Beverage_info)
