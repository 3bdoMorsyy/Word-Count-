import word_count_task as wc

# import machine_translation_rec as ml
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


class DocumentAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Count Program")

        # Styling
        self.root.configure(bg="#fff")  # Background color
        self.root.geometry("600x600")  # Set initial window size

        # Text input
        self.input_label = tk.Label(
            root,
            text="Text",
            bg="#FFFFFF",
            fg="#333333",
            font=("Arial", 12, "bold"),
        )
        self.input_label.pack(pady=(20, 5))
        self.input_text = scrolledtext.ScrolledText(
            root,
            width=60,
            height=10,
            bg="#F0F0F0",
            fg="#333333",
            font=("Arial", 10),
        )
        self.input_text.pack(pady=(0, 10))

        # Buttons
        self.map_buttom = tk.Button(
            root,
            text="Map",
            command=self.Map,
            bg="#999999",
            fg="#000",
            font=("Arial", 10, "bold"),
        )
        self.map_buttom.pack()
        self.Shuffle_buttom = tk.Button(
            root,
            text="Shuffle",
            command=self.Shuffle,
            bg="#999999",
            fg="#000",
            font=("Arial", 10, "bold"),
        )
        self.Shuffle_buttom.pack()
        self.word_count_buttom = tk.Button(
            root,
            text="MapReduce",
            command=self.MAP_REDUCE,
            bg="#999999",
            fg="#000",
            font=("Arial", 10, "bold"),
        )
        self.word_count_buttom.pack()

        self.reset_button = tk.Button(
            root,
            text="reset",
            command=self.reset,
            bg="#000",
            fg="#FFFFFF",
            font=("Arial", 10, "bold"),
        )
        self.reset_button.pack()

        # Output
        self.output_label = tk.Label(
            root, text="Output:", bg="#FFFFFF", fg="#333333", font=("Arial", 12, "bold")
        )
        self.output_label.pack(pady=(20, 5))
        self.output_text = scrolledtext.ScrolledText(
            root, width=60, height=10, bg="#F0F0F0", fg="#000"
        )
        self.output_text.pack(pady=(0, 10))

    def MAP_REDUCE(self):
        text = self.input_text.get("1.0", "end-1c")
        if text.strip():
            text = text.replace("\n", "").replace("'", "").replace('"', "")
            output_text = wc.MapReduce(text)
            self.output_text.delete("1.0", tk.END)  # Clear previous output
            for o in output_text:
                self.output_text.insert(tk.END, f"{o}\n")
        else:
            messagebox.showwarning("Error", "Input is empty!")

    def Map(self):
        text = self.input_text.get("1.0", "end-1c")
        if text.strip():
            text = text.replace("\n", "").replace("'", "").replace('"', "")
            output_text = wc.Map(text)
            self.output_text.delete("1.0", tk.END)  # Clear previous output
            for o in output_text:
                self.output_text.insert(tk.END, f"{o}\n")
        else:
            messagebox.showwarning("Error", "Input is empty!")

    def Shuffle(self):
        text = self.input_text.get("1.0", "end-1c")
        if text.strip():
            text = text.replace("\n", "").replace("'", "").replace('"', "")
            output_text = wc.Shuffle(text)
            self.output_text.delete("1.0", tk.END)  # Clear previous output
            for o in output_text:
                self.output_text.insert(tk.END, f"{o}\n")
        else:
            messagebox.showwarning("Error", "Input is empty!")

    def reset(self):
        self.output_text.delete("1.0", tk.END)  # Clear previous output


root = tk.Tk()
app = DocumentAnalyzerApp(root)
root.mainloop()
