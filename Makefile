APP_NAME := nosleep_menu
ICON := nosleep.icns
DMG_NAME := NoSleep.dmg

.PHONY: run build dmg clean

run:
	python3 $(APP_NAME).py


build: clean
	pyinstaller --onefile --windowed --icon=$(ICON) $(APP_NAME).py
	mkdir -p dist
	mv dist/$(APP_NAME).app dist/NoSleepMenu.app

dmg: build
	create-dmg \
	  --volname "NoSleep" \
	  --window-size 500 300 \
	  --icon-size 100 \
	  --icon "NoSleepMenu.app" 100 100 \
	  --icon "Applications" 350 100 \
	  --hide-extension "NoSleepMenu.app" \
	  --app-drop-link 350 100 \
	  $(DMG_NAME) \
	  dist/NoSleepMenu.app


clean:
	rm -rf build dist *.spec $(DMG_NAME)
