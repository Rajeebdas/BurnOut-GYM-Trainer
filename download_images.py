import os
import requests
from PIL import Image
from io import BytesIO

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Dictionary of image URLs and their corresponding filenames
image_urls = {
    'gym-background.jpg': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1920',
    'gym-pattern.jpg': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=1920',
    'nutrition-guidance.jpg': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=1920',
    'progress-tracking.jpg': 'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?q=80&w=1920',
    'expert-trainer.jpg': 'https://images.unsplash.com/photo-1571388208497-71bedc66e932?q=80&w=1920',
    'trainer-profile.jpg': 'https://images.unsplash.com/photo-1571388208497-71bedc66e932?q=80&w=1920',
    'about-gym.jpg': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1920',
    'contact-gym.jpg': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=1920',
    'gym-equipment-1.jpg': 'https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?q=80&w=1920',
    'gym-equipment-2.jpg': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=1920',
    'gym-equipment-3.jpg': 'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?q=80&w=1920',
    'gym-equipment-4.jpg': 'https://images.unsplash.com/photo-1571388208497-71bedc66e932?q=80&w=1920',
    'gym-equipment-5.jpg': 'https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?q=80&w=1920',
    'gym-equipment-6.jpg': 'https://images.unsplash.com/photo-1545205597-3d9d02c29597?q=80&w=1920'
}

def download_and_optimize_image(url, filename):
    try:
        # Download image
        response = requests.get(url)
        response.raise_for_status()
        
        # Open image with PIL
        img = Image.open(BytesIO(response.content))
        
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Save optimized image
        img.save(f'images/{filename}', 'JPEG', quality=85, optimize=True)
        print(f'Successfully downloaded and optimized {filename}')
        
    except Exception as e:
        print(f'Error downloading {filename}: {str(e)}')

# Download and optimize all images
for filename, url in image_urls.items():
    download_and_optimize_image(url, filename)

print('All images have been downloaded and optimized!') 