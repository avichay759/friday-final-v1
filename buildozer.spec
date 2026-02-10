[app]
title = FRIDAY RED CORE
package.name = friday_red
package.domain = org.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,requests,certifi,urllib3,chardet,idna,sqlite3
orientation = portrait
permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, VIBRATE
android.api = 33
android.minapi = 21
android.arch = armeabi-v7a
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
