import json
import time
import os


class BookCollection:
    """📚 A class to manage a collection of books with add, remove, and list features."""
    
    def __init__(self):
        """Initialize the collection with an empty list of books."""
        self.book_list = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.storage_file = os.path.join(script_dir, "books_data.json")
        self.load_books()
    
    def load_books(self):
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, "r") as file:
                    self.book_list = json.load(file)
            else:
                self.book_list = []
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []
            print("⚠️ No file or invalid JSON found. Starting with an empty collection...")
            time.sleep(1)
    
    def save_books(self):
        try:
            with open(self.storage_file, "w") as file:
                json.dump(self.book_list, file, indent=4)
        except Exception as e:
            print(f"❌ Error saving books: {e}")
            time.sleep(1)
            
    def add_book(self):
        """Add a new book to the collection."""
        print("\n📖 Adding a New Book 📖")
        print("-----------------------")
        title = input("📚 Enter the title: ")
        author = input("✍️ Enter the author: ")
        publication_year = input("📅 Enter the publication year: ")
        book_genre = input("📝 Enter the genre: ")
        is_book_read = input("✅ Have you read this book? (y/n): ").strip().lower() == "y"
        
        new_book = {
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "genre": book_genre,
            "is_read": is_book_read
        }
        
        self.book_list.append(new_book)
        self.save_books()
        print("\n🎉 Book added successfully!")
        time.sleep(1)
    
    def delete_book(self):
        """Delete a book from the collection."""
        print("\n🗑️ Deleting a Book 🗑️")
        print("-----------------------")
        title_to_delete = input("📚 Enter the title to delete: ")
        for book in self.book_list:
            if book["title"].lower() == title_to_delete.lower():
                self.book_list.remove(book)
                self.save_books()
                print("\n✅ Book deleted successfully!")
                time.sleep(1)
                return
        print("\n❌ Book not found!")
        time.sleep(1)
    
    def list_books(self):
        """List all books in the collection."""
        print("\n📋 Listing All Books 📋")
        print("-----------------------")
        if not self.book_list:
            print("⚠️ No books in the collection.")
            time.sleep(1)
        else:
            for idx, book in enumerate(self.book_list, 1):
                print(f"\n📖 Book {idx}:")
                print(f"  Title: {book['title']}")
                print(f"  Author: {book['author']}")
                print(f"  Year: {book['publication_year']}")
                print(f"  Genre: {book['genre']}")
                print(f"  Read: {'Yes' if book['is_read'] else 'No'}")
            print()
            time.sleep(1)

    def search_book(self):
        """Search for a book by title."""
        print("\n🔍 Searching for a Book 🔍")
        print("-----------------------")
        title_to_search = input("📚 Enter the title to search: ")
        for book in self.book_list:
            if book["title"].lower() == title_to_search.lower():
                print("\n✅ Book found:")
                print(f"  Title: {book['title']}")
                print(f"  Author: {book['author']}")
                print(f"  Year: {book['publication_year']}")
                print(f"  Genre: {book['genre']}")
                print(f"  Read: {'Yes' if book['is_read'] else 'No'}")
                print()
                time.sleep(1)
                return
        print("\n❌ Book not found!")
        time.sleep(1)
            
    def update_book(self):
        """Update a book in the collection."""
        print("\n✏️ Updating a Book ✏️")
        print("-----------------------")
        title_to_update = input("📚 Enter the title to update: ")
        for book in self.book_list:
            if book["title"].lower() == title_to_update.lower():
                book["title"] = input("📚 Enter the new title: ")
                book["author"] = input("✍️ Enter the new author: ")
                book["publication_year"] = input("📅 Enter the new publication year: ")
                book["genre"] = input("📝 Enter the new genre: ")
                book["is_read"] = input("✅ Have you read this book? (y/n): ").strip().lower() == "y"
                updated_book = {
                    "title": book["title"],
                    "author": book["author"],
                    "publication_year": book["publication_year"],
                    "genre": book["genre"],
                    "is_read": book["is_read"]
                }
                self.book_list.remove(book)
                self.book_list.append(updated_book)
                self.save_books()
                print("\n🎉 Book updated successfully!")
                time.sleep(1)
                return
        print("\n❌ Book not found!")
        time.sleep(1)
    
    def view_reading_progress(self):
        """View the reading progress of the books."""
        print("\n📊 Reading Progress 📊")
        print("-----------------------")
        if not self.book_list:
            print("⚠️ No books in the collection.")
            time.sleep(1)
        else:
            total_books = len(self.book_list)
            read_books = sum(1 for book in self.book_list if book["is_read"])
            unread_books = total_books - read_books
            print(f"📚 Total books: {total_books}")
            print(f"✅ Read books: {read_books}")
            print(f"📖 Unread books: {unread_books}")
            print()
            time.sleep(1)
        
    def start_application(self):
        print("\n🌟 Welcome to Your Personal Library Manager 🌟")
        time.sleep(1)
        while True:
            print("\n📚 Main Menu 📚")
            print("==================")
            print("1️⃣ Add a book")
            print("2️⃣ Delete a book")
            print("3️⃣ List all books")
            print("4️⃣ Search for a book")
            print("5️⃣ Update a book")
            print("6️⃣ View reading progress")
            print("7️⃣ Exit")
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.list_books()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.update_book()
            elif choice == "6":
                self.view_reading_progress()
            elif choice == "7":
                print("\n👋 Exiting the application... Happy reading!")
                time.sleep(1)
                break
            else:
                print("\n❌ Invalid choice. Please try again.")
                time.sleep(1)

if __name__ == "__main__":
    print("🚀 Starting the Personal Library Manager...")
    time.sleep(1)
    book_collection = BookCollection()
    book_collection.start_application()
