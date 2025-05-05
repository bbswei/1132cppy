from datetime import datetime

class InsuffError(Exception):
    pass

class BankAccount:
    def __init__(self, account_id, initial_balance, open_ym):
        self.account_id = account_id
        self.balance = initial_balance
        self.is_closed = False
        self.last_interest_ym = None
        self.open_ym = open_ym

    def deposit(self, amount): # 存入
        # TODO: Add the amount to the balance
        if self.is_closed:
            print("Account not found")
            return

        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError
        except (ValueError, TypeError):
            print("Invalid transaction amount")
            return
        
        self.balance += amount # 現在金額加上存款金額 Add the amount to the balance

    def withdraw(self, amount): # 領出
        # TODO: Check if the balance is sufficient and subtract the amount
        if self.is_closed:
            print("Account not found")
            return
        
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError
            elif amount > self.balance:
                raise InsuffError
        except (ValueError, TypeError):
            print("Invalid transaction amount")
        except InsuffError:
            print("Insufficient balance")
            return
        
        self.balance -= amount

    def apply_interest(self, current_ym):
        # TODO: Add 1% interest to the balance (truncate to integer)

        if self.is_closed:
            return

        if self.last_interest_ym is None:
            # 第一次套用利息，從開戶的月份開始算
            self.last_interest_ym = self.open_ym

        y1, m1 = self.last_interest_ym
        y2, m2 = current_ym
        gap = (y2 - y1) * 12 + (m2 - m1)

        for _ in range(gap):
            interest = int(self.balance * 0.01)
            self.balance += interest

        self.last_interest_ym = current_ym


    def close(self):
        # TODO: Mark the account as closed
        self.is_closed = True

    def is_active(self):
        # TODO: Return whether the account is still active
        return not self.is_closed

    def get_balance(self):
        # TODO: Return the current balance
        return int(self.balance)
    
    def transfer(self, target_acc, amount):
        if self.is_closed or target_acc.is_closed:
            print("Account not found")
            return

        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError
            if amount > self.balance:
                raise InsuffError
        except (ValueError, TypeError):
            print("Invalid transaction amount")
            return
        except InsuffError:
            print("Insufficient balance")
            return

        self.balance -= amount
        target_acc.balance += amount

def parse(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def main():
    """
    2021-10-15 DEPOSIT A 1000
    2021-10-20 OPEN A aa
    2021-10-25 OPEN B 500
    2021-10-31 OPEN C 600
    2021-11-01 OPEN D 1000
    2022-01-05 TRANSFER B D 500
    2022-01-05 BALANCE D
    q
    """
    accounts = {}
    last_interest_ym = None

    while True:
        command = input().strip()
        if command == "q":
            break

        parts = command.split()
        if not parts:
            continue

        date = parse(parts[0])
        year_month = (date.year, date.month)

        if last_interest_ym != year_month:
            for acc in accounts.values():
                if acc.is_active():
                    acc.apply_interest(year_month)
            last_interest_ym = year_month

        if parts[1] == "OPEN":
            acc_id = parts[2]
            try:
                balance = float(parts[3])
                if acc_id in accounts:
                    print("Account ID already exists")
                    continue
                else:
                    # accounts[acc_id] = BankAccount(acc_id, balance)
                    accounts[acc_id] = BankAccount(acc_id, balance, year_month)
            except:
                print("Invalid transaction amount")
                continue

        elif parts[1] == "DEPOSIT":
            acc_id = parts[2]
            if acc_id in accounts:
                accounts[acc_id].deposit(parts[3])
            else:
                print("Account not found")
                continue

        elif parts[1] == "WITHDRAW":
            acc_id = parts[2]
            if acc_id in accounts:
                accounts[acc_id].withdraw(parts[3])
            else:
                print("Account not found")
                continue
        
        elif parts[1] == "BALANCE":
            acc_id = parts[2]
            if acc_id in accounts:
                print(f"{acc_id} {accounts[acc_id].get_balance()}")
            else:
                print("Account not found")


        elif parts[1] == "TRANSFER":
            give_id = parts[2]
            take_id = parts[3]
            amount = parts[4]

            if give_id in accounts and take_id in accounts:
                accounts[give_id].transfer(accounts[take_id], amount)
            else:
                if give_id not in accounts:
                    print("Account not found")
                if take_id not in accounts:
                    print("Account not found")

        elif parts[1] == "CLOSE":
            acc_id = parts[2]
            if acc_id in accounts and accounts[acc_id].is_active():
                accounts[acc_id].close()
            else:
                print("Account not found")

main()

       