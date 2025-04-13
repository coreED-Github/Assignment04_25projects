import qrcode
import cv2
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# QR Code Generate Function
def generate_qr():
    data = entry.get()
    if data == "":
        messagebox.showerror("Error", "Please enter some text or URL to generate QR code.")
        return
    qr_img = qrcode.make(data)
    qr_img.save("generated_qr.png")
    img = Image.open("generated_qr.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    messagebox.showinfo("Success", "QR Code generated and saved as 'generated_qr.png'")


# QR Code Decode Function
def decode_qr():
    file_path = filedialog.askopenfilename(title="Select QR Code Image",
                                           filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if not file_path:
        return
    image = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image)
    if data:
        result_text.delete(1.0, END)
        result_text.insert(END, f"Decoded Data:\n{data}")
    else:
        messagebox.showerror("Error", "No QR code found in the selected image.")


# GUI Design
root = Tk()
root.title("QR Code Encoder / Decoder")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="white")

Label(root, text="QR Code Encoder/Decoder", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

Label(root, text="Enter text or URL:", bg="white").pack()
entry = Entry(root, width=40, font=("Helvetica", 12))
entry.pack(pady=5)

Button(root, text="Generate QR Code", command=generate_qr, bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(pady=10)

qr_label = Label(root, bg="white")
qr_label.pack(pady=10)

Button(root, text="Decode QR Code from Image", command=decode_qr, bg="#2196F3", fg="white", font=("Helvetica", 12)).pack(pady=10)

result_text = Text(root, height=5, width=40, font=("Helvetica", 12))
result_text.pack(pady=10)

root.mainloop()