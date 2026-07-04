import random 
import emoji

emojis = ["smile", "thumbs_up", "heart", "fire", "rocket", "star"]
chosen = random.choice(emojis)
print(emoji.emojize(f":{chosen}:"))