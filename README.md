# Portfolio Website (Resume-Driven)

This project demonstrates how to build a dynamic personal portfolio using **Python** and **Flask**. It follows the **TCREI Framework** (Task, Context, Reference, Evaluate, Iterate) to guide you through the process.

## 🌟 Features
- **Dynamic Content**: Data is loaded from `resume.json`, making it easy to update without touching HTML.
- **Modern Design**: Dark mode aesthetic with Glassmorphism effects using pure CSS.
- **Responsive**: Adapts to mobile and desktop screens.

## 📂 Folder Structure

```
portfolio_antigravity/
├── app.py              # Main Flask application (Backend)
├── resume.json         # Data source (your resume info)
├── README.md           # This guide
├── templates/          # HTML files (Frontend)
│   ├── base.html       # Layout template (inherited by others)
│   ├── home.html       # Landing page
│   ├── about.html      # Education & Objective
│   ├── projects.html   # Grid of project cards
│   ├── resume.html     # Skills & Certifications
│   └── contact.html    # Contact form placeholder
└── static/             # Static assets
    └── css/
        └── style.css   # Main stylesheet
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Basic knowledge of HTML/CSS

### Installation

1.  **Run the Application**:
    ```bash
    python app.py
    ```
2.  **View in Browser**:
    Open `http://127.0.0.1:5000` in your web browser.

## 🎓 TCREI Framework Explained

### T - Task
**Goal**: Build a portfolio that fetches data dynamically.
**Implementation**: We used `json.load()` in `app.py` to read `resume.json` and utilized Flask's `render_template` to inject this data into HTML.

### C - Context
**Why a Portfolio?**
A portfolio acts as "proof of work." Unlike a static PDF resume, a website shows you can *build* things. For a Data Science student, it allows you to showcase interactive charts or link directly to GitHub repos.

**Tech Stack**:
- **Flask**: A micro web framework for Python. Great for beginners because it's simple but powerful enough for production.
- **Jinja2**: The templating engine used by Flask (the `{% %}` syntax in HTML) that allows us to write dynamic loops and variables.
- **CSS3 Variables**: Used in `style.css` (`--bg-color`) to easily manage color themes.

### R - Reference
**Key Concepts**:
- **Routes**: `@app.route('/')` tells Flask what URL triggers which function.
- **Inheritance**: `{% extends 'base.html' %}` allows us to write the navigation bar once and use it everywhere.

### E - Evaluate
**Testing**:
- **Responsiveness**: Resize your browser window. The grid layouts in `projects.html` use `repeat(auto-fit, minmax(300px, 1fr))` to automatically adjust columns.
- **Data Accuracy**: Edit `resume.json` and refresh the page. The content should update immediately.

### I - Iterate (Next Steps)
To make this real-world ready:
1.  **Deployment**: Push this code to GitHub and connect it to **Render** or **PythonAnywhere** for free hosting.
2.  **Contact Form**: Currently, the form is static. You can use services like **Formspree** to make it actually send emails.
3.  **PDF Generation**: Implement a button to dynamically generate a PDF from the HTML content using `WeasyPrint`.

---

Built with ❤️ using Python & Flask.
