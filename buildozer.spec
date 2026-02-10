[app]

# (str) Title of your application
title = FRIDAY RED CORE

# (str) Package name
package.name = friday_red

# (str) Package domain (needed for android packaging)
package.domain = org.boss

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0.0

# (list) Application requirements
# הוספתי כאן את כל מה שצריך בשביל המוח, הקול והתקשורת המאובטחת
requirements = python3,kivy,requests,certifi,urllib3,chardet,idna,hostpython3

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
# הרשאות לאינטרנט, הקלטת קול (לפקודות), ואחסון (להגנה על קבצים)
permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, VIBRATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android architecture to build for
android.arch = armeabi-v7a

# (bool) indicates if the application should be fullscreen or not
fullscreen = 1

# (list) List of service to declare
# כאן נוכל להוסיף את שירות ההגנה שירוץ ברקע בעתיד
services = 

[buildozer]

# (int) log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) display warning on buildozer version
warn_on_root = 1
