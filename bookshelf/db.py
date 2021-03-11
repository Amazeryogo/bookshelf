import psycopg2

db = psycopg2.connect(database="clumsy-cat-1208.books", user="suvid", password="intelnucjalgaya",
                      host="free-tier.gcp-us-central1.cockroachlabs.cloud", port="26257")
cursor = db.cursor()

def alter(bool1):
    if bool1 == "True":
        return True
    else:
        return False

def addbooks(title, author, isbn, owner, read, borrow, genre,pages):
    borrow = alter(borrow)
    query = '''INSERT INTO books.kalicat(title,author,isbn,owner,read,borrowed,genre,pages) VALUES ('{}','{}','{}','{}','{}',{},'{}','{}');'''.format(
        title, author, isbn, owner, read, borrow, genre,pages)
    cursor.execute(query)
    db.commit()
    print("done")
    return "done"


def getbookdata():
    query = '''SELECT * FROM books.kalicat'''
    cursor.execute(query)
    data = cursor.fetchall()
    return data
