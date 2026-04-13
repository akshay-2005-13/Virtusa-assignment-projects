package com.library.service;

import com.library.exception.BookNotAvailableException;
import com.library.exception.BookNotFoundException;
import com.library.exception.MaxBorrowLimitException;
import com.library.exception.UserNotFoundException;
import com.library.model.Book;
import com.library.model.Transaction;
import com.library.model.User;
import com.library.repository.BookRepository;
import com.library.repository.TransactionRepository;
import com.library.repository.UserRepository;
import java.util.List;
import java.util.UUID;

public class LibraryService {

    private BookRepository bookRepository;
    private UserRepository userRepository;
    private TransactionRepository transactionRepository;

    public LibraryService(BookRepository bookRepository,
                          UserRepository userRepository,
                          TransactionRepository transactionRepository) {
        this.bookRepository = bookRepository;
        this.userRepository = userRepository;
        this.transactionRepository = transactionRepository;
    }

    public void addBook(String isbn, String title, String author,
                        String genre, int totalCopies) {
        if (bookRepository.existsByIsbn(isbn)) {
            throw new IllegalArgumentException(
                "Book already exists with ISBN: " + isbn);
        }
        Book book = new Book(isbn, title, author, genre, totalCopies);
        bookRepository.save(book);
        System.out.println("Book added successfully: " + title);
    }

    public void registerUser(String userId, String name, String email) {
        if (userRepository.existsById(userId)) {
            throw new IllegalArgumentException(
                "User already exists with ID: " + userId);
        }
        if (userRepository.findByEmail(email).isPresent()) {
            throw new IllegalArgumentException(
                "Email already registered: " + email);
        }
        User user = new User(userId, name, email);
        userRepository.save(user);
        System.out.println("User registered successfully: " + name);
    }

    public Transaction borrowBook(String userId, String isbn) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new UserNotFoundException(userId));

        Book book = bookRepository.findByIsbn(isbn)
                .orElseThrow(() -> new BookNotFoundException(isbn));

        if (user.hasReachedBorrowLimit()) {
            throw new MaxBorrowLimitException(
                user.getName(), user.getMaxBorrowLimit());
        }

        if (!book.isCopyAvailable()) {
            throw new BookNotAvailableException(book.getTitle());
        }

        if (user.hasBorrowed(isbn)) {
            throw new IllegalStateException(
                "User already has this book borrowed");
        }

        book.decrementCopy();
        user.addBorrowedBook(book);

        String transactionId = UUID.randomUUID().toString();
        Transaction transaction = new Transaction(transactionId, book, user);
        transactionRepository.save(transaction);

        System.out.println("Book borrowed successfully!");
        System.out.println("Due date: " + transaction.getDueDate());

        return transaction;
    }

    public double returnBook(String userId, String isbn) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new UserNotFoundException(userId));

        Book book = bookRepository.findByIsbn(isbn)
                .orElseThrow(() -> new BookNotFoundException(isbn));

        Transaction transaction = transactionRepository
                .findActiveByUserAndBook(userId, isbn)
                .orElseThrow(() -> new IllegalStateException(
                    "No active borrowing found for this book and user"));

        transaction.markAsReturned();
        book.incrementCopy();
        user.removeBorrowedBook(isbn);

        double fine = transaction.calculateFine();
        if (fine > 0) {
            System.out.println("Book returned late! Fine: Rs." + fine);
        } else {
            System.out.println("Book returned successfully! No fine.");
        }

        return fine;
    }

    public List<Book> searchBooksByTitle(String title) {
        List<Book> results = bookRepository.findByTitle(title);
        if (results.isEmpty()) {
            System.out.println("No books found with title: " + title);
        }
        return results;
    }

    public List<Book> searchBooksByAuthor(String author) {
        List<Book> results = bookRepository.findByAuthor(author);
        if (results.isEmpty()) {
            System.out.println("No books found by author: " + author);
        }
        return results;
    }

    public List<Book> getAllBooks() {
        return bookRepository.findAll();
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public List<Transaction> getUserTransactionHistory(String userId) {
        if (!userRepository.existsById(userId)) {
            throw new UserNotFoundException(userId);
        }
        return transactionRepository.findByUserId(userId);
    }

    public List<Transaction> getAllActiveTransactions() {
        return transactionRepository.findAllActive();
    }
}