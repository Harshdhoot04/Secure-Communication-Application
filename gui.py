# gui.py
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
from encryption import CryptoHandler

class SecureChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Communication App")
        
        # Initialize encryption handler
        self.crypto_handler = CryptoHandler()
        
        # Authenticate user
        self.authenticate()

    def authenticate(self):
        password = simpledialog.askstring("Authentication", "Enter password:")
        if password == "123":  # Replace with actual password check
            self.create_widgets()
        else:
            messagebox.showerror("Error", "Incorrect password.")
            self.root.quit()
    
    def create_widgets(self):
        # Create a header
        self.header = tk.Label(self.root, text="Secure Communication App", font=("Arial", 16), bg="#4CAF50", fg="white")
        self.header.pack(fill=tk.X)

        # Create a text area for message display
        self.message_area = scrolledtext.ScrolledText(self.root, width=60, height=20, wrap=tk.WORD, font=("Arial", 12), bg="#f0f0f0")
        self.message_area.pack(padx=10, pady=10)

        # Create a text entry for message input
        self.message_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.message_entry.pack(padx=10, pady=5)

        # Create a profile entry
        self.profile_name_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.profile_name_entry.pack(padx=10, pady=5)
        self.profile_name_entry.insert(0, "Enter your name")

        # Create a send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.send_button.pack(pady=5)

        # Create a receive button
        self.receive_button = tk.Button(self.root, text="Receive", command=self.receive_message_prompt, font=("Arial", 12), bg="#008CBA", fg="white")
        self.receive_button.pack(pady=5)

    def send_message(self):
        profile_name = self.profile_name_entry.get().strip()
        if not profile_name:
            profile_name = "Anonymous"
        plaintext = self.message_entry.get().strip()
        if not plaintext:
            self.message_area.insert(tk.END, "Error: Message cannot be empty.\n")
            return
        encrypted_message = self.crypto_handler.encrypt(plaintext)
        message_hash = self.get_hash(plaintext)
        self.message_area.insert(tk.END, f"{profile_name}: Encrypted: {encrypted_message}\nHash: {message_hash}\n")
        self.message_entry.delete(0, tk.END)

    def receive_message_prompt(self):
        encrypted_message = simpledialog.askstring("Receive Message", "Enter encrypted message:")
        if encrypted_message:
            self.receive_message(encrypted_message)

    def receive_message(self, encrypted_message):
        decrypted_message = self.crypto_handler.decrypt(encrypted_message)
        self.message_area.insert(tk.END, f"Decrypted: {decrypted_message}\n")

    def get_hash(self, message):
        import hashlib
        return hashlib.sha256(message.encode()).hexdigest()

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureChatApp(root)
    root.mainloop()
