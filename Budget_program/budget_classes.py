class Entry:
    def __init__(self, amount=0):
        self.amount = amount


class IncomeEntry(Entry):
    def __init__(self, amount=0, sender="", extra_information=""):
        super().__init__(amount)
        self.sender = sender
        self.extra_information = extra_information

    def __repr__(self):
        return f"{self.amount}, {self.sender}, {self.extra_information}"


class ExpenseEntry(Entry):
    def __init__(self, amount=0, payment_option="", bought_goods_or_services=""):
        super().__init__(amount)
        self.payment_option = payment_option
        self.bought_goods_or_services = bought_goods_or_services

    def __repr__(self):
        return f"{self.amount}, {self.payment_option}, {self.bought_goods_or_services}"


class Budget:
    JOURNAL = []

    def __init__(self, entry):
        self.JOURNAL.append(entry)

    @classmethod
    def get_balance(cls):
        amounts = []
        for entry in cls.JOURNAL:
            amounts.append(entry.amount)
        return sum(amounts)

    @classmethod
    def get_entries(cls):
        entries = []
        for entry in cls.JOURNAL:
            if isinstance(entry, IncomeEntry):
                entry = [entry.amount, entry.sender, entry.extra_information]
            else:
                entry = [entry.amount, entry.payment_option, entry.bought_goods_or_services]
            entries.append(entry)
        return entries