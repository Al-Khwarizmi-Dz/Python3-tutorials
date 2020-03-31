# variables
prenom = "Fares"
nom = "Herhar"
age = "22"

# concatinations des chaines
person = "Je suis " + prenom + " " + nom + ", et j'ai " + age + " ans."
print(person)

# formatting expression
person = "Je suis {} {}, et j'ai {} ans.".format(prenom, nom, age)
print(person)

# formatting expression with index
person = "Je suis {1} {0}, et j'ai {2} ans.".format(prenom, nom, age)
print(person)

# formatting expression with index maniupulation, and posisitions
country = "{0} is my country, {0} is {1}.".format("Algeria", "DZ")
print(country)

# a different syntax.
# both are correct.
country = "{0} is my country, {0} is {1}."
print(country.format("Algeria", "DZ"))
