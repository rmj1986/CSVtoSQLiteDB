# CSV to SQLite Importer

This Python script imports data from multiple CSV files into a SQLite database. It creates a table for each CSV file, using the filename (without the.csv extension) as the table name.

## Features

* Automatically detects and imports all CSV files in the directory.
* Creates tables with the same names as the CSV files.
* Handles different CSV formats (comma-separated, tab-separated, etc.).
* Uses parameterized queries to prevent SQL injection vulnerabilities.

## Requirements

* Python 3.6 or higher
* SQLite3

## Usage

1.  **Place the script (`import_csv.py`) in the same directory as your CSV files.**
2.  **Run the script from your terminal:** `python import_csv.py`

This will create a new SQLite database file named `my_database.db` (or use an existing one) and import the data from all CSV files in the directory into corresponding tables.

## Customization

* **Database name:** You can change the database name by modifying the `conn = sqlite3.connect('my_database.db')` line in the script.
* **Encoding:** If your CSV files use a different encoding than the default (`utf-8`), you can specify the encoding when opening the files:
    ```python
    with open(csv_file, 'r', encoding='latin-1') as file:  # Replace 'latin-1' with the correct encoding
        #... rest of the code
    ```
* **Error handling:** You can add error handling to skip or report errors during the import process.

## Example

If you have the following CSV files in your directory:

*   `customers.csv`
*   `orders.csv`
*   `products.csv`

The script will create three tables in the database: `customers`, `orders`, and `products`, and import the data from the corresponding CSV files.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
