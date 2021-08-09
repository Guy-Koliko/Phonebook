def console_card_printer(firstname, lastname, email, phonenumber):
    output = f"| Firstname: ' {firstname.upper()} '" \
             f" Lastname: ' {lastname.upper()} '" \
             f" Email: ' {email} '" \
             f" Phonenumber: ' {phonenumber} '" \
             " | "
    banner = "+" + "_" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) +"|"
    lines = (banner, border, output, border, banner)
    card = "\n".join(lines)
    print(card)
    print()