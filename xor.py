import numpy as np
from PIL import Image
import random

def encrypt_image(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Resize the image to 256x256
    img = img.resize((256, 256))
    
    # Split the image into its RGB components
    r, g, b = img.split()
    
    # Convert RGB components to numpy arrays for easier manipulation and resize to 256x256
    r_array = np.array(r.resize((256, 256)))
    g_array = np.array(g.resize((256, 256)))
    b_array = np.array(b.resize((256, 256)))
    
    # Generate a random number between 0 to 255 for each color channel and resize to 256x256
    random_number_r = np.random.randint(0, 255, (256, 256))
    random_number_g = np.random.randint(0, 255, (256, 256))
    random_number_b = np.random.randint(0, 255, (256, 256))
    
    # XOR each pixel value with the random number for respective color channel
    encrypted_r = np.bitwise_xor(r_array, random_number_r).astype(np.uint8)
    encrypted_g = np.bitwise_xor(g_array, random_number_g).astype(np.uint8)
    encrypted_b = np.bitwise_xor(b_array, random_number_b).astype(np.uint8)
    
    # Create encrypted RGB images
    encrypted_r_img = Image.fromarray(encrypted_r)
    encrypted_g_img = Image.fromarray(encrypted_g)
    encrypted_b_img = Image.fromarray(encrypted_b)
    
    # Merge the encrypted RGB components into a single image
    encrypted_img = Image.merge('RGB', (encrypted_r_img, encrypted_g_img, encrypted_b_img))
    
    # Save the encrypted image in the specified directory
    save_path = "C:/DESKTOP/ISHAN FILES/encrypted_image.png"
    encrypted_img.save(save_path)
    print("Image encrypted and saved as:", save_path)
    
    # Return the random numbers along with the encrypted image
    return encrypted_img, random_number_r, random_number_g, random_number_b

def decrypt_image(encrypted_image_path, random_number_r, random_number_g, random_number_b):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Resize the image to 256x256
    encrypted_img = encrypted_img.resize((256, 256))
    
    # Split the image into its RGB components
    r, g, b = encrypted_img.split()
    
    # Convert RGB components to numpy arrays for easier manipulation and resize to 256x256
    r_array = np.array(r.resize((256, 256)))
    g_array = np.array(g.resize((256, 256)))
    b_array = np.array(b.resize((256, 256)))
    
    # XOR each pixel value with the same random number used during encryption for respective color channel
    decrypted_r = np.bitwise_xor(r_array, random_number_r).astype(np.uint8)
    decrypted_g = np.bitwise_xor(g_array, random_number_g).astype(np.uint8)
    decrypted_b = np.bitwise_xor(b_array, random_number_b).astype(np.uint8)
    
    # Create decrypted RGB images
    decrypted_r_img = Image.fromarray(decrypted_r)
    decrypted_g_img = Image.fromarray(decrypted_g)
    decrypted_b_img = Image.fromarray(decrypted_b)
    
    # Merge the decrypted RGB components into a single image
    decrypted_img = Image.merge('RGB', (decrypted_r_img, decrypted_g_img, decrypted_b_img))
    
    # Save the decrypted image
    save_path = "C:/DESKTOP/ISHAN FILES/decrypted_image.png"
    decrypted_img.save(save_path)
    print("Image decrypted and saved as:", save_path)
    
    # Show the decrypted image
    decrypted_img.show()
# Example usage:
image_path = "C:\DESKTOP\ISHAN FILES\download.jpeg"
encrypted_image, random_number_r, random_number_g, random_number_b = encrypt_image(image_path)
decrypt_image("C:/DESKTOP/ISHAN FILES/encrypted_image.png", random_number_r, random_number_g, random_number_b)
