class india():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Democratic Republic")

class bangladesh():
    def capital(self):
        print("Dhaka")
    def language(self):
        print("Bengali")
    def type(self):
        print("Unitary Parliamentary Republic")

obj_ind = india()
obj_bang = bangladesh()
for country in (obj_ind, obj_bang):
    country.capital()
    country.language()
    country.type()
# test_obj.print_value(20)  # Removed or comment out this line to avoid NameError