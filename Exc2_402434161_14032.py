def calculate():
    num1 = float(input("Lotfan adad aval ro vared konid: "))
    num2 = float(input("Lotfan adad dovom ro vared konid: "))

    summation = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2 if num2 != 0 else "na moshakhas"  # Jolo giri az taghsim bar sefr

    print(f"\nMojmou: {summation}")
    print(f"Tafavot: {difference}")
    print(f"Zarb: {product}")
    print(f"Taghsim: {division}")

    input("\nBaray khoroj, har klidi ro feshar bedid...")

calculate()