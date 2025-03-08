def get_integer_part():
    num = float(input("Lotfan yek adad ashari vared konid: "))  # User inputs a decimal number
    
    integer_part = int(num)  # Giraftan ghesmat sahih adad
    
    print(f"\nGhesmat sahih adad vared shode: {integer_part}")
    
    input("\nBaray khoroj, har klidi ro feshar bedid...")  # Prompt for exit

get_integer_part()