#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open('fasteners.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Totaal aantal fasteners: {len(data)}")
print("\nEerste 20 fasteners:")
print("-" * 70)
for i, item in enumerate(data[:20], 1):
    print(f"{i}. {item['naam']} - €{item['prijs']} (EAN: {item.get('ean', 'N/A')})")

print("\n" + "=" * 70)
print("JSON structuur is correct!")
print("=" * 70)

