# Mile to Km Converter

## Description
This is a simple graphical user interface (GUI) application built using Python's Tkinter library. The application converts a value entered in miles to kilometers and displays the result. 

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## Installation
No special installation is required other than having Python installed. Tkinter comes bundled with Python on most platforms. If Tkinter is not installed, you can install it using your package manager or by running:

```sh
# For Debian-based systems
sudo apt-get install python3-tk

# For Red Hat-based systems
sudo yum install python3-tkinter

# For Windows, if not included, you can use the installer from python.org which includes Tkinter
```

## Usage
1. Save the provided Python code in a file, for example, `mile_to_km_converter.py`.
2. Run the script using Python:
   ```sh
   converter.py
   ```
3. A window will appear with the following elements:
   - An entry box to input miles.
   - A label displaying "Miles".
   - A label displaying the converted kilometers value.
   - A label displaying "Km".
   - A "Calculate" button to perform the conversion.

4. Enter the number of miles you want to convert in the entry box and click the "Calculate" button. The result in kilometers will be displayed.

## Code Explanation
Here's a brief explanation of the main parts of the code:

- **Importing Tkinter**:
  ```python
  from tkinter import *
  ```
  Import all the necessary classes and functions from the Tkinter library.

- **Creating the main window**:
  ```python
  window = Tk()
  window.title("Mile to Km Converter")
  window.config(padx=20, pady=20)
  ```
  Create the main window and set its title and padding.

- **Defining the conversion function**:
  ```python
  def convert():
      result = int(mile_entry.get()) * 1.60934
      num_of_km["text"] = int(result)
  ```
  Define a function to convert miles to kilometers and update the result label.

- **Creating and placing widgets**:
  ```python
  mile_entry = Entry()
  mile_entry["width"] = 10
  mile_entry.grid(row=0, column=1)

  mile_label = Label(text="Miles")
  mile_label.grid(row=0, column=2)

  num_of_km = Label(text="0")
  num_of_km.grid(row=1, column=1)

  km = Label(text="Km")
  km.grid(row=1, column=2)

  button = Button(text="Calculate", command=convert)
  button.grid(row=2, column=1)
  ```
  Create and place the entry, labels, and button in the grid layout of the window.

- **Running the main loop**:
  ```python
  window.mainloop()
  ```
  Start the Tkinter event loop to run the application.

## License
This project is open-source and available under the MIT License.