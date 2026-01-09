# 10. The Multiverse: Virtual Environments

> "You're not the only Spider-Man."

Every project should live in its own universe.
- Use `requests` version 1 for Project A.
- Use `requests` version 2 for Project B.

If you install everything globally, universes collide (Version Conflicts). We use **venv** to create isolated bubbles.

## 1. Creating a Venv (The Spell)
Open Terminal in your project folder.

**Windows:**
```bash
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

You will see a folder named `venv` appear.

## 2. Activating the Venv (Entering the Portal)
You must activate it to use it.

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` appear in your terminal name.

## 3. Installing Libraries *Inside* Venv
Now, when you `pip install`, it goes into *this* folder only.

```bash
pip install pandas
```

## 4. Deactivating (Returning Home)
```bash
deactivate
```

## 5. Requirements.txt (The Spellbook)
Share your environment list so others can replicate it.

**Save:**
```bash
pip freeze > requirements.txt
```

**Install from file:**
```bash
pip install -r requirements.txt
```

---
**Next Module:** Real World Automation (The Utility Belt).
