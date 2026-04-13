package com.library;

import com.library.repository.BookRepository;
import com.library.repository.TransactionRepository;
import com.library.repository.UserRepository;
import com.library.repository.impl.InMemoryBookRepository;
import com.library.repository.impl.InMemoryTransactionRepository;
import com.library.repository.impl.InMemoryUserRepository;
import com.library.service.LibraryService;
import com.library.ui.LibraryCLI;

public class Main {

    public static void main(String[] args) {

        // Step 1 — create repositories
        BookRepository bookRepository = new InMemoryBookRepository();
        UserRepository userRepository = new InMemoryUserRepository();
        TransactionRepository transactionRepository = new InMemoryTransactionRepository();

        // Step 2 — inject repositories into service
        LibraryService libraryService = new LibraryService(
                bookRepository,
                userRepository,
                transactionRepository
        );

        // Step 3 — inject service into CLI
        LibraryCLI cli = new LibraryCLI(libraryService);

        // Step 4 — start the application
        cli.start();
    }
}