# Shopify Image Updater

This Python script allows you to automatically update product images in a Shopify CSV export. It requires your updated images to be hosted on a server or an HTTP server running locally.

## Dependencies

This script uses the following Python libraries:

- `os` (Standard Library)
- `pandas`
- `urllib` (Standard Library)
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
    - Ensure it's named 'products_export_1 (10).csv' or adjust the script to your filename.

4. **Run**:
    - Execute the script with:
      ```
      python shopify_image_updater.py
      ```

5. **Results**:
    - An 'updated_shopify_products.csv' file will be generated in the main directory, with updated 'Image Src' and 'Variant Image' URLs.
    - The console will provide feedback on the number of images replaced and variants updated.

**Important**: Before executing the script, ensure your images are accessible via the provided `new_url`. If using a local HTTP server, ensure it's running.
