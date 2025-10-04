# 🤝 Contributing to HITEC-CS312L AI Labs

First off, thank you for taking the time to contribute!  
This project is meant to support **CS312L: Artificial Intelligence Lab** at HITEC University.  
We welcome contributions that improve labs, fix bugs, or enhance documentation.

---

## 📜 Code of Conduct
Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md).  
By participating in this project you agree to abide by its terms.

---

## 🛠 How Can I Contribute?

### 1. Reporting Issues
- Use the **Issues** tab in GitHub.  
- Search existing issues before opening a new one.  
- Provide clear details (lab/task number, error message, screenshots if possible).

### 2. Suggesting Enhancements
- Create an **Enhancement Issue** describing:
  - What problem it solves
  - Why it’s useful
  - Example use case

### 3. Contributing Code
- Fork the repository  
- Create a branch:
  ```bash
  git checkout -b lab-XX-task-YY-feature
  ```
 
* Make your changes under the correct lab/task folder
* Add/update tests if relevant
* Ensure all tests pass:

  ```bash
  pytest
  ```
* Push your branch and open a Pull Request (PR)

---

## 🔧 Coding Standards

* **Language**: Python 3.10+
* **Style**: [PEP8](https://peps.python.org/pep-0008/) with enforced tools:

  * `black` for formatting
  * `flake8` for linting
* **Tests**: Write unit tests with `pytest`. Place them in `tests/` folders.
* **Notebooks**: Keep clean, minimal output. Avoid committing heavy data outputs.

---

## 📂 Repo Structure Reminder

* `labs/Lab-XX/Task-YY/notebooks/` → interactive notebooks
* `labs/Lab-XX/Task-YY/src/` → Python scripts/functions
* `labs/Lab-XX/Task-YY/tests/` → pytest unit tests
* `examples/` → reference solutions (instructor only)

Always follow this structure so labs remain consistent.

---

## ✅ Pull Request Process

1. Update `README.md` or task `README.md` with details of changes if necessary
2. Verify tests and formatting pass locally
3. Ensure your branch is up-to-date with `main` before submitting PR
4. Fill out the PR template with:

   * Summary of changes
   * Related issue number (if applicable)
   * Screenshots (if UI/notebook change)

---

## 📄 Licensing

By contributing, you agree that your contributions will be licensed under:

* **MIT License** for code
* **CC BY-NC-SA 4.0** for course content

---

Thanks again for your contribution 🙌
Together, we can make AI learning more interactive and fun 🚀
