Final Project Website Repository: https://github.com/Graph-Theory-Coding-Project/Final-Project-Website




# ✈️ Fastravel ✈️

Guys fill this stuff in lmaoaoaooa

## Group Members
| Name                              | NRP         | Contribution          |
|-----------------------------------|-------------|-----------------------|
| Fadhil Revinno Hairiman           | 5025231002  | Website Creation & Frontend Development  |
| R. Rafif Aqil Aabid Hermawan      | 5025231069  | Project Planning, Quality Assurance, & Report Creation |
| Rogelio Kenny Arisandi            | 5025231074  | Algorithm Creation & Backend Development |
| Matteo Dennequin                  | 5999241043  | Project Planning, Quality Assurance, & Report Creation |

# Background


# Methodology


# Implementation


---

## Tech Stack
- **Backend**: Python (Flask framework)
- **Frontend**: HTML

---

## Required Dependencies
Make sure to install the following dependencies for this project to work:
- Flask
- Any other necessary Python libraries

Install the dependencies using:
```
pip install -r requirements.txt
```

![image](https://github.com/user-attachments/assets/ec9e4b89-c799-4895-9490-b589f5ac3fb8)


---

## Project Structure

The project is structured as follows:
```
project/
│
├── static/
│   ├── css/
│   ├── js/
│   └── m_path_map.html
│
├── templates/
│   └── index.html
│
├── app.py
└── requirements.txt
```

![image](https://github.com/user-attachments/assets/6139e402-3e75-483c-9771-42bfe783989f)


---

## Setting Up the Environment

To run the project locally:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`.

---

![image](https://github.com/user-attachments/assets/30701acf-f4ea-4a9b-80fb-95627d18b97e)


## Displaying the Map

All calculations and rendering are handled by the backend using Python. The generated map is saved as `m_path_map.html` and displayed in the main HTML file using the `<iframe>` tag.

Example:
```html
<iframe src="/static/m_path_map.html" width="100%" height="500"></iframe>
```

By placing the `m_path_map.html` file in the `static` folder, Flask automatically detects and serves it. If set up correctly, the map will appear as shown below:

![image](https://github.com/user-attachments/assets/1e7ae2d6-d608-488b-b47e-0630c895e12a)

---



## User Input

To enhance user experience, the application includes the following features:

- **Dropdown for Airport Selection**: Users can select airports in various countries.
- **Search Filter**: Helps users quickly find airports by city.
- **Uncheck All**: Allows users to reset their selections and plan a new trip.
- **Generate Map**: After selecting airports, users can click "Generate Map" to display the optimized travel plan.

Example interface:

![image](https://github.com/user-attachments/assets/9f06d7db-3054-4d1b-9602-6888e008c792)


---

## Contribution

Feel free to fork this repository, submit issues, and send pull requests. Contributions are always welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```
