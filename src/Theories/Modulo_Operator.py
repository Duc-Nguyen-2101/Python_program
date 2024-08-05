####################################################
## Use modulo operator to split names into rows

####################################################

def split_names_into_rows(name_list, modulus=3):
    for index, name in enumerate(name_list, start=1):
        print(f"{name:-^15} ", end="")
        if index % modulus == 0:
            print()
    print()


names = ["Picard", "Riker", "Troi", "Crusher", "Worf", "Data", "La Forge"]
print("modulus = 3")
split_names_into_rows(names)    # Using modulus default defined inside the function which is 3
print("modulus = 1")
split_names_into_rows(names, 1) # Using modulus 1
print("modulus = 2")
split_names_into_rows(names, 2) # Using modulus 2
print("modulus = 4")
split_names_into_rows(names, 4) # Using modulus 4
print("modulus = 5")
split_names_into_rows(names, 5) # Using modulus 5
print("modulus = 6")
split_names_into_rows(names, 6) # Using modulus 6
print("modulus = 7")
split_names_into_rows(names, 7) # Using modulus 7
print("modulus = 8")
split_names_into_rows(names, 8) # Using modulus 8 which is bigger than the size of list
