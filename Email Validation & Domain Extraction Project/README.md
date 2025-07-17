### ✅ Email Validation & Domain Extraction Project

This project processes a list of emails from a `.csv` or `.xlsx` file, validates them using Python, and extracts their domains.

---

### 📁 File Structure:

* `E-mails.csv` / `E-mails.xlsx`:
  Input files containing a list of emails.

* `v_emails.csv`:
  Output file with only the **valid** emails after processing.

* `validation.py`:
  Contains utility functions:

  * `valid(email)`: Checks if an email is valid .
  * `get_domain(emails)`: Extracts domains from valid emails.

* `valid_emails.py`:
  Reads the input CSV file, validates the emails, and writes valid ones to `v_emails.csv`.

---

### ▶️ How to Run

Make sure you have Python installed. Then in your terminal or VS Code:

```bash
python valid_emails.py
```

The script will:

1. Read emails from `E-mails.csv`.
2. Use `validation.py` functions to:

   * Filter only valid emails.
   * Optionally extract domains.
3. Save valid emails into `v_emails.csv`.

---

### 🧪 Example

Input (`E-mails.csv`):

```
example@gmail.com
wrong_email@com
test@domain.org
```

Output (`v_emails.csv`):

```
example@gmail.com
test@domain.org
```

---

### 📦 Requirements

No external libraries needed — just standard Python (works with Python 3.6+).
