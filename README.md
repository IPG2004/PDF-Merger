# PDF Merger

PDF Merger is a graphical user interface (GUI) application that allows users to merge multiple PDF files into a single document.

## Features

- Add multiple PDF files to merge.
- Select the destination folder and set a custom filename for the merged PDF.
- Clear the list of selected files.
- Dynamic UI scaling based on screen resolution.
- Dark mode support with a custom color theme.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/IPG2004/PDF-Merger.git
    cd PDF-Merger
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. (Optional) Install the package using `setup.py`:
    ```sh
    pip install .
    ```

## Usage

1. Run the application:
    ```sh
    python3 src/app.py
    ```

2. Click the "Search" button to add PDF files to the list.

3. Select the destination folder by clicking the "Destination" button.

4. Set a custom filename in the provided entry field.

5. Click the "Merge" button to merge the selected PDF files.

## Project Structure

```plaintext
PDF-Merger/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src/
    ├── __init__.py
│   └── app.py
└── tests/
    ├── __init__.py
    └── test_app.py
```
- `src/`: Contains the main application code.
    - `app.py`: Main GUI application.
- `tests/`: Contains test files.
    - `test_app.py`: Test cases for the application.

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) for more details.

## Credits

Made by [@IPG2004](https://github.com/IPG2004)