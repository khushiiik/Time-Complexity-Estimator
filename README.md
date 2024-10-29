# Time Complexity Estimator

A web application built with Django to help users estimate the time complexity of their code. Users can input their function code, and the app will provide an estimated time complexity.

## Features

- Input area for users to paste their function code.
- Button to analyze and estimate the time complexity.
- Displays the estimated time complexity in a clean and minimal UI.

## Technologies Used

- **Django**: Backend framework to handle requests and render templates.
- **HTML/CSS**: For the frontend UI design.

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/khushiiik/Time-Complexity-Estimator.git
   cd Time-Complexity-Estimator
   ```

2. Install the required dependencies:

   ```bash
   pip install django
   ```

3. Run the Django server:

   ```bash
   python manage.py runserver
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000/time/`.

### File Structure

- **views.py**: Contains the logic for estimating time complexity.
- **index.html**: Frontend for users to input their code.
- **result.html**: Displays the estimated time complexity.

### Usage

1. Enter your function code in the text area provided.
2. Click on **Analyze Time Complexity** to get an estimated complexity.

### Contributing

If you’d like to contribute to this project, please fork the repository and make a pull request.

### Acknowledgments

- Special thanks to the Django community for providing extensive documentation and support.

---

Enjoy coding!
