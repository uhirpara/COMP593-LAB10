import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ctypes import *
from poke_api import get_pokemon_list
from set_desk import set_desk

# give number how many pokemon list is required
num = 5 #enter a num value
dict = get_pokemon_list(num)
print(dict)

# Define global variables
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 550
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_ICO_FILE = "pokeaap.ico"
POKEMON_IMAGES_FOLDER = "images"
POKEMON_IMAGE_FILE = "poke.png"
POKEMON_NAMES = dict

# Define GUI class
class PokemonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Viewer")
        self.root.iconbitmap(POKEMON_ICO_FILE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.create_widgets()

    def create_widgets(self):
        # Create Frame widget
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Create Label widget for displaying Pokemon image
        self.pokemon_image = tk.Label(self.root)
        self.pokemon_image.pack(pady=10)

        # Create Combobox widget
        self.combobox_label = tk.Label(self.root, text="Select a Pokemon:")
        self.combobox_label.pack(pady=5)
        self.combobox = ttk.Combobox(self.root, values=POKEMON_NAMES)
        self.combobox.pack(pady=5)
        self.combobox.bind("<<ComboboxSelected>>", self.display_pokemon_image)

        # Create Button widget
        self.button = tk.Button(self.root, text="Set as Desktop Image", command=self.button_clicked)
        self.button.pack(pady=5)    
         
    def display_pokemon_image(self, event=None):
        # Retrieve and display selected Pokemon image or default image
        pokemon_name = self.combobox.get()
        global pokemon_image_path
        if pokemon_name:
            pokemon_image_path = f"{POKEMON_IMAGES_FOLDER}\{pokemon_name}.png"
        else:
            pokemon_image_path = f"{POKEMON_IMAGES_FOLDER}\pokeaap.png"
        image = Image.open(pokemon_image_path)
        image = image.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.pokemon_image.config(image=photo)
        self.pokemon_image.image = photo
        
    def button_clicked(self):
        set_desk(pokemon_image_path)
      
# Define external DLL function
user32 = windll.user32
user32.MessageBoxW(None, "Welcome to the Pokemon GUI!", "Pokemon GUI", 0)

# Create instance of PokemonGUI class and run main loop
root = tk.Tk()
app = PokemonGUI(root)
root.mainloop()