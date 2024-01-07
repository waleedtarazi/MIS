#include <iostream>
#include <string>


const std::string validUsername = "admin";
const std::string validPassword = "admin123";


bool validateUser(const std::string& username, const std::string& password) {
    return (username == validUsername && password == validPassword);
}

int main() {
    std::string username, password;

    std::cout << "Library System Login\n";
    std::cout << "---------------------\n";

    
    std::cout << "Enter username: ";
    std::cin >> username;

    std::cout << "Enter password: ";
    std::cin >> password;

   
    if (validateUser(username, password)) {
        std::cout << "Login successful. Welcome, " << username << "!\n";

        

    }
    else {
        std::cout << "Login failed. Invalid username or password.\n";
    }

    return 0;
}