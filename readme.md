# Shopify Image Updater

This Python script allows you to automatically update product images in a Shopify CSV export. It requires your updated images to be hosted on a server or an HTTP server running locally.

You can download all the product images from your store using [shopify-photo-download](https://github.com/ComicDansMS/shopify-photo-download). While processing/editing, ensure to keep the original file names.

You can then use this script to update the export/import CSV with the URL where the images are available. This can be done with a reverse proxy (such as [ngrok](https://ngrok.com)), pointing to a local HTTP server running on your machine. The `new_url` would be your ngrok URL.

When the script runs, it will proceed to grab the updated images from the specified location.

## Warning

During the upload process, if Shopify determines there is an updated image on the product/variant, it will remove the existing image and try to fetch the new one. If the new image is not available at the URL, it will move onto the next image without reloading the existing image. It's an easy way to wipe a lot of product images from the store. It's not a bad idea to test this on a test product first to ensure the reverse proxy and HTTP server is working as expected.

## Dependencies

This script uses the following Python libraries:

- `pandas`
- `tqdm`

You can install the necessary libraries using pip:

`pip install pandas tqdm`

## Usage

1. **Setup**:
    - Clone or download the repository.
    - Place your images in your desired folder.

2. **Configuration**:
    - Modify the `image_folder_path` and `new_url` variables in the script to match your directory structure and hosting setup.
      ```python
      image_folder_path = 'path_to_your_images_folder'  # Example: '/Users/user_name/Projects/images_folder'
      new_url = "your_server_url"  # Make sure to end with a "/"
      ```

3. **CSV Preparation**:
    - Place your Shopify products export CSV in the main directory. 
    - Update `csv_file` to the name of your csv.

4. **Run**:
    - Execute the script with:
      ```
      python shopify_image_updater.py
      ```

5. **Results**:
    - An 'updated_products_export.csv' file will be generated in the main directory, with updated 'Image Src' and 'Variant Image' URLs.
