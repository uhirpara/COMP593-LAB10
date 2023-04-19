import os
import subprocess

# Make a GET request to the Pokemon API to get the list of Pokemon
def set_desk(pokemon_image_path):

        # Replace this with the actual path of the image file you want to set as the background
        # Execute the command to set the image as the desktop background
        image_path = f"{os.getcwd()}\\"+pokemon_image_path
        print(image_path)
        subprocess.run('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "{}" /f'.format(image_path), shell=True)

        # Refresh the desktop to apply the changes
        subprocess.run('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters ,1 ,True', shell=True)

        print("Desktop background set successfully")
