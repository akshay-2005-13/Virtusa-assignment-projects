package com.library.model;
import java.util.ArrayList;
import java.util.List;
public class User 
{
    private String userId;
    private String name;
    private String email;
    private List<Book> borrowedBooks;
    private static final int borrow_limit=3;
    public User(String userId, String name, String email) 
    {
        this.userId = userId;
        this.name = name;
        this.email = email;
        this.borrowedBooks = new ArrayList<>();
    }
    public String getUserId() 
    {
        return userId;
    }
    public String getName() 
    {
        return name;
    }
    public String getEmail() 
    {
        return email;
    }
    public List<Book> getBorrowedBooks() 
    {
        return borrowedBooks;
    }
    public int getMaxBorrowLimit() 
    {
        return borrow_limit;
    }
    public boolean hasReachedBorrowLimit() 
    {
        return borrowedBooks.size()>=borrow_limit;
    }
    public boolean hasBorrowed(String isbn) 
    {
        for(Book book : borrowedBooks) 
        {
            if(book.getIsbn().equals(isbn)) 
            {
                return true;
            }
        }
        return false;
    }
    public void addBorrowedBook(Book book) 
    {
        borrowedBooks.add(book);
    }
    public void removeBorrowedBook(String isbn) 
    {
        borrowedBooks.removeIf(book->book.getIsbn().equals(isbn));
    }
    @Override
    public String toString() 
    {
        return "User{" +
                "userId='" + userId + '\'' +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", borrowedBooks=" + borrowedBooks.size() +
                "/" + borrow_limit +
                '}';
    }
}