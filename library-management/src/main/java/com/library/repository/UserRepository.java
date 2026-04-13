package com.library.repository;

import com.library.model.User;
import java.util.List;
import java.util.Optional;
public interface UserRepository 
{
    void save(User user);
    Optional<User> findById(String userId);
    Optional<User> findByEmail(String email);
    List<User> findAll();
    void delete(String userId);
    boolean existsById(String userId);
}
