import os
from PIL import Image
import requests
from io import BytesIO

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Save the black and white profile photo
profile_photo = Image.open('hitesh_profile.jpg')  # The provided B&W photo
profile_photo = profile_photo.convert('L')  # Convert to black and white if not already
profile_photo.save('images/hitesh_profile.png', 'PNG', quality=95)

print('Profile photo has been saved successfully!') 