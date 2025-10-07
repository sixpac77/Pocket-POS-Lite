[app]
title = Pocket POS Lite
package.name = pocket_pos_lite
package.domain = com.homenest
source.dir = .
source.include_exts = py, png, jpg, kv, atlas
version = 0.4.0
version.code = 400
requirements = python3, kivy==2.3.1, pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# App icons/splash optional:
# icon.filename = %(source.dir)s/assets/icon.png
# presplash.filename = %(source.dir)s/assets/presplash.png

# Avoid asking for NDK/SDK interactively
p4a.local_recipes = 
android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21
android.ndk_api = 21
