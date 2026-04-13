package com.library.model;
public class Book 
{
    private String isbn;
    private String title;
    private String author;
    private String genre;
    private int totalCopies;
    private int availableCopies;
    public Book(String isbn,String title,String author,String genre,int totalCopies) 
    {
        this.isbn=isbn;
        this.title=title;
        this.author=author;
        this.genre=genre;
        this.totalCopies=totalCopies;
        this.availableCopies=totalCopies;
    }
    public String getIsbn() 
    {
        return isbn;
    }
    public String getTitle() 
    {
        return title;
    }
    public String getAuthor() 
    {
        return author;
    }
    public String getGenre() 
    {
        return genre;
    }
    public int getTotalCopies() 
    {
        return totalCopies;
    }
    public int getAvailableCopies() 
    {
        return availableCopies;
    }
    public boolean isCopyAvailable() 
    {
        return availableCopies>0;
    }
    public void decrementCopy() 
    {
        if(availableCopies<=0) 
        {
            throw new IllegalStateException("No copies available to borrow");
        }
        availableCopies--;
    }
    public void incrementCopy() 
    {
        if(availableCopies>=totalCopies) 
        {
            throw new IllegalStateException("All copies are already returned");
        }
        availableCopies++;
    }
    @Override
    public String toString() 
    {
        return "Book{" +
                "isbn='" + isbn + '\'' +
                ", title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", genre='" + genre + '\'' +
                ", availableCopies=" + availableCopies +
                "/" + totalCopies +
                '}';
    }
}