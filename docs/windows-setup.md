# Windows workstation setup

## Checklist

1. Install Git for Windows and verify `git --version` in PowerShell.
2. Install Python 3.10+ and verify `py --version` or `python --version`.
3. Install VS Code and the Microsoft Python extension.
4. Clone `windows-setup`, open the folder in VS Code, and select the Python interpreter.
5. In the VS Code terminal (PowerShell), run `py -m unittest discover -s tests -v`.

## Optional virtual environment

Lab 01 has no third-party dependencies, so a virtual environment is optional:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Calling the environment's Python directly avoids changing PowerShell execution policy. If `py` is unavailable, substitute `python`.

## Windows vs macOS quick reference

| Task | Windows PowerShell | macOS terminal |
| --- | --- | --- |
| Python launcher | `py` (or `python`) | `python3` |
| Run simulation | `py -m src.cooling_lab --steps 60` | `python3 -m src.cooling_lab --steps 60` |
| Run tests | `py -m unittest discover -s tests -v` | `python3 -m unittest discover -s tests -v` |
| Virtualenv interpreter | `.\.venv\Scripts\python.exe` | `.venv/bin/python` |
| Git status | `git status` | `git status` |

## Troubleshooting

- **Python not found:** restart the terminal after installing Python; check the launcher and PATH.
- **Microsoft Store alias appears:** use the verified `py` launcher or adjust Windows app execution aliases.
- **`No module named src`:** run commands from the repository root, not from inside `src`.
- **Wrong branch:** run `git branch --show-current` and switch to `windows-setup`.

This track uses software simulation only. Do not attach production controllers or connect to operational industrial networks.
