# Secure Communication Application

## Description

The Secure Communication Application is a Python-based tool for encrypted messaging. It allows users to send and receive encrypted messages using Fernet encryption. This application ensures that messages are secure and can only be decrypted by the intended recipient.

## Features

- **Encryption/Decryption**: Encrypt and decrypt messages using Fernet encryption.
- **Authentication**: Simple password-based access control.
- **Hashing**: Generate SHA-256 hashes of messages to verify integrity.
- **User Interface**: Tkinter-based GUI for user-friendly interaction.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Harshdhoot04/Secure-Communication-Application.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Secure-Communication-Application
    ```

3. **Install the required Python libraries**:

    ```bash
    pip install cryptography
    ```

## Usage

1. **Run the application**:

    ```bash
    python gui.py
    ```

2. **Authenticate**: Enter the password when prompted to access the application.

3. **Sending a Message**:
    - Enter your name in the profile entry (optional).
    - Type your message in the message entry.
    - Click "Send."

4. **Receiving a Message**:
    - Click "Receive" and enter the encrypted message in the prompt.

## Configuration

- The encryption key is generated automatically. If you want to set a specific key, modify the `CryptoHandler` class in `encryption.py`.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Ensure that any contributions adhere to the project's coding standards and guidelines.

## Acknowledgements

- **Cryptography Library**: Used for encryption and decryption.
- **Tkinter**: Used for creating the GUI.
