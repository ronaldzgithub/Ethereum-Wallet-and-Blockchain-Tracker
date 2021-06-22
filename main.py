import requests
import classes

print("\n\t\t~~~ Welcome to the Ethereum Tracker Program ~~~\n")
run = True

while run:

    choice = input("""~~~ Would you like to explore an individual wallet or the blockchain as a whole? ~~~\n
    \t\t\t    [1] Individual Wallet\n
    \t\t\t    [2] Whole Blockchain\n
    \t\t\t    [3] Exit\n
    """)

    if choice == '1':

        active_wallet = classes.wallet()

        while active_wallet.active:

            active_wallet.operation_choice()

    elif choice == "2":

        block_chain = classes.blockchain()

        while block_chain.active:

            block_chain.operation_choice()

    elif choice == "3":
        
        run = False

    else:

        print("\n\t\t  [ERROR] Please input a valid choice! [ERROR]\n")