package fr.steve.spring.service;

import fr.steve.spring.model.User;
import fr.steve.spring.model.repository.UserRepository;
import fr.steve.spring.model.response.UserResponse;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<UserResponse> allUsers() {
        List<UserResponse> users = new ArrayList<>();

        userRepository.findAll().forEach(user -> users.add(genereUserResponse(user)));

        return users;
    }

    public UserResponse genereUserResponse(User user) {
        UserResponse userResponse = new UserResponse();
        userResponse.setEmail(user.getEmail());
        userResponse.setUsername(user.getUsername());
        userResponse.setFullName(user.getFullName());
        userResponse.setEnabled(user.isEnabled());
        userResponse.setCreatedAt(user.getCreatedAt());
        userResponse.setUpdatedAt(user.getUpdatedAt());
        userResponse.setAccountNonExpired(user.isAccountNonExpired());
        userResponse.setAccountNonLocked(user.isAccountNonLocked());
        userResponse.setCredentialsNonExpired(user.isCredentialsNonExpired());
        userResponse.setRoles(user.getAuthorities());
        return userResponse;
    }
}
