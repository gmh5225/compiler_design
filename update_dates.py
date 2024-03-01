import subprocess
import os

def is_binary(file_path):
    """Guess if a file is binary."""
    try:
        with open(file_path, 'rb') as file:
            return b'\0' in file.read(1024)
    except IOError:
        return True

def get_git_files():
    """Returns a list of all files tracked by Git, excluding those in the .obsidian folder."""
    result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True)
    files = result.stdout.splitlines()
    return [file for file in files if not file.startswith('.obsidian/')]

def get_last_commit_date(file_path):
    """Returns the last commit date of a file."""
    result = subprocess.run(['git', 'log', '-1', '--format=%ai', '--', file_path], capture_output=True, text=True, check=True)
    return result.stdout.strip()

def append_or_update_last_edited(file_path, last_edited_date):
    """Updates or appends the last edited date at the bottom of a file, after checking if it's not binary."""
    if is_binary(file_path):
        print(f"Skipped binary file: {file_path}")
        return

    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            found = False
            for i, line in enumerate(lines):
                if line.startswith("Last Edited: "):
                    lines[i] = f"Last Edited: {last_edited_date}\n"
                    found = True
                    break
            if not found:
                if lines and not lines[-1].strip() == "":
                    lines.append("\n")
                lines.append(f"Last Edited: {last_edited_date}\n")

            file.seek(0)
            file.writelines(lines)
            file.truncate()
    except UnicodeDecodeError:
        print(f"Skipped due to encoding issue: {file_path}")

def main():
    repo_path = os.path.join(os.path.expanduser('~'), 'compiler_design')
    os.chdir(repo_path)
    
    for file_path in get_git_files():
        last_edited_date = get_last_commit_date(file_path)
        append_or_update_last_edited(file_path, last_edited_date)
        print(f"Updated {file_path}")

if __name__ == "__main__":
    main()
