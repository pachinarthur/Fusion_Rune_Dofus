import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Tableau de Runes - Mode Sombre")

    # Configuration de la couleur de fond principale
    bg_color = "#2b2b2b"
    fg_color = "#ffffff"
    entry_bg = "#3c3f41"
    entry_fg = "#ffffff"
    highlight_color = "#5c5c5c"

    root.configure(bg=bg_color)

    # Style sombre pour les widgets ttk
    style = ttk.Style()
    style.theme_use("default")

    style.configure("TLabel", background=bg_color, foreground=fg_color, font=("Arial", 10))
    style.configure("TButton", background=highlight_color, foreground=fg_color)
    style.map("TButton", background=[("active", "#444444")])

    # Titres colonnes et lignes
    col_titles = ["1", "10", "100", "1000"]
    row_titles = ["Runes", "Runes Pa", "Runes Ra"]

    entries_input = []
    entries_output = []

    # --- Premier tableau (avec titres) ---
    for j, title in enumerate(col_titles):
        label = ttk.Label(root, text=title)
        label.grid(row=0, column=j+1, padx=5, pady=5)

    for i, row_title in enumerate(row_titles):
        label = ttk.Label(root, text=row_title)
        label.grid(row=i+1, column=0, padx=5, pady=5)

        row_entries = []
        for j in range(len(col_titles)):
            entry = tk.Entry(root, width=20, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg,
                             relief=tk.FLAT)
            entry.grid(row=i+1, column=j+1, padx=5, pady=5)
            row_entries.append(entry)
        entries_input.append(row_entries)

    # --- Bouton "Calculer" ---
    def calculer():
        for i in range(len(row_titles)):
            for j in range(len(col_titles)):
                value = entries_input[i][j].get()
                entries_output[i][j].config(state='normal')
                entries_output[i][j].delete(0, tk.END)
                entries_output[i][j].insert(0, value)
                entries_output[i][j].config(state='readonly')

    calculate_button = ttk.Button(root, text="Calculer", command=calculer)
    calculate_button.grid(row=len(row_titles)+1, column=0, columnspan=len(col_titles)+1, pady=15)

    # --- Deuxième tableau (sans titres) ---
    offset = len(row_titles) + 2

    for i in range(len(row_titles)):
        row_entries = []
        for j in range(len(col_titles)):
            entry = tk.Entry(root, width=20, bg=entry_bg, fg=entry_fg, relief=tk.FLAT, state='readonly',
                             readonlybackground=entry_bg, insertbackground=entry_fg)
            entry.grid(row=offset + i, column=j+1, padx=5, pady=5)
            row_entries.append(entry)
        entries_output.append(row_entries)

    root.mainloop()

if __name__ == "__main__":
    main()
