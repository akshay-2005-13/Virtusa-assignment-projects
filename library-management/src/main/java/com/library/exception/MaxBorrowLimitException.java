package com.library.exception;

public class MaxBorrowLimitException extends LibraryException 
{
    public MaxBorrowLimitException(String userName,int limit) 
    {
        super("User "+userName+" has reached the maximum borrow limit of "+limit+" books");
    }
}