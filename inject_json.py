#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject JSON data from fasteners.json into index.html DATA section
"""

import json
import re

# Read JSON data
with open('fasteners.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert to JSON string with proper formatting
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the empty array in the DATA script tag
# Pattern: <script id="DATA" type="application/json">[]</script>
pattern = r'(<script id="DATA" type="application/json">)\[\](\</script>)'
replacement = r'\1' + json_str + r'\2'

html_content = re.sub(pattern, replacement, html_content)

# Write back to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully injected {len(data)} fasteners into index.html")
print(f"JSON data size: {len(json_str)} characters")

