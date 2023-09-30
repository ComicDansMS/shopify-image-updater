import os
import pandas as pd
from urllib.parse import urlparse
from tqdm import tqdm

# Define the path of the images folder (no trailing slash)
image_folder_path = '/path/to/images'

# URL of where the images are hosted (must have a trailing slash)
new_url = "http://123.45.678.9/"

# CSV filename
csv_file = "products_export.csv"

# Load the CSV file
df = pd.read_csv(csv_file)

# Get the list of all image files in the folder
image_files = os.listdir(image_folder_path)

# Initialize the progress bar
pbar = tqdm(total=len(image_files))

replaced_count = 0
updated_variants = 0

# Iterate through each image file
for image_file in image_files:
    # Update the progress bar
    pbar.update(1)

    # Get the filename without extension
    filename_without_extension = os.path.splitext(image_file)[0]

    # Extract the filename from the 'Image Src' and 'Variant Image' columns
    df['filename_from_src'] = df['Image Src'].apply(lambda x: os.path.splitext(os.path.basename(urlparse(x).path))[0] if pd.notnull(x) else '')
    df['filename_from_variant'] = df['Variant Image'].apply(lambda x: os.path.splitext(os.path.basename(urlparse(x).path))[0] if pd.notnull(x) else '')

    # Check if the filename exists in the new 'filename' columns
    image_exists_in_src = (df['filename_from_src'] == filename_without_extension).any()
    image_exists_in_variant = (df['filename_from_variant'] == filename_without_extension).any()

    # If the image exists in the CSV, replace the URL and extension
    if image_exists_in_src:
        df.loc[df['filename_from_src'] == filename_without_extension, 'Image Src'] = new_url + image_file
        replaced_count += 1
        print(f"Replaced src image: {image_file}")
    if image_exists_in_variant:
        df.loc[df['filename_from_variant'] == filename_without_extension, 'Variant Image'] = new_url + image_file
        updated_variants += 1
        print(f"Replaced variant image: {image_file}")

# Close the progress bar
pbar.close()

# Drop the 'filename' columns
df.drop(columns=['filename_from_src', 'filename_from_variant'], inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_shopify_products.csv', index=False)

print(f"Replaced {replaced_count} images and updated {updated_variants} variants")