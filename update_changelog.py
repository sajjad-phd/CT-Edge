import subprocess
import datetime
import re
from pathlib import Path

def get_latest_commit_info():
    """Get the latest commit information"""
    try:
        # Get the latest commit message
        commit_msg = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%B'],
            universal_newlines=True
        ).strip()
        
        # Get the latest commit hash
        commit_hash = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%H'],
            universal_newlines=True
        ).strip()[:7]  # Get first 7 characters of hash
        
        return commit_msg, commit_hash
    except subprocess.CalledProcessError:
        return None, None

def update_changelog():
    """Update the CHANGELOG.md file with the latest commit information"""
    changelog_path = Path('CHANGELOG.md')
    
    # Get current time
    now = datetime.datetime.now()
    date_str = now.strftime('%Y-%m-%d %H:%M:%S')
    
    # Get latest commit info
    commit_msg, commit_hash = get_latest_commit_info()
    
    if not commit_msg:
        print("No commit information found. Make sure you're in a git repository.")
        return
    
    # Read current changelog
    if changelog_path.exists():
        with open(changelog_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n"
    
    # Extract current version
    version_match = re.search(r'## \[(\d+\.\d+\.\d+)\]', content)
    if version_match:
        current_version = version_match.group(1)
        major, minor, patch = map(int, current_version.split('.'))
        new_version = f"{major}.{minor}.{patch + 1}"
    else:
        new_version = "1.0.0"
    
    # Create new changelog entry
    new_entry = f"\n## [{new_version}] - {date_str}\n\n"
    new_entry += f"### Commit: {commit_hash}\n"
    new_entry += f"- {commit_msg}\n"
    
    # Add new entry after the first version entry
    if version_match:
        insert_pos = content.find(version_match.group(0))
        new_content = content[:insert_pos] + new_entry + content[insert_pos:]
    else:
        new_content = content + new_entry
    
    # Write updated changelog
    with open(changelog_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated CHANGELOG.md with version {new_version}")

if __name__ == "__main__":
    update_changelog() 