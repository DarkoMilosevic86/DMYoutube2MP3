# Contributing to DM Youtube2MP3

Thank you for your interest in contributing to DM Youtube2MP3! Contributions are welcome and appreciated. Whether you're fixing bugs, suggesting improvements, or adding new features, your help is valuable.

---

## 🐞 Reporting Bugs

If you find a bug or something that doesn't work as expected:

- Open a GitHub issue.
- Provide clear and reproducible steps.
- Include your operating system, Python version, and a description of the issue.
- Screenshots or logs are helpful!

---

## 💡 Suggesting Features

Have an idea to improve the app?

- Open a GitHub issue with the label `enhancement`.
- Describe the feature clearly and why it's useful.
- If possible, suggest how it could be implemented.

---

## 💻 Contributing Code

To contribute code:

1. **Fork** the repository.
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature-your-feature-name
3. 
Make your changes (use comments and docstrings).
4. 
Follow PEP8 coding standards.
5. 
Run and test the application to verify everything works.
6. 
Submit a pull request with a clear explanation of what you’ve changed.
 
🌍 Localization
This app supports multiple languages using JSON translation files.
• 
Translations are stored in the languages/ directory (e.g. en_US.json, de_DE.json).
• 
When adding new strings to the UI, make sure to add them to the default language file (en_US.json).
• 
If you want to add or update a translation, modify or create the appropriate file and test that the keys match.
 
✅ Pull Request Guidelines
• 
Keep PRs focused — one feature/fix per PR.
• 
Add clear commit messages and descriptive PR titles.
• 
Avoid mixing refactoring with feature changes unless necessary.
• 
Update documentation or translation files if relevant.
 
📋 Code Style
• 
Python 3.8+ compatible
• 
Follow PEP8 and use 4-space indentation.
• 
GUI code is written using wxPython — use appropriate sizers and layout practices.
• 
String literals for UI elements should always go through the translation system (e.g. _("Download")).
 
Thanks again for your contribution!