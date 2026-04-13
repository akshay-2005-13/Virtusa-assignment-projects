package com.library.ui;

import com.library.model.Book;
import com.library.model.Transaction;
import com.library.model.User;
import com.library.service.LibraryService;
import java.util.List;
import java.util.Scanner;

public class LibraryCLI {

    private LibraryService libraryService;
    private Scanner scanner;

    public LibraryCLI(LibraryService libraryService) {
        this.libraryService = libraryService;
        this.scanner = new Scanner(System.in);
    }

    public void start() {
        System.out.println("========================================");
        System.out.println("   Welcome to Library Management System");
        System.out.println("========================================");

        boolean running = true;
        while (running) {
            printMainMenu();
            String choice = scanner.nextLine().trim();

            switch (choice) {
                case "1":
                    addBook();
                    break;
                case "2":
                    registerUser();
                    break;
                case "3":
                    borrowBook();
                    break;
                case "4":
                    returnBook();
                    break;
                case "5":
                    searchBooks();
                    break;
                case "6":
                    viewAllBooks();
                    break;
                case "7":
                    viewAllUsers();
                    break;
                case "8":
                    viewUserHistory();
                    break;
                case "9":
                    viewActiveTransactions();
                    break;
                case "0":
                    running = false;
                    System.out.println("Thank you for using Library Management System. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number from the menu.");
            }
        }
        scanner.close();
    }

    private void printMainMenu() {
        System.out.println("\n========================================");
        System.out.println("              MAIN MENU");
        System.out.println("========================================");
        System.out.println("1. Add Book");
        System.out.println("2. Register User");
        System.out.println("3. Borrow Book");
        System.out.println("4. Return Book");
        System.out.println("5. Search Books");
        System.out.println("6. View All Books");
        System.out.println("7. View All Users");
        System.out.println("8. View User Transaction History");
        System.out.println("9. View All Active Transactions");
        System.out.println("0. Exit");
        System.out.println("========================================");
        System.out.print("Enter your choice: ");
    }

    private void addBook() {
        System.out.println("\n--- Add New Book ---");
        try {
            System.out.print("Enter ISBN: ");
            String isbn = scanner.nextLine().trim();

            System.out.print("Enter Title: ");
            String title = scanner.nextLine().trim();

            System.out.print("Enter Author: ");
            String author = scanner.nextLine().trim();

            System.out.print("Enter Genre: ");
            String genre = scanner.nextLine().trim();

            System.out.print("Enter Total Copies: ");
            int totalCopies = Integer.parseInt(scanner.nextLine().trim());

            libraryService.addBook(isbn, title, author, genre, totalCopies);

        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Total copies must be a number.");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void registerUser() {
        System.out.println("\n--- Register New User ---");
        try {
            System.out.print("Enter User ID: ");
            String userId = scanner.nextLine().trim();

            System.out.print("Enter Name: ");
            String name = scanner.nextLine().trim();

            System.out.print("Enter Email: ");
            String email = scanner.nextLine().trim();

            libraryService.registerUser(userId, name, email);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void borrowBook() {
        System.out.println("\n--- Borrow Book ---");
        try {
            System.out.print("Enter User ID: ");
            String userId = scanner.nextLine().trim();

            System.out.print("Enter Book ISBN: ");
            String isbn = scanner.nextLine().trim();

            Transaction transaction = libraryService.borrowBook(userId, isbn);
            System.out.println("Transaction ID: " + transaction.getTransactionId());
            System.out.println("Borrow Date: " + transaction.getBorrowDate());
            System.out.println("Due Date: " + transaction.getDueDate());

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void returnBook() {
        System.out.println("\n--- Return Book ---");
        try {
            System.out.print("Enter User ID: ");
            String userId = scanner.nextLine().trim();

            System.out.print("Enter Book ISBN: ");
            String isbn = scanner.nextLine().trim();

            double fine = libraryService.returnBook(userId, isbn);
            if (fine > 0) {
                System.out.println("Fine to pay: Rs." + fine);
            }

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void searchBooks() {
        System.out.println("\n--- Search Books ---");
        System.out.println("1. Search by Title");
        System.out.println("2. Search by Author");
        System.out.print("Enter choice: ");

        String choice = scanner.nextLine().trim();

        try {
            if (choice.equals("1")) {
                System.out.print("Enter Title to search: ");
                String title = scanner.nextLine().trim();
                List<Book> books = libraryService.searchBooksByTitle(title);
                printBooks(books);

            } else if (choice.equals("2")) {
                System.out.print("Enter Author to search: ");
                String author = scanner.nextLine().trim();
                List<Book> books = libraryService.searchBooksByAuthor(author);
                printBooks(books);

            } else {
                System.out.println("Invalid choice.");
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void viewAllBooks() {
        System.out.println("\n--- All Books ---");
        List<Book> books = libraryService.getAllBooks();
        if (books.isEmpty()) {
            System.out.println("No books in the system.");
            return;
        }
        printBooks(books);
    }

    private void viewAllUsers() {
        System.out.println("\n--- All Users ---");
        List<User> users = libraryService.getAllUsers();
        if (users.isEmpty()) {
            System.out.println("No users registered.");
            return;
        }
        for (User user : users) {
            System.out.println("------------------------");
            System.out.println("ID    : " + user.getUserId());
            System.out.println("Name  : " + user.getName());
            System.out.println("Email : " + user.getEmail());
            System.out.println("Books : " + user.getBorrowedBooks().size()
                    + "/" + user.getMaxBorrowLimit());
        }
    }

    private void viewUserHistory() {
        System.out.println("\n--- User Transaction History ---");
        try {
            System.out.print("Enter User ID: ");
            String userId = scanner.nextLine().trim();

            List<Transaction> transactions =
                    libraryService.getUserTransactionHistory(userId);

            if (transactions.isEmpty()) {
                System.out.println("No transactions found for this user.");
                return;
            }
            printTransactions(transactions);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void viewActiveTransactions() {
        System.out.println("\n--- Active Transactions ---");
        List<Transaction> transactions =
                libraryService.getAllActiveTransactions();

        if (transactions.isEmpty()) {
            System.out.println("No active transactions.");
            return;
        }
        printTransactions(transactions);
    }

    private void printBooks(List<Book> books) {
        for (Book book : books) {
            System.out.println("------------------------");
            System.out.println("ISBN    : " + book.getIsbn());
            System.out.println("Title   : " + book.getTitle());
            System.out.println("Author  : " + book.getAuthor());
            System.out.println("Genre   : " + book.getGenre());
            System.out.println("Copies  : " + book.getAvailableCopies()
                    + "/" + book.getTotalCopies());
        }
    }

    private void printTransactions(List<Transaction> transactions) {
        for (Transaction t : transactions) {
            System.out.println("------------------------");
            System.out.println("Transaction ID : " + t.getTransactionId());
            System.out.println("Book           : " + t.getBook().getTitle());
            System.out.println("User           : " + t.getUser().getName());
            System.out.println("Borrow Date    : " + t.getBorrowDate());
            System.out.println("Due Date       : " + t.getDueDate());
            System.out.println("Return Date    : " +
                    (t.isReturned() ? t.getReturnDate() : "Not returned yet"));
            System.out.println("Fine           : Rs." + t.calculateFine());
        }
    }
}