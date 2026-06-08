import os
import re
import json
import time

# Configuration paths
STAGING_FILE = "agent_output.txt"
TARGET_DIR = "src/content/pmp-questions"

def slugify(text):
    """Converts a question title into a clean URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    return re.sub(r'[\s-]+', '-', text).strip('-')

def process_handoff():
    if not os.path.exists(STAGING_FILE):
        return

    print(f"🔄 Clear token detected in {STAGING_FILE}. Ingesting payload...")
    
    with open(STAGING_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Locate the trigger boundaries
    if "READY_FOR_EXECUTION" not in content:
        return

    # Extract the title from the markdown frontmatter to build a clean file name
    title_match = re.search(r'^title:\s*["\']?(.*?)["\']?$', content, re.MULTILINE)
    if title_match:
        title_str = title_match.group(1)
        filename = f"{slugify(title_str)}.md"
    else:
        filename = f"pmp-scenario-{int(time.time())}.md"

    target_path = os.path.join(TARGET_DIR, filename)

    # Clean up the output string (strip handoff wrappers if present)
    clean_content = re.sub(r'```token-handoff.*?```', '', content, flags=re.DOTALL).strip()

    # Write the file directly to your Astro collection
    os.makedirs(TARGET_DIR, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as out:
        out.write(clean_content)

    print(f"✅ Success! Generated content file: {target_path}")
    
    # Wipe the staging file so it's fresh for the next automation loop
    os.remove(STAGING_FILE)

if __name__ == "__main__":
    print("🚀 Logic Router Automation Listener running. Waiting for agent outputs...")
    while True:
        if os.path.exists(STAGING_FILE):
            process_handoff()
        time.sleep(2)