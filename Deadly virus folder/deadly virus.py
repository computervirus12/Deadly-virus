import tkinter as tk
import random

# Create root window
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")

# Fonts and icons
icons = ["⚠️", "❌", "❔"]
texts = ["REAL GLITCH DETECTED", "SYSTEM WARNING", "1T EFFECTS ACTIVE"]

# Canvas for drawing
canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

def show_warning_boxes():
    # First warning
    box1 = tk.Toplevel(root)
    box1.title("⚠️ Warning")
    tk.Label(box1, text="Something is happening...", font=("Consolas", 16)).pack(padx=20, pady=20)
    box1.geometry("300x100+100+100")

    # Second warning
    box2 = tk.Toplevel(root)
    box2.title("❌ Critical Error")
    tk.Label(box2, text="REAL GLITCH DETECTED", font=("Consolas", 16)).pack(padx=20, pady=20)
    box2.geometry("300x100+500+300")

    # Close after 3 seconds
    root.after(3000, lambda: [box1.destroy(), box2.destroy(), simulate_desktop()])

def simulate_desktop():
    canvas.delete("all")
    canvas.create_text(800, 400, text="Restoring Desktop...", fill="white", font=("Consolas", 24))
    root.after(2000, start_glitch_effects)

def start_glitch_effects():
    def draw_glitch():
        canvas.delete("all")
        for _ in range(30):
            x1 = random.randint(0, root.winfo_screenwidth())
            y1 = random.randint(0, root.winfo_screenheight())
            x2 = x1 + random.randint(20, 200)
            y2 = y1 + random.randint(20, 200)
            color = random.choice(["red", "green", "blue", "yellow", "magenta", "cyan"])
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        
        # Draw glitch text
        for _ in range(5):
            text = random.choice(texts)
            icon = random.choice(icons)
            canvas.create_text(random.randint(100, 1500), random.randint(100, 800),
                               text=f"{icon} {text}", fill=random.choice(["white", "gray", "lime"]),
                               font=("Consolas", 20))

        root.after(100, draw_glitch)

    draw_glitch()

# Start sequence
show_warning_boxes()

# Exit on ESC
def exit_on_esc(event):
    root.destroy()

root.bind("<Escape>", exit_on_esc)
root.mainloop()