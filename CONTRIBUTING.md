# 🤝 Contributing to ParkEase

Thanks for your interest in contributing to **ParkEase**!  
This project aims to automate parking using ESPHome, Home Assistant, and AI — and we're happy to welcome suggestions, improvements, and bug reports.

## 🚀 Getting Started

1. **Fork the repository** to your GitHub account.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/ParkEase-ESPHome.git
   cd ParkEase-ESPHome
   ````
3. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**, commit, and push:
   ```bash
   git add .
   git commit -m "Add: [Your feature or fix]"
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request (PR)** with a clear explanation of what you changed and why.



## 🧠 Areas You Can Contribute To

* Improving or testing the ESPHome configurations
* Expanding Home Assistant dashboard integrations
* Working on the AI model for car/slot detection
* Reporting bugs and suggesting UI/UX improvements
* Writing documentation (README, usage guide, wiring diagrams, etc.)

---

## 📂 Project Structure

| File/Folder            | Purpose                                      |
| ---------------------- | -------------------------------------------- |
| `parkEase.yaml`        | ESPHome config for sensors + gate            |
| `cam.yaml`             | ESPHome config for camera                    |
| `dashboard.yaml`       | Home Assistant dashboard layout              |
| `carDetectionModel/`   | ML model and scripts for car detection (WIP) |
| `Images/`              | Example images (dashboards, test inputs/outputs) |
| `requirements.txt`     | Python libraries required for the ML scripts |
| `README.md`            | Main project overview                        |
| `CONTRIBUTION.md`      | Contribution guidelines (you are here)       |
| `secrets.yaml`         | Wi-Fi and API credentials (not committed)    |


---

## 🛠 Code Guidelines

* Keep YAML code clean and properly indented.
* Comment clearly on logic where needed.
* Use meaningful commit messages (`Add:`, `Fix:`, `Refactor:`, etc.).
* Don't commit `.pt` model files or secrets (`.gitignore` is in place).

## 🐛 Reporting Bugs

If you encounter a bug:

1. Check if it already exists in [Issues](https://github.com/YJuDeAd/ParkEase-ESPHome/issues).
2. If not, open a new issue with:

   * A clear title
   * Steps to reproduce the problem
   * What you expected vs. what actually happened
   * Any relevant logs, screenshots, or error messages

## 🧠 Before You Submit

* Ensure your changes work and don’t break existing features.
* Test ESPHome YAML locally via `esphome run`.
* If you're working with AI, verify your script runs cleanly with the current `requirements.txt`.

## 📬 Questions?

If you're unsure about something, open an issue or discussion — happy to help!

Thanks for helping improve ParkEase! 🚗✨
