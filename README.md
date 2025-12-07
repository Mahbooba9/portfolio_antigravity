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
---

Built with ❤️ using Python & Flask.
