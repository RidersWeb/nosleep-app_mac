import rumps
import subprocess

class NoSleepApp(rumps.App):
    def __init__(self):
        super().__init__("🛌 Сон разрешён", quit_button=None)
        self.proc = None
        self.menu_item = rumps.MenuItem("🔒 Заблокировать сон", callback=self.toggle)
        self.menu = [self.menu_item, "Выход"]

    def toggle(self, sender):
        if self.proc is None:
            try:
                self.proc = subprocess.Popen(["/usr/bin/caffeinate", "-dims"])
                self.title = "⛔ Сон заблокирован"
                self.menu_item.title = "✅ Разрешить сон"
            except Exception as e:
                rumps.alert(f"Ошибка запуска caffeinate:\n{e}")
        else:
            try:
                self.proc.terminate()
                self.proc = None
                self.title = "🛌 Сон разрешён"
                self.menu_item.title = "🔒 Заблокировать сон"
            except Exception as e:
                rumps.alert(f"Ошибка остановки caffeinate:\n{e}")

    @rumps.clicked("Выход")
    def quit_app(self, _):
        if self.proc:
            self.proc.terminate()
        rumps.quit_application()

if __name__ == "__main__":
    NoSleepApp().run()
