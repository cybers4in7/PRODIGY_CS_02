from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    # Apply a basic mathematical operation (XOR) with the key
    encrypted_pixels = pixels ^ key

    # Swap pixel values
    encrypted_pixels = encrypted_pixels[::-1, ::-1, ::-1]
    
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    # Revert the swap pixel values
    decrypted_pixels = pixels[::-1, ::-1, ::-1]
    
    # Revert the mathematical operation (XOR) with the key
    decrypted_pixels = decrypted_pixels ^ key
    
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            break
        elif choice in ['e', 'd']:
            image_path = input("Enter the path to the image: ")
            output_path = input("Enter the output path for the processed image: ")
            key = int(input("Enter an encryption/decryption key (integer): "))
            if choice == 'e':
                encrypt_image(image_path, output_path, key)
            else:
                decrypt_image(image_path, output_path, key)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
