# 🎓 HITEC-CS312L AI Labs

> A hands-on, interactive Python lab repository for **CS312L: Artificial Intelligence Lab** at HITEC University  
> Featuring Jupyter notebooks, auto-graded tasks, reference solutions, and learning support

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejY2NTc2a3RpdmVwcmlxbmpwanVybHJ1b3Uxczd6anR1c3R3OWMzcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Lny6Rw04nsOOc/giphy.gif" width="1000" alt="AI Coding GIF">
</p>

---

## 🏷️ Badges

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/docs-available-brightgreen" alt="Docs Available">
  <img src="https://img.shields.io/github/actions/workflow/status/UsamaMatrix/HITEC-CS312L-AI-Labs/ci.yml?branch=main" alt="Build Status">
  <img src="https://img.shields.io/github/last-commit/UsamaMatrix/HITEC-CS312L-AI-Labs" alt="Last Commit">
</p>

---

## 🧭 Table of Contents

1. [About](#about)  
2. [Repository Structure](#repository-structure)  
3. [Quick Start](#quick-start)  
4. [How to Work Through the Labs](#how-to-work-through-the-labs)  
5. [Testing & Autograding](#testing--autograding)  
6. [Contribution & Style Guide](#contribution--style-guide)  
7. [Licenses](#licenses)  
8. [Contact & Support](#contact--support)  

---

## 🧠 About

This repo contains **14+ lab modules** aligned with the CS312L AI syllabus — from Python fundamentals and search algorithms to machine learning and deep learning.  
Each lab is broken down into **tasks**, combining narrative notebooks, coding skeletons, and automated tests to ensure an interactive and structured learning experience.  

---

## 📁 Repository Structure

```

.
├── .github/                   # GitHub settings, issue templates, workflows
├── labs/
│   ├── Lab-01/
│   │   ├── Task-01/
│   │   ├── Task-02/
│   │   └── README.md
│   └── Lab-14/ …
├── data/                      # Sample datasets or download scripts
├── notebooks/                 # Shared notebooks & helpers
├── examples/                  # Instructor/reference solutions
├── assets/                    # Images, GIFs, diagrams
├── requirements.txt
├── LICENSE                    # MIT (for code)
├── LICENSE-content.md         # CC (for materials)
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── README.md

````

---

## 🚀 Quick Start

```bash
git clone https://github.com/UsamaMatrix/HITEC-CS312L-AI-Labs.git
cd HITEC-CS312L-AI-Labs
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
````

Open a lab folder (e.g. `labs/Lab-01/Task-01/notebooks/Task-01.ipynb`) to begin.

---

## 🎯 How to Work Through the Labs

* Each **Lab-XX** corresponds to a module/week.
* Within, **Task-YY** is a self-contained exercise:

  * `notebooks/` contains narrative & starter code
  * `src/` is where you implement functions
  * `tests/` contains pytest tests to validate your work
  * `README.md` explains objectives, instructions & hints
* Use `examples/` only when you need reference after submission.

<p align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExem53MTg3dDkwOXhpOGF3NTJkbDJrcjN1bHB5aWswdDZ6OGdrNGVqOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dZX3AduGrY3uJ7qCsx/giphy.gif" width="1000" alt="Learning AI GIF">
</p>

---

## ✅ Testing & Autograding

* Run `pytest labs/Lab-XX/Task-YY/tests` to check your solutions
* Notebooks may be validated using `nbval` in CI
* CI workflows (GitHub Actions) will:

  1. install dependencies
  2. run code style checks (`black --check`, `flake8`)
  3. run pytest across tasks
  4. optionally run notebook validation

---

## 🤝 Contribution & Style Guide

* Fork → create branch under `lab-XX-feature` → make changes → open Pull Request
* Adhere to formatting: **Black**, **Flake8**
* Run tests before submitting
* Follow filename & folder naming conventions exactly (`Lab-01/Task-01`)
* Use meaningful commit messages

See `CONTRIBUTING.md` for full guide.

---

## 📝 Licenses

| Component                     | License                                    |
| ----------------------------- | ------------------------------------------ |
| Code (Python, scripts)        | MIT (see `LICENSE`)                        |
| Course materials (labs, text) | CC BY-NC-SA 4.0 (see `LICENSE-content.md`) |

In short: code is open for reuse; lab instructions require attribution, non-commercial use, and shared format.

---

## 📬 Contact & Support

For issues, questions or suggestions: open a GitHub issue or email the course owner/CO.
This repo is a living project — improvements and feedback are welcome!

---

*“Learning AI by doing — code, test, reflect, repeat.”*
