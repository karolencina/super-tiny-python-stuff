# String concatenation (putting strings together)
# Goal: create a string that says "Subscribe to _____"

person = "Karolinita"  # some string variable

# Various ways of printing stuff:

print("This is " + person + ".")
print("Say hello to {}.".format(person))

# This is the same as template literals in JS! ^^ (`blahblahblah${var}`)
print(f"I am {person}.")

# MADLIP

adj0 = input("Adjective: ")
adj1 = input("Adjective: ")
verb0 = input("Verb: ")
verb1 = input("Verb: ")
noun0 = input("Noun: ")

madlip = f"Computer programming is so {adj0}! It makes me so excited " \
         f"all the time because I love to {verb0}. " \
         f"Stay {adj1} and {verb1} like you are a {noun0}!"

print(madlip)
