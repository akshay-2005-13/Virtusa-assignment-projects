package com.library.repository;

import com.library.model.Transaction;
import java.util.List;
import java.util.Optional;
public interface TransactionRepository 
{
    void save(Transaction transaction);
    Optional<Transaction> findById(String transactionId);
    List<Transaction> findByUserId(String userId);
    List<Transaction> findByIsbn(String isbn);
    Optional<Transaction> findActiveByUserAndBook(String userId, String isbn);
    List<Transaction> findAllActive();
    List<Transaction> findAll();
}