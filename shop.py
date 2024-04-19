print("""
Welcome to your favorite childhood game:
I Went to the Shop and I Bought!
""")

# Initialize an empty list to store items
stuff_to_buy = []

# Main game loop
while True:
    # Ask the player for an item
    item = input("What did you buy? (type 'exit' to end the game) ")

    # Check if the player wants to stop adding items
    if item.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered

    # Add the item to the list
    stuff_to_buy.append(item)

    # Display the current list of items
    print("I went to the shop and I bought: " + ", ".join(stuff_to_buy))

# Game ended
print("Go raibh maith agat for playing!")
