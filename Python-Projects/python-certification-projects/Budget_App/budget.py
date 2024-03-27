class Category:

    def __init__(self, name): # initialize budget category object
        self.name = name
        self.ledger = [] # an instance variable called ledger, a list

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):   # if this returns True
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
        # if not enough funds, nothing adds to the ledger

    def get_balance(self): 
        balance = 0
        for item in self.ledger:
            balance += item['amount'] 
        return balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.name}')
            destination.deposit(amount, f'Transfer from {self.name}') 
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        output = self.name.center(30, '*') + '\n'
        for item in self.ledger:
            description = item['description'][:23]
            amount = '{:.2f}'.format(item['amount']).rjust(30 - len(description))
            output += f'{description}{amount}\n'
        output += f'Total: {self.get_balance()}'
        return output


def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    spending_list_per_category = []

    # Calculate spending percentage for each category
    for category in categories:
        spending = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        spending_list_per_category.append(spending)

    total_spending = sum(spending_list_per_category)

    bar_list = [int((s / total_spending) * 100 / 10) for s in spending_list_per_category]

    for i in range(100, -1, -10): # outer loop
        chart += f"{i:3}| " 
        
        # every i will be compared to each item in bar_list three times, thus generating the whole line ...
        for bar in bar_list: # I can't believe line 61 - 64 took me the whole day to not figure it out ...  # inner loop
            if i / 10 <= bar: # comparing the percentage label with each bar item. Every time the inner loop iterates, it iterates through every item in the bar_list. 
                chart += 'o  ' # if the item in the bar_list is bigger than the percentage/10, there should be a bar
            else : chart += '   ' # if not, 3 spaces. Then it goes onto the next bar to iterate .... 
            

        chart += '\n'

    chart += '    ' + '-' * (3 * len(categories) + 1) + '\n'

    max_name_length = max(len(category.name) for category in categories)

    for i in range(max_name_length):
        chart += '     '
        for category in categories:
            chart += category.name[i] if i < len(category.name) else ' '
            chart += '  '
        chart += '\n'

    return chart.strip() + '  '






