class Undergraduate(object):
    book_list = {} # 每個人都共享這筆書單

    def __init__(self, name, book_limit=5):
        self.name = name
        self.limit = book_limit
        self.book = []

    @classmethod
    def add_book(cls, book_name, quantity):
        cls.book_list[book_name] = quantity
    
    @classmethod
    def search_book(cls, book_name):
        if book_name not in cls.book_list:
            print(f'{book_name} is not available in the library.')
        else:
            n = cls.book_list[book_name]
            print(f'{book_name} has {n} copies left.') 

    def borrow_book(self, book_name):
        if book_name not in self.__class__.book_list:
            print(f'{book_name} is not available in the library.')
            return
        if self.__class__.book_list[book_name] == 0:
            print(f'No copies of {book_name} left.')
            return
        if self.limit == 0:
            print(f'{self.name} has reached the borrow limit of {self.limit} books.')
            return
        
        self.book.append(book_name)
        self.limit -= 1
        self.__class__.book_list[book_name] -= 1

    def return_book(self, book_name):
        if book_name not in Undergraduate.book_list.keys():
            print(f'{book_name} is not available in the library.')
            return
        elif book_name not in self.book:
            print(f'{self.name} did not borrow {book_name}.')
            return
            
        self.book.remove(book_name)
        self.limit += 1
        self.__class__.book_list[book_name] += 1

    def showStatus(self):
        print("\n" + 
              f"--- {self.name}'s Status ---\n" +
              f"Borrowed Books: {sorted(self.book)}\n")

class Graduate(Undergraduate):
    lab_booked_list = []

    def __init__(self, name, book_limit=8):
        Undergraduate.__init__(self, name, book_limit)
        self.lab = {}

    def applyLAB(self, lab_id, date):
        if lab_id in self.__class__.lab_booked_list:
            print(f'Lab {lab_id} is already booked on {date}.')
        else:
            self.__class__.lab_booked_list.append(lab_id)
            self.lab[date] = lab_id

    def showStatus(self):
        print("\n" +
              f"--- {self.name}'s Status ---\n" +
              f"Borrowed Books: {sorted(self.book)}\n" +
              f"Reserved Labs: {dict(sorted(self.lab.items()))}\n")
    
class Professor(Graduate):
    con_booked_list = []

    def __init__(self, name, book_limit=10):
        Graduate.__init__(self, name, book_limit)
        self.confer = {}

    def applyConference(self, con_id, date):
        if con_id in self.__class__.con_booked_list:
            print(f'Conference Room {con_id} is already booked on {date}.')
        else:
            self.__class__.con_booked_list.append(con_id)
            self.confer[date] = con_id

    def showStatus(self):
        print("\n" +
              f"--- {self.name}'s Status ---\n" +
              f"Borrowed Books: {sorted(self.book)}\n" +
              f"Reserved Labs: {dict(sorted(self.lab.items()))}\n" +
              f"Reserved Conferences: {dict(sorted(self.confer.items()))}\n")


def main():
    raw = input().strip().split(' ')
    for i in range(0, len(raw), 2):
        name = raw[i]
        num = int(raw[i + 1])
        Undergraduate.add_book(name, num)

    user_map = {}

    while True:
        line = input().strip()
        # print(line)
        if line == 'EXIT':
            break

        parts = line.split()
        # print(parts)
        command = parts[0]

        if command == 'CREATE_USER':
            identity = parts[1]
            user_name = parts[2]
            if identity == 'U':
                user_map[user_name] = Undergraduate(user_name)
            elif identity == 'G':
                user_map[user_name] = Graduate(user_name)
            elif identity == 'P':
                user_map[user_name] = Professor(user_name)

        elif command == 'SEARCH':
            book_name = parts[1]
            Undergraduate.search_book(book_name)

        elif command == 'BORROW':
            user_name, book_name = parts[1], parts[2]
            if user_name in user_map:
                user_map[user_name].borrow_book(book_name)

        elif command == 'RETURN':
            user_name, book_name = parts[1], parts[2]
            if user_name in user_map:
                user_map[user_name].return_book(book_name)

        elif command == 'SHOW':
            user_name = parts[1]
            if user_name in user_map:
                user_map[user_name].showStatus()

        elif command == 'APPLY_LAB':
            user_name, date, lab_id = parts[1], parts[2], parts[3]
            if user_name in user_map:
                if isinstance(user_map[user_name], Undergraduate) and not isinstance(user_map[user_name], Graduate): 
                    print(f'{user_name} is not allowed to reserve labs.')
                else:
                    user_map[user_name].applyLAB(lab_id, date)

        elif command == 'APPLY_CONFERENCE':
            user_name, date, con_id = parts[1], parts[2], parts[3]
            if user_name in user_map:
                if isinstance(user_map[user_name], Professor):
                    user_map[user_name].applyConference(con_id, date)
                else:
                    print(f'{user_name} is not allowed to reserve conferences.')


if __name__ == "__main__":
    main()