bid = 0
highest_bid = 0
item = input("What is the auction for? ")
reserve_price = int(input("What is the reserve price? "))

print("\n"
      "The auction for the", item, "has started.\n")

while bid != -1:
    print("Highest bid so far:", highest_bid)
    bid = int(input("What is your bid? "))
    if bid > highest_bid:
        highest_bid = bid
    else:
        print("PLease enter a higher bid.")
    if bid == -1:
        break

print("\n"
      f"The auction for the", item, f"finished with a bid of ${highest_bid}")
