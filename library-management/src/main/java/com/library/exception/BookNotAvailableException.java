package com.library.exception;

public class BookNotAvailableException extends LibraryException 
{
    public BookNotAvailableException(String title) 
    {
        super("No copies available for book: "+title);
    }
}