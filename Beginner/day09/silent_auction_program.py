print("""
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
""")

def find_highest_bidder(bidding_dictionary):
    highest_bid = max(bidding_dictionary.values())
    print(highest_bid)
    winner = next(
        bidder for bidder, price in bidding_dictionary.items() 
            if price == highest_bid
    )
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    
    
bids = {}
continue_biddings = True
while continue_biddings:
    name = input('What is your name?: ')
    price = input('What is your bid?: $')
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if should_continue == 'no':
        continue_biddings = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

