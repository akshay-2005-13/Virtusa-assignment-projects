package com.library.repository.impl;

import com.library.model.Book;
import com.library.repository.BookRepository;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public class InMemoryBookRepository implements BookRepository {

    private Map<String, Book> books = new HashMap<>();

    @Override
    public void save(Book book) {
        books.put(book.getIsbn(), book);
    }

    @Override
    public Optional<Book> findByIsbn(String isbn) {
        return Optional.ofNullable(books.get(isbn));
    }

    @Override
    public List<Book> findAll() {
        return new ArrayList<>(books.values());
    }

    @Override
    public List<Book> findByTitle(String title) {
        return books.values().stream()
                .filter(book -> book.getTitle()
                .toLowerCase()
                .contains(title.toLowerCase()))
                .collect(Collectors.toList());
    }

    @Override
    public List<Book> findByAuthor(String author) {
        return books.values().stream()
                .filter(book -> book.getAuthor()
                .toLowerCase()
                .contains(author.toLowerCase()))
                .collect(Collectors.toList());
    }

    @Override
    public void delete(String isbn) {
        books.remove(isbn);
    }

    @Override
    public boolean existsByIsbn(String isbn) {
        return books.containsKey(isbn);
    }
}