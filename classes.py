import requests
import matplotlib

class wallet:

    def __init__(self):
        
        self.wallet = input("\t\t~~~ Please type in a valid wallet address ~~~\n")
        while self.wallet[:2] != '0x' or len(self.wallet) != len('0x02A4F3931672b5615c41F3671669e27fd669CB31'):
            self.wallet = input("\t\t[ERROR] Please type in a VALID wallet address [ERROR]\n")

        self.active = True
        self.operation_choice()

    def operation_choice(self):
        choice = input(f"""\n\t\t ~~~ You are currently exploring {self.wallet} ~~~\n
            \t\t\t    ~~~ What would you like to do? ~~~\n
            \t\t\t[1]  Get the current wallet's data\n
            \t\t\t[2]  Get the current wallet's transaction data\n
            \t\t\t[3]  Change the current wallet\n
            \t\t\t[4]  Return to program overview\n
            """)
        if choice == '1':
            self.get_wallet_data()
        elif choice == '2':
            self.get_wallet_transactions()
        elif choice == '3':
            self.change_current_wallet()
        elif choice == '4':
            self.program_overview()

    def get_wallet_data(self):

        url = 'https://api.etherscan.io/api?module=account&action=balance&address=' + self.wallet + '&tag=latest&apikey=4XDW9G2CVB2M87CYP1MWM3F77R4WM8KFIP'
        response = requests.get(url)

        response_json = response.json()

        result = str(int(response_json.get('result')) / 1000000000000000000)

        print(self.wallet + ' Balance: ' + result)

    def get_wallet_transactions(self):

        url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + self.wallet + '&startblock=0&endblock=99999999&sort=asc&apikey=4XDW9G2CVB2M87CYP1MWM3F77R4WM8KFIP'
        response = requests.get(url)

        response_json = response.json()
        result = response_json.get('result')

        no_value = input("Would you like to view 0 value transactions? Y/N ")

        for id, tx in enumerate(result):
            
            if tx.get('value') == '0' and no_value.lower() == 'n':
                continue
            else:
                print("Transaction ID: " + str(id + 1))
                print("Ethereum Sent: " + str(int(tx.get('value')) / 1000000000000000000))
                print("Recipient Address: " + str(tx.get('to')))
                print('\n')

    def change_current_wallet(self):
        
        self.wallet = input("\t\t~~~ Please type in a valid wallet address ~~~\n")
        while self.wallet[:2] != '0x' or len(self.wallet) != len('0x02A4F3931672b5615c41F3671669e27fd669CB31'):
            self.wallet = input("\t\t[ERROR] Please type in a VALID wallet address [ERROR]\n")

    def track_interacted_wallets(self):
        pass

    def program_overview(self):

        self.active = False

class blockchain:

    def __init__(self):
        
        self.active = True
        self.operation_choice()

    def operation_choice(self):

        
        choice = input("""\n\t\t ~~~ You are currently exploring the Ethereum Blockchain ~~~\n
            \t\t     ~~~ What would you like to do? ~~~\n
            \t\t\t[1]  Get general data\n
            \t\t\t[2]  View price or historical price\n
            \t\t\t[3]  View historical market cap\n
            \t\t\t[4]  Return to program overview\n
            """)
        if choice == '1':
            self.get_general_data()
        elif choice == '2':
            self.view_historical_price()
        elif choice == '3':
            self.view_historical_market_cap()
        elif choice == '4':
            self.program_overview()

    def get_general_data(self):

        url = 'https://api.etherscan.io/api?module=stats&action=ethsupply&apikey=4XDW9G2CVB2M87CYP1MWM3F77R4WM8KFIP'
        response = requests.get(url)
        response_json = response.json()
        result = response_json.get('result')

        print("The total supply of Eth is: " + str(int(result) / 1000000000000000000))

     # PRO VERSION OF API IS NEEDED TO GET HISTORICAL DATA
    def view_historical_price(self):

        choice = input("Would you like to view the current price or a historical price? C/H")

        if choice.upper() == "C":
            url = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=4XDW9G2CVB2M87CYP1MWM3F77R4WM8KFIP'
            response = requests.get(url)
            response_json = response.json()
            result = response_json.get('result')


            print("ETH <--> BTC: " + result.get('ethbtc'))
            print("ETH <--> USD: " + result.get('ethusd'))

        elif choice.upper() == "H":

            print("Please put in a FROM and TO date (yyyy-mm-dd):")
            from_ = input("From: ")
            to_ = input("To: ")

            date = []
            price = []

    # PRO VERSION OF API IS NEEDED FOR HISTORICAL MARKET CAP
    def view_historical_market_cap(self):

        pass

    def program_overview(self):

        self.active = False