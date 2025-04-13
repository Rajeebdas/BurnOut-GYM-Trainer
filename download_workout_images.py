import requests
from PIL import Image
from io import BytesIO
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Dictionary of image URLs and their corresponding filenames
workout_images = {
    'strength-training.jpg': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1920',  # Weight training
    'cardio-training.jpg': 'https://images.unsplash.com/photo-1538805060514-97d9cc17730c?q=80&w=1920',    # Treadmill running
    'hiit-workout.jpg': 'https://images.unsplash.com/photo-1601422407692-ec4eeec1d9b3?q=80&w=1920',       # High intensity training
    'flexibility-training.jpg': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=1920', # Stretching
    'calisthenics.jpg': 'https://images.unsplash.com/photo-1599058945522-28d584b6f0ff?q=80&w=1920',       # Bodyweight exercise
    'pilates-class.jpg': 'https://images.unsplash.com/photo-1518310383802-640c2de311b2?q=80&w=1920',      # Pilates
    'functional-training.jpg': 'https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?q=80&w=1920', # Functional movements
    'crossfit-workout.jpg': 'https://images.unsplash.com/photo-1533681904393-9ab6eee7e408?q=80&w=1920',   # CrossFit
}

def download_and_optimize_image(url, filename):
    try:
        # Download image
        response = requests.get(url)
        response.raise_for_status()
        
        # Open and optimize image
        img = Image.open(BytesIO(response.content))
        
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Save optimized image
        output_path = os.path.join('images', filename)
        img.save(output_path, 'JPEG', quality=85, optimize=True)
        print(f"Successfully downloaded and optimized: {filename}")
        
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Download and optimize all images
for filename, url in workout_images.items():
    download_and_optimize_image(url, filename) 