package com.library.exception;

public class UserNotFoundException extends LibraryException 
{
    public UserNotFoundException(String userId) 
    {
        super("User not found with ID: "+userId);
    }
}