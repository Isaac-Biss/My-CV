# Resume Web Application using Django

## Overview

This web application is built using the Django framework to create an interactive and visually appealing online resume. It allows users to showcase their professional experience, skills, and projects in a structured and easily accessible format. The application provides a user-friendly interface for both the resume owner to manage their content and visitors to view the resume.

## Features

1. **User Authentication**: Secure user authentication system to allow resume owners to log in and update their information.

2. **Profile Section**: A dedicated section to display personal information, including name, contact details, and a brief bio.

3. **Experience**: Clearly organized section to list professional experience, including job titles, companies, dates, and job descriptions.

4. **Skills**: A visually appealing display of skills with the option to categorize them for better organization.

5. **Education**: An area to showcase educational background, including degrees, institutions, and graduation dates.

6. **Projects**: Highlight your significant projects with detailed descriptions, technologies used, and project timelines.

7. **Customizable Themes**: Choose from a variety of themes to personalize the appearance of the resume.

8. **Mobile Responsiveness**: Ensures a seamless experience for users accessing the resume on various devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Isaac-Biss/My-CV.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the admin panel at `http://127.0.0.1:8000/admin/` to log in with the superuser credentials and start managing your resume content.

## Usage

1. Log in with your superuser account.

2. Navigate to the admin panel to update personal information, experience, skills, education, and projects.

3. Customize the resume theme by selecting the desired theme in the settings.

4. View your resume at `http://127.0.0.1:8000/` and share the link with others.

## Contributing

If you'd like to contribute to the project, feel free to submit issues or pull requests. Contributions are welcome and appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README to better fit your specific project details and preferences. Good luck with your Django web application!