```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Query-Extract/blob/main/LICENSE
```

---

## Installation

```
pip install Query-Extract
```

---

## Usage

```py
import query_extract


link = "https://github-readme-stats.vercel.app/api?username=FayasNoushad&theme=tokyonight"
print(query_extract.extract(link))
# returns :-
"""
{
    "username": "FayasNoushad",
    "theme": "tokyonight"
}
"""

data = {
    "username": "FayasNoushad",
    "theme": "tokyonight"
}
print(query_extract.stringify(data))
# => username=FayasNoushad&theme=tokyonight
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
