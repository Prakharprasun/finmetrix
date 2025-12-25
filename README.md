# Finmetrix

**Finmetrix** is a minimal, high-performance financial metrics library featuring a Python‑first API and an optional C++ backend powered by pybind11.

---

## 🚀 Features

- **Time‑Weighted Return (TWR)** – Accurate multi‑period return calculation  
- **Automatic backend dispatch** – Uses the fastest available backend (C++ or Python)  
- **Zero‑copy numerical kernels** – Avoids unnecessary data duplication  
- **Deterministic results** – Identical numerical output across all backends  
- **Lightweight & minimal** – No unnecessary dependencies

---

## 📦 Installation

### For Users
Coming soon on PyPI.

### For Developers

1. **Create and activate a virtual environment**
   ```bash
   python3 -m venv fm
   source fm/bin/activate  # On Windows: fm\Scripts\activate
   ```
   ⚠️ **Note:** Conda is not recommended due to potential ABI incompatibilities.

2. **Install dependencies**
   ```bash
   pip install -U pip
   pip install -r requirements.txt
   ```
   `requirements.txt` contains exact, tested versions generated via `pip freeze`.

3. **Install in editable mode**
   ```bash
   pip install -e .
   ```
   This builds the C++ extension and installs Finmetrix in development mode.

---

## 🧠 Backend Selection

Finmetrix automatically selects the optimal backend at import time, falling back to the pure‑Python implementation only if the C++ extension is unavailable.

```python
from finmetrix._backend import BACKEND
print(f"Active backend: {BACKEND}")  # Output: "cpp" or "python"
```

---

## 📊 Usage

```python
from finmetrix import twr
from finmetrix._backend import BACKEND

returns = [0.10, -0.10, 0.05]
print("Backend:", BACKEND)
print(f"TWR: {twr(returns):.4f}")
```

---

## 🧪 Testing

Run tests using the active interpreter:

```bash
python -m pytest
```
*Always invoke pytest via `python -m` to ensure the correct environment is used.*

---

## 🔧 Development Notes

### Updating Dependencies (Maintainers Only)
```bash
pip install <new-package>
pip freeze > requirements.txt
```
**Never edit `requirements.txt` manually.**

### Toolchain (macOS)
- LLVM/Clang (installed via Homebrew)
- CMake (via scikit‑build‑core)
- Ninja (handled automatically)

**Tested Environment:**
- Python 3.12
- macOS arm64 (Apple Silicon)
- LLVM Clang

---

## 📁 Project Structure
```
finmetrix/
├── finmetrix/
│   ├── __init__.py
│   └── _backend/
│       ├── __init__.py
│       └── cpp/          # C++ extension source
├── tests/
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🎯 Design Principles
- **Python for validation** – User‑friendly API and error handling
- **C++ for math** – High‑performance numerical kernels
- **Transparent execution** – No silent backend fallbacks
- **Numerical consistency** – Identical results across implementations

---

## 📌 Status
**Stable API** – Actively maintained. C++ backend fully verified and tested.