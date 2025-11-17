#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re

html = open('index.html', encoding='utf-8').read()
match = re.search(r'<script id="DATA" type="application/json">(.*?)</script>', html, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    print(f'JSON correct gelezen: {len(data)} items')
    print(f'Eerste item: {data[0]["naam"]}')
    print(f'Laatste item: {data[-1]["naam"]}')
    print('JSON is geldig!')
else:
    print('DATA sectie niet gevonden!')

