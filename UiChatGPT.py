import tkinter as tk
from tkinter import messagebox

# ---------- Encryption / Decryption Functions ----------

def lavKryptedList(string): 
    return [ord(i) for i in string]

def kryptering(kryptKey, tekst): 
    kryptedTekstString = "" 
    for i in range(1, len(tekst)+1): 
        x = i % len(kryptKey) 
        kryptedTekst = kryptKey[x-1] + tekst[i-1]
        kryptedTekstString += chr(kryptedTekst) 
    return kryptedTekstString 

def deKryption(kryptKeyAscii, kryptedTekst): 
    deKryptedTekstString = "" 
    for i in range(1, len(kryptedTekst)+1): 
        x = i % len(kryptKeyAscii) 
        deKryptedTekst = ord(kryptedTekst[i-1]) - kryptKeyAscii[x-1] 
        deKryptedTekstString += chr(deKryptedTekst) 
    return deKryptedTekstString 

# ---------- Tkinter UI ----------

def do_encrypt():
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get().strip()
    if not text or not key:
        messagebox.showwarning("Fejl", "Indtast både tekst og nøgle.")
        return
    
    tekstList = lavKryptedList(text) 
    kryptKey = lavKryptedList(key) 
    encrypted = kryptering(kryptKey, tekstList) 
    output.delete("1.0", tk.END)
    output.insert(tk.END, encrypted)

def do_decrypt():
    encrypted_text = text_input.get("1.0", tk.END).strip()
    key = key_input.get().strip()
    if not encrypted_text or not key:
        messagebox.showwarning("Fejl", "Indtast både krypteret tekst og nøgle.")
        return
    
    opLåsNøgle = lavKryptedList(key) 
    decrypted = deKryption(opLåsNøgle, encrypted_text) 
    output.delete("1.0", tk.END)
    output.insert(tk.END, decrypted)

# Main window
root = tk.Tk()
root.title("Kryptering / Dekryptering")

# Input for text
tk.Label(root, text="Tekst:").pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

# Input for key
tk.Label(root, text="Nøgle:").pack()
key_input = tk.Entry(root, width=5, show="*")
key_input.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

encrypt_btn = tk.Button(button_frame, text="Krypter", command=do_encrypt)
encrypt_btn.pack(side=tk.LEFT, padx=5)

decrypt_btn = tk.Button(button_frame, text="Dekrypter", command=do_decrypt)
decrypt_btn.pack(side=tk.LEFT, padx=5)

# Output
tk.Label(root, text="Resultat:").pack()
output = tk.Text(root, height=5, width=50)
output.pack()

root.mainloop()
