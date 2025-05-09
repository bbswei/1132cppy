class BookManage:
    def __init__(self, title, authors, pub_year, edit):
        self.title = title 
        self.authors = authors.split(', ') # 變成 list 比較好處理
        self.pub_year = pub_year
        self.edition = edit

    def add_author(self, added_author):
        self.authors.append(added_author)

    def remove_author(self, del_author):
        # print(self.authors)
        # print(del_author)
        self.authors.remove(del_author)

    def update_edition(self, ud_edition):
        self.edition = ud_edition

    def update_publication_year(self, ud_year):
        self.pub_year = ud_year

    def update_title(self, ud_title):
        self.title = ud_title

    def __str__(self):
        # Sample: Title: Linear Algebra; Authors: Andrew Waldron, David Cherney, Rohit Thomas, Tom Denton; Year: 2013; Edition: Second
        au = ", ".join(sorted(self.authors))
        return (f"Title: {self.title}; Authors: {au}; Year: {self.pub_year}; Edition: {self.edition}")

if __name__ == "__main__":
    book_num = int(input())

    for _ in range(book_num):
        info = []
        while True:
            line = str(input())
            info.append(line)
        
            if line == '-':
                break

        info = [i for i in info if i != '---' and i != '-']
        # print(info)
        for idx, item in enumerate(info):
            if idx == 0:
                title = item
            if idx == 1:
                authors = item
            if idx == 2:
                pub_year = item
            else:
                edition = item
        # print(book_info)

        book = BookManage(title, authors, pub_year, edition)

        actions = []

        while True:
            operation = str(input())
            actions.append(operation)
            if operation == '---':
                break

        actions = [i for i in actions if i != '---' and i != '-']
        # print(actions)

        for item in actions:
            item = item.split(maxsplit=1)
            action = item[0]
            arg = item[1] if len(item) > 1 else None
            # print(action)
            if action == 'add_author':
                book.add_author(arg)
            elif action == 'rm_author':
                book.remove_author(arg)
            elif action == 'update_edition':
                book.update_edition(arg)
            elif action == 'update_pubyear':
                book.update_publication_year(arg)
            elif action == 'update_title':
                book.update_title(arg)
            else:
                print(book)
            # elif action == 'print':
            #     print(book)