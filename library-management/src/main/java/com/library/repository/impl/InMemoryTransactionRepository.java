package com.library.repository.impl;

import com.library.model.Transaction;
import com.library.repository.TransactionRepository;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public class InMemoryTransactionRepository implements TransactionRepository {

    private Map<String, Transaction> transactions = new HashMap<>();

    @Override
    public void save(Transaction transaction) {
        transactions.put(transaction.getTransactionId(), transaction);
    }

    @Override
    public Optional<Transaction> findById(String transactionId) {
        return Optional.ofNullable(transactions.get(transactionId));
    }

    @Override
    public List<Transaction> findByUserId(String userId) {
        return transactions.values().stream()
                .filter(transaction -> transaction.getUser()
                .getUserId()
                .equals(userId))
                .collect(Collectors.toList());
    }

    @Override
    public List<Transaction> findByIsbn(String isbn) {
        return transactions.values().stream()
                .filter(transaction -> transaction.getBook()
                .getIsbn()
                .equals(isbn))
                .collect(Collectors.toList());
    }

    @Override
    public Optional<Transaction> findActiveByUserAndBook(String userId, String isbn) {
        return transactions.values().stream()
                .filter(transaction -> transaction.getUser()
                .getUserId()
                .equals(userId))
                .filter(transaction -> transaction.getBook()
                .getIsbn()
                .equals(isbn))
                .filter(transaction -> !transaction.isReturned())
                .findFirst();
    }

    @Override
    public List<Transaction> findAllActive() {
        return transactions.values().stream()
                .filter(transaction -> !transaction.isReturned())
                .collect(Collectors.toList());
    }

    @Override
    public List<Transaction> findAll() {
        return new ArrayList<>(transactions.values());
    }
}