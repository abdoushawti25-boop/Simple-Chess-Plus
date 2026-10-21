#!/usr/bin/env python3
import os
import zipfile
import shutil

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ZIP_NAMES = [
    'simple-chess-plus.zip',
    'simple-chess-build-apk.zip',
    'simple-chess-github.zip',
    'simple-chess-source.zip'
]

EXCLUDE_DIRS = {
    'node_modules',
    '.android-sdk',
    'dist',
    '.git',
    '.gradle',
    'build',
    '__pycache__'
}

EXCLUDE_EXTENSIONS = {
    '.zip',
    '.tar',
    '.gz',
    '.hprof',
    '.class'
}

def create_zip(target_zip_path):
    print(f"Generating archive: {target_zip_path}")
    os.makedirs(os.path.dirname(target_zip_path), exist_ok=True)
    
    with zipfile.ZipFile(target_zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
        # 1. Explicitly create directory entries for .github and .github/workflows
        zip_info_gh = zipfile.ZipInfo('.github/')
        zip_info_gh.external_attr = 0o755 << 16 | 0x10  # directory attribute
        zipf.writestr(zip_info_gh, '')

        zip_info_wf = zipfile.ZipInfo('.github/workflows/')
        zip_info_wf.external_attr = 0o755 << 16 | 0x10  # directory attribute
        zipf.writestr(zip_info_wf, '')

        count = 0
        added_paths = set()

        # 2. Explicitly write .github/workflows/build-apk.yml
        wf_file = os.path.join(PROJECT_ROOT, '.github', 'workflows', 'build-apk.yml')
        if os.path.exists(wf_file):
            zipf.write(wf_file, arcname='.github/workflows/build-apk.yml')
            added_paths.add('.github/workflows/build-apk.yml')
            count += 1
            print("Verified addition of: .github/workflows/build-apk.yml")

        # 3. Explicitly write package-lock.json
        pkg_lock = os.path.join(PROJECT_ROOT, 'package-lock.json')
        if os.path.exists(pkg_lock):
            zipf.write(pkg_lock, arcname='package-lock.json')
            added_paths.add('package-lock.json')
            count += 1
            print("Verified addition of: package-lock.json")

        # 4. Walk the entire project root
        for root, dirs, files in os.walk(PROJECT_ROOT):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in EXCLUDE_EXTENSIONS:
                    continue
                
                abs_file = os.path.join(root, file)
                rel_file = os.path.relpath(abs_file, PROJECT_ROOT).replace(os.sep, '/')

                # Skip if excluded
                parts = rel_file.split('/')
                if any(p in EXCLUDE_DIRS for p in parts):
                    continue
                if rel_file in added_paths:
                    continue

                zipf.write(abs_file, arcname=rel_file)
                added_paths.add(rel_file)
                count += 1

    print(f"Archive created with {count} files, size: {os.path.getsize(target_zip_path)/1024:.1f} KB")

def main():
    for name in ZIP_NAMES:
        root_path = os.path.join(PROJECT_ROOT, name)
        public_path = os.path.join(PROJECT_ROOT, 'public', name)
        dist_path = os.path.join(PROJECT_ROOT, 'dist', name)

        create_zip(root_path)
        shutil.copy2(root_path, public_path)
        if os.path.exists(os.path.dirname(dist_path)):
            shutil.copy2(root_path, dist_path)
        print(f"Available at: public/{name} and dist/{name}")

if __name__ == '__main__':
    main()
