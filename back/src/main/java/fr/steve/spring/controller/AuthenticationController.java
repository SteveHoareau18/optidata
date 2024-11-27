package fr.steve.spring.controller;

import fr.steve.spring.model.User;
import fr.steve.spring.model.dto.LoginUserDto;
import fr.steve.spring.model.dto.RegisterUserDto;
import fr.steve.spring.model.response.LoginResponse;
import fr.steve.spring.model.response.UserResponse;
import fr.steve.spring.service.AuthenticationService;
import fr.steve.spring.service.JwtService;
import fr.steve.spring.service.UserService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/auth")
@RestController
public class AuthenticationController {

    private final JwtService jwtService;
    private final AuthenticationService authenticationService;
    private final UserService userService;

    public AuthenticationController(JwtService jwtService, AuthenticationService authenticationService,
                                    UserService userService) {
        this.jwtService = jwtService;
        this.authenticationService = authenticationService;
        this.userService = userService;
    }

    @PostMapping("/signup")
    public ResponseEntity<UserResponse> register(@RequestBody RegisterUserDto registerUserDto) {
        User registeredUser = authenticationService.signup(registerUserDto);

        return ResponseEntity.ok(userService.genereUserResponse(registeredUser));
    }

    @PostMapping("/login")
    public ResponseEntity<LoginResponse> authenticate(@RequestBody LoginUserDto loginUserDto) {
        User authenticatedUser = authenticationService.authenticate(loginUserDto);

        String jwtToken = jwtService.generateToken(authenticatedUser);

        LoginResponse loginResponse = new LoginResponse();
        loginResponse.setToken(jwtToken);
        loginResponse.setExpiresIn(jwtService.getExpirationTime());

        return ResponseEntity.ok(loginResponse);
    }
}