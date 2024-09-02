# Hyperimon

**Hyperimon** is a web-based application designed to simplify the process of planning and installing solar panels. It helps users create detailed project plans, calculate necessary configurations, and generate straightforward technical drawings to streamline the installation process.

## Key Features

- **Project Creation**: Easily create and manage multiple solar panel installation projects.
- **Accurate Measurements**: Input the actual dimensions of the roof or structure for precise calculations.
- **Automatic Calculations**: The app calculates how many panels can fit based on the entered data and provides recommendations.
- **Manual Editing**: Adjust project details manually if needed.
- **Simple Technical Drawings**: Generate basic visualizations of the panel layout on the roof.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML/CSS, JavaScript
- **Database**: SQLite

## Getting Started

To get a local copy of the project up and running, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/hyperimon.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd hyperimon
    ```

3. **Set up a virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

   Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

For major changes, please open an issue to discuss the changes you propose.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or questions, please contact [artem.monkiewicz@gmail.com](mailto:artem.monkiewicz@gmail.com).
