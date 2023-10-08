from gtts import gTTS
import os

# Lyrics of the song you want to sing
lyrics = '''Once upon a time in a small, picturesque village, there lived a curious young girl named Lily. She had a deep fascination for the stars and spent her nights stargazing from her bedroom window. One clear night, she noticed a shooting star streak across the sky and made a heartfelt wish.

The next morning, to her astonishment, she awoke to find a mysterious book at her doorstep. It was bound in an ancient leather cover with shimmering constellations etched on it. As she opened it, the book emitted a soft, radiant light, revealing its magical secrets.

The book contained spells that could manipulate the very elements of nature, and with each incantation, Lily's powers grew stronger. She used her newfound abilities to bring prosperity and happiness to her village, earning the gratitude of all its inhabitants.

In the end, Lily learned that true magic lay not only in spells but in the goodness of one's heart. She continued to protect her village, using her powers to spread love and kindness throughout the land, ensuring that her story would be told for generations to come.'''

# Create a gTTS object
song = gTTS(text=lyrics, lang='en')

# Save the singing to a file
song.save("singing.mp3")

# Play the singing
os.system("start singing.mp3")  # This is for Windows, use "open singing.mp3" on macOS or Linux
