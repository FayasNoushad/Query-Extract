## Query Extract
Extract queries from url

## Installation

```
pip install Query-Extract
```

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
