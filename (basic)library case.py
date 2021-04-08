"""
    Case 1:
    Ada seseorang yang bernama Glico, dengan id_member 1202114.
    Glico ingin meminjam buku sebanyak 2 buah.
    Case 2:
    Ada n orang ingin meminjam buku, masing-masing orang memiliki id_member, juga masing-masing meminjam buku.
    Case 3:
    Ada orang yang baru saja mendaftar sebagai member perpustakaan, memiliki data sebagai berikut:
    Nama: John
    Umur: 20 tahun
    Fakultas: Pendidikan
    ID member: 12345
    Status member: new
"""
# Case 1:
""""
name = input("Name: ")  # Create a string variable that will store the name of member
id_member = input("Id: ")   # Create a string variable that will store the id member of member
n_book = input("How much book you borrow: ") # Create a string variable that will store the numbers of book is borrow

print("Member dengan nama " + name)
print("Id member: " + id_member)
print("Ingin meminjam buku sebanyak " + n_book + " buah")
"""
# Case 2:
""""
list_name = []   # Create a name list to store the name of each member
list_id_member = []  # Create a id member list to store the data of each member id
list_n_book = []  # Create a n book list to store the data of how much the book that member borrow

# Create a n_people string variable to store of how much member are borrow book
n_people = int(input("How many of you?: "))

for i in range(n_people):
    name = input("Your name: ")  # Create a string variable 'name' to store name for each member
    list_name.append(name)  # Use append function to copy the data from 'name' to 'list_name'
    id_member = input("Your id member: ")
    list_id_member.append(id_member)    # Use append function to copy the data from 'id_member' to 'list_id_member'
    n_book = input("How much book you borrow?: ")
    list_n_book.append(n_book)  # Use append function to copy the data from 'n_book' to 'list_n_book'


print("List of members who borrow book: ", list_name)
print("List of each member id: ", list_id_member)
print("List of numbers of book that each member borrow: ", list_n_book)
"""
# Case 3:
""""
name = 'John'
age = '20 Tahun'
faculty = 'Pendidikan'
id_member = 12345
is_new = True

print("Member name:", name)
print("Age:", age)
print("Faculty:", faculty)
print("Active member:", is_new)
"""
