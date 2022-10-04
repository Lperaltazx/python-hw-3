def shopping_cart():
shopping_list = []
while True:
user_question = input ("\welcome to your shopping list\n\n" + "Do you want to Show , Add , Delete , clear  or  to Quit: ")
if user_question.lower() == "show":

print(f"\nYour current shopping list:\n{shopping_list}")
if user_question. lower() = "add":
add = input ("what would you like to add?")
shopping_list.append (add)
print(f"\nYour current shopping list:\n{shopping_list}")
if user_question. lower) = 'delete':
remove = input("which Item would you like to remove?")
shopping_list.remove(remove)
print(f"in{remove} was removed from your shopping list. \n\n Here is your updated list:\n\n{shopping List}\n")
if Len(shopping_list) == 0:
print("Nothing to renove")
if user_question.lower0() = "clear"
shopping_list.clear()
print (f"\nYour shopping List has been cleared \n")
if user_question.lower() == "quit":
print(f"\nso long\n{shopping_list}")
break

shopping_cart ()







