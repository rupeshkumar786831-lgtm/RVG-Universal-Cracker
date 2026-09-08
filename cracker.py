#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile
import rarfile
import py7zr
import pikepdf
import os
import time
import sys
import subprocess
import getpass

# -------------------- BANNER --------------------
def banner():
    os.system('clear')
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║     ██████╗ ██████╗  █████╗  ██████╗██╗  ██╗███████╗   ║
    ║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝   ║
    ║     ██████╔╝██████╔╝███████║██║     █████╔╝ █████╗     ║
    ║     ██╔══██╗██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝     ║
    ║     ██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗   ║
    ║     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ║
    ║                                                          ║
    ║         🔐 UNIVERSAL PASSWORD CRACKER 🔐                ║
    ║       ZIP | RAR | 7Z | PDF | DOCX | XLSX | APK         ║
    ║                  BY RVG DEVELOPER                        ║
    ╚══════════════════════════════════════════════════════════╝
    """)

# -------------------- STORAGE PERMISSION --------------------
def check_storage():
    if os.path.exists("/sdcard/Android"):
        return True
    else:
        print("\n⚠️ Storage permission not detected!")
        print("📌 Run: termux-setup-storage")
        return False

# -------------------- FILE TYPE DETECTION --------------------
def detect_file_type(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    
    file_types = {
        '.zip': 'zip',
        '.rar': 'rar',
        '.7z': '7z',
        '.pdf': 'pdf',
        '.docx': 'docx',
        '.xlsx': 'xlsx',
        '.pptx': 'pptx',
        '.apk': 'apk'
    }
    
    return file_types.get(ext, None)

# -------------------- CRACK FUNCTIONS --------------------
def crack_zip(filepath, password):
    try:
        with zipfile.ZipFile(filepath) as zf:
            zf.extractall(pwd=password.encode('utf-8'), path='/tmp/rvg_crack/')
        return True
    except:
        return False

def crack_rar(filepath, password):
    try:
        with rarfile.RarFile(filepath) as rf:
            rf.extractall(path='/tmp/rvg_crack/', pwd=password)
        return True
    except:
        return False

def crack_7z(filepath, password):
    try:
        with py7zr.SevenZipFile(filepath, password=password) as sz:
            sz.extractall(path='/tmp/rvg_crack/')
        return True
    except:
        return False

def crack_pdf(filepath, password):
    try:
        pikepdf.open(filepath, password=password)
        return True
    except:
        return False

def crack_office(filepath, password):
    try:
        with zipfile.ZipFile(filepath) as zf:
            zf.extractall(pwd=password.encode('utf-8'), path='/tmp/rvg_crack/')
        return True
    except:
        return False

def crack_apk(filepath, password):
    try:
        with zipfile.ZipFile(filepath) as zf:
            zf.extractall(pwd=password.encode('utf-8'), path='/tmp/rvg_crack/')
        return True
    except:
        return False

# -------------------- GET FILE PATH (HIDDEN) --------------------
def get_hidden_path(prompt):
    while True:
        print(f"\n📂 {prompt}")
        path = getpass.getpass("📁 Enter path (hidden): ").strip()
        
        if os.path.exists(path):
            return path
        
        for base in ["/sdcard/Download/", "/sdcard/", "./"]:
            test_path = base + path
            if os.path.exists(test_path):
                print(f"✅ Found: {test_path}")
                return test_path
        
        print(f"❌ File not found: {path}")
        retry = input("🔄 Retry? (y/n): ").strip().lower()
        if retry != 'y':
            return None

# -------------------- CRACK ENGINE --------------------
def crack_file(filepath, wordlist, file_type):
    total = 0
    try:
        with open(wordlist, 'r', encoding='latin-1', errors='ignore') as f:
            total = sum(1 for _ in f)
    except:
        total = 0
    
    print(f"\n📊 Total passwords: {total:,}")
    print(f"📂 File Type: {file_type.upper()}")
    print("⏳ Starting crack...\n")
    
    start_time = time.time()
    count = 0
    found = False
    
    crack_functions = {
        'zip': crack_zip,
        'rar': crack_rar,
        '7z': crack_7z,
        'pdf': crack_pdf,
        'docx': crack_office,
        'xlsx': crack_office,
        'pptx': crack_office,
        'apk': crack_apk
    }
    
    crack_func = crack_functions.get(file_type)
    if not crack_func:
        print("❌ Unsupported file type!")
        return None
    
    try:
        with open(wordlist, 'r', encoding='latin-1', errors='ignore') as f:
            for password in f:
                password = password.strip()
                count += 1
                
                if count % 100 == 0:
                    elapsed = time.time() - start_time
                    speed = count / elapsed if elapsed > 0 else 0
                    print(f"⏳ Tried: {count:,} | Speed: {speed:.0f}/sec")
                
                if crack_func(filepath, password):
                    print("\n" + "="*60)
                    print("🎉 " + "="*56)
                    print(f"✅ PASSWORD FOUND: {password}")
                    print(f"⏱️  Time: {time.time() - start_time:.2f} seconds")
                    print(f"📊 Position: {count:,} / {total:,}")
                    print("🎉 " + "="*56)
                    print("="*60)
                    return password
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user.")
        sys.exit(0)
    
    print("\n❌ Password NOT found in wordlist")
    return None

# -------------------- MAIN LOOP --------------------
def main_loop():
    while True:
        print("\n" + "="*60)
        print("📂 SUPPORTED FILE TYPES")
        print("="*60)
        print("   ZIP | RAR | 7Z | PDF | DOCX | XLSX | PPTX | APK")
        print("="*60 + "\n")
        
        target_file = get_hidden_path("Enter target file path:")
        if target_file is None:
            print("❌ File selection cancelled.")
            return
        
        file_type = detect_file_type(target_file)
        if file_type is None:
            print("❌ Unsupported file type!")
            print("💡 Supported: .zip, .rar, .7z, .pdf, .docx, .xlsx, .pptx, .apk")
            continue
        
        wordlist = get_hidden_path("Enter wordlist path:")
        if wordlist is None:
            print("❌ Wordlist selection cancelled.")
            continue
        
        result = crack_file(target_file, wordlist, file_type)
        
        if result:
            print(f"\n✅ CRACKED! Password: {result}")
            print(f"📂 Extracted to: /tmp/rvg_crack/")
        else:
            print("\n❌ CRACK FAILED! Try a different wordlist.")
        
        print("\n" + "="*60)
        again = input("🔄 Crack another file? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Exiting...")
            break

# -------------------- MAIN --------------------
if __name__ == "__main__":
    try:
        import rarfile
        import py7zr
        import pikepdf
        import getpass
    except ImportError:
        print("⚠️ Installing dependencies...")
        os.system("pip install rarfile py7zr pikepdf pycryptodome")
        print("✅ Done. Run again.")
        sys.exit(0)
    
    banner()
    
    if not check_storage():
        print("❌ Storage permission required. Exiting...")
        sys.exit(1)
    
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user.")
        print("👋 Exiting...")
