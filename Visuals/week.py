class Week:
    def __int__(self,month, account_number):
        self.month = month
        self.account_number = account_number
        self.transactions = []
        self.total = 0

        # Totals up the spending for a specific week
    def total_sum(self):
        for transaction in range(len(self.transactions)):
            if 