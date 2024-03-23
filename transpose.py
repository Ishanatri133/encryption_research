import numpy as np
from PIL import Image


def transpose_image(img):
    # Swap pixel rows
    transposed_img = img.copy()
    for i in range(0, img.shape[0], 2):
        if i + 1 < img.shape[0]:
            transposed_img[i], transposed_img[i + 1] = transposed_img[i + 1], transposed_img[i]

    # Swap pixel columns
    for i in range(img.shape[1]):
        for j in range(0, img.shape[0], 2):
            if j + 1 < img.shape[0]:
                transposed_img[j, i], transposed_img[j + 1, i] = transposed_img[j + 1, i], transposed_img[j, i]

    return transposed_img


def encrypt_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Resize the image to 256x256
    img = img.resize((256, 256))

    # Convert image to numpy array
    img_array = np.array(img)

    # Transpose the image pixel columns and rows
    transposed_img = transpose_image(img_array)

    # Generate random numbers for encryption
    random_numbers = np.random.randint(0, 255, (256, 256, 3))

    # XOR each pixel value with the random number for respective color channel
    encrypted_img = np.bitwise_xor(transposed_img, random_numbers)
    encrypted_img = encrypted_img.astype(np.uint8)

    # Save the encrypted image in the specified directory
    encrypted_image_path = "C:/DESKTOP/ISHAN FILES/encrypted_image.png"
    Image.fromarray(encrypted_img).save(encrypted_image_path)
    print("Image encrypted and saved as:", encrypted_image_path)

    # Return the random numbers along with the encrypted image
    return encrypted_img, random_numbers


def decrypt_image(encrypted_img, random_numbers):
    # XOR each pixel value with the same random number used during encryption
    decrypted_img = np.bitwise_xor(encrypted_img, random_numbers)
    decrypted_img = decrypted_img.astype(np.uint8)

    # Transpose back the decrypted image pixel columns and rows
    decrypted_img = transpose_image(decrypted_img)

    # Save the decrypted image in the specified directory
    decrypted_image_path = "C:/DESKTOP/ISHAN FILES/decrypted_image.png"
    Image.fromarray(decrypted_img).save(decrypted_image_path)
    print("Image decrypted and saved as:", decrypted_image_path)


# Example usage
image_path = "C:/DESKTOP/ISHAN FILES/WhatsApp Image 2024-03-18 at 23.03.16_3ea17d21.jpg"
encrypted_img, random_numbers = encrypt_image(image_path)
decrypt_image(encrypted_img, random_numbers)
