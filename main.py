
# Daftar buku perpustakaan (data buku)
library = [
    {"title": "Pelangi Basah", "author": "Diki", "year": 2020, "stock": 5},
    {"title": "Beri Aku Uang", "author": "Diki", "year": 2018, "stock": 3},
    {"title": "Pelangi Yang Indah", "author": "Diki", "year": 2019, "stock": 4},
    {"title": "Cinta Yang Bersemi", "author": "Aji", "year": 2021, "stock": 6},
    {"title": "Cinta Di Bawah Hujan", "author": "Aji", "year": 2015, "stock": 2},
    {"title": "Dua Garis Biru", "author": "Aji", "year": 2016, "stock": 5},
    {"title": "Love Song", "author": "Ditto", "year": 2017, "stock": 3},
    {"title": "Di Langit Ku", "author": "Ditto", "year": 2018, "stock": 4},
    {"title": "Kupu Kupu Malam", "author": "Ditto", "year": 2019, "stock": 6},
    {"title": "Aku Pulang", "author": "Didi", "year": 2020, "stock": 5},
    {"title": "Terjebak Cinta", "author": "Didi", "year": 2021, "stock": 3},
    {"title": "Indonesia Ku", "author": "Didi", "year": 2022, "stock": 4},
    {"title": "Lemah Lembut", "author": "Rafly", "year": 2023, "stock": 6},
    {"title": "Aku Dan Samudra", "author": "Rafly", "year": 2024, "stock": 2},
    {"title": "Dillan 1990", "author": "Rafly", "year": 2025, "stock": 5}
]

def search_books(keyword):
    # Fungsi untuk mencari buku berdasarkan kata kunci judul
    results = []
    for book in library:
        if keyword.lower() in book["title"].lower():
            results.append(book)
    return results

def display_books(books):
    # Fungsi untuk menampilkan daftar buku
    if not books:
        print("Tidak ada buku yang ditemukan")
    else:
        print("Buku yang ditemukan:")
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}, Stok: {book['stock']}")

def add_book():
    # Fungsi untuk menambahkan buku baru
    title = input("Masukkan judul buku: ")
    author = input("Masukkan penulis buku: ")
    year = int(input("Masukkan tahun terbit buku: "))
    stock = int(input("Masukkan jumlah stok buku: "))
    new_book = {"title": title, "author": author, "year": year, "stock": stock}
    library.append(new_book)
    print("Buku baru berhasil ditambahkan")

def buy_book():
    # Fungsi untuk membeli buku
    keyword = input("Masukkan judul buku yang ingin dibeli: ")
    results = search_books(keyword)
    if not results:
        print("Buku tidak ditemukan")
        return
    display_books(results)
    title = input("Masukkan judul lengkap buku yang ingin dibeli: ")
    for book in library:
        if title.lower() == book["title"].lower():
            if book["stock"] > 0:
                book["stock"] -= 1
                print(f"Anda telah membeli buku '{book['title']}'. Sisa stok: {book['stock']}")
            else:
                print("Stok buku habis")
            return
    print("Judul buku tidak valid")

def restock_book():
    # Fungsi untuk menambah stok buku
    keyword = input("Masukkan judul buku yang ingin ditambah stoknya: ")
    results = search_books(keyword)
    if not results:
        print("Buku tidak ditemukan")
        return
    display_books(results)
    title = input("Masukkan judul lengkap buku yang ingin ditambah stoknya: ")
    for book in library:
        if title.lower() == book["title"].lower():
            additional_stock = int(input("Masukkan jumlah stok tambahan: "))
            book["stock"] += additional_stock
            print(f"Stok buku '{book['title']}' telah ditambah. Jumlah stok sekarang: {book['stock']}")
            return
    print("Judul buku tidak valid")

def main():
    print("Selamat datang di perpustakaan!")
    while True:
        print("\nPilihan:")
        print("1. Cari buku")
        print("2. Tambah buku baru")
        print("3. Beli buku")
        print("4. Tambah stok buku")
        print("5. Keluar")
        choice = input("Masukkan pilihan Anda (1/2/3/4/5): ")
        if choice == "1":
            keyword = input("Masukkan kata kunci judul buku yang ingin dicari: ")
            results = search_books(keyword)
            display_books(results)
        elif choice == "2":
            add_book()
        elif choice == "3":
            buy_book()
        elif choice == "4":
            restock_book()
        elif choice == "5":
            print("Terima kasih telah menggunakan perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi")

if __name__ == "__main__":
    main()
