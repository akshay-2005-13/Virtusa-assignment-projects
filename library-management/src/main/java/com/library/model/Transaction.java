package com.library.model;
import java.time.LocalDate;
public class Transaction 
{
    private String transactionId;
    private Book book;
    private User user;
    private LocalDate borrowDate;
    private LocalDate dueDate;
    private LocalDate returnDate;
    private static final int LOAN_PERIOD_DAYS = 14;
    private static final double FINE_PER_DAY = 2.0;
    public Transaction(String transactionId, Book book, User user) 
    {
        this.transactionId=transactionId;
        this.book=book;
        this.user=user;
        this.borrowDate=LocalDate.now();
        this.dueDate=LocalDate.now().plusDays(LOAN_PERIOD_DAYS);
        this.returnDate=null;
    }
    public String getTransactionId() 
    {
        return transactionId;
    }
    public Book getBook() 
    {
        return book;
    }
    public User getUser() 
    {
        return user;
    }
    public LocalDate getBorrowDate() 
    {
        return borrowDate;
    }
    public LocalDate getDueDate() 
    {
        return dueDate;
    }
    public LocalDate getReturnDate() 
    {
        return returnDate;
    }
    public boolean isReturned() 
    {
        return returnDate!=null;
    }
    public void markAsReturned() 
    {
        this.returnDate=LocalDate.now();
    }
    public double calculateFine() 
    {
        if(!isReturned()) 
        {
            return 0.0;
        }
        if(returnDate.isAfter(dueDate)) 
        {
            long daysLate=dueDate.until(returnDate).getDays();
            return daysLate*FINE_PER_DAY;
        }
        return 0.0;
    }
    @Override
    public String toString() 
    {
        return "Transaction{" +
                "transactionId='" + transactionId + '\'' +
                ", book=" + book.getTitle() +
                ", user=" + user.getName() +
                ", borrowDate=" + borrowDate +
                ", dueDate=" + dueDate +
                ", returnDate=" + (isReturned() ? returnDate : "Not returned yet") +
                ", fine=" + calculateFine() +
                '}';
    }
}