# ☀️ NoSleepApp

A simple macOS menu bar app that prevents your Mac from going to sleep using the built-in `caffeinate` command.

---

## 🚀 How to run (just run, without building .app)

1. Install dependencies:

```bash
pip install rumps

    Run the app:

python nosleep_menu.py

🛠 How to build .app

    Install PyInstaller:

pip install pyinstaller

    Build the app:

pyinstaller --onefile --windowed --icon=img/nosleep.icns nosleep_menu.py

The .app will be created in the dist/ folder.
📦 How to create .dmg

    Create .app as described above.

    Install create-dmg tool (requires Node.js):

brew install create-dmg

    Create DMG:

create-dmg 'dist/nosleep_menu.app' --overwrite

☀️ NoSleepApp (на русском)

Простое приложение в строке меню macOS, блокирующее сон компьютера через встроенную команду caffeinate.
🚀 Как запустить без сборки

    Установи зависимости:

pip install rumps

    Запусти приложение:

python nosleep_menu.py

🛠 Как собрать .app

    Установи PyInstaller:

pip install pyinstaller

    Собери приложение:

pyinstaller --onefile --windowed --icon=img/nosleep.icns nosleep_menu.py

Файл .app появится в папке dist/.
📦 Как собрать .dmg

    Сначала собери .app как описано выше.

    Установи create-dmg (нужен Node.js):

brew install create-dmg

    Собери .dmg:

create-dmg 'dist/nosleep_menu.app' --overwrite

✅ Зависимости

    rumps

📌 Автор

Вячеслав, 2025
[Telegram: @RidersWeb]