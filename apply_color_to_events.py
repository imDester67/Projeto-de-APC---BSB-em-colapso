# script para substituir prints de eventos por print_event quando apropriado
import re
p = r"logica_brasilia.py"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    s = f.read()

# inserir função print_event após imports (após the last import line)
insert_marker = "from colorama import Fore, Back, Style, init\n"
if insert_marker in s:
    helper = "\n\ndef print_event(block):\n    try:\n        init()\n    except Exception:\n        pass\n    for raw in block.splitlines():\n        line = raw.rstrip()\n        if line.strip().endswith('+'):\n            print(Fore.GREEN + line + Fore.WHITE)\n        elif line.strip().endswith('-'):\n            print(Fore.RED + line + Fore.WHITE)\n        else:\n            print(line)\n\n"
    if 'def print_event(' not in s:
        s = s.replace(insert_marker, insert_marker + helper)

# regex to find print blocks: print( ... ) capturing balanced parentheses naive: find "print(" then until the next line that starts with 10 spaces and ")" or a line with ")" and optional spaces
# We'll do a simpler approach: find occurrences of "print(" followed by lines until a line with only spaces and ")" or a line that ends with ")"
pattern = re.compile(r"print\([\s\S]{0,1000}?\)\n", re.M)

replacements = 0

def should_replace(block):
    # choose blocks that contain 'Efeitos:' and do NOT contain 'Fore.'
    return ('Efeitos:' in block) and ('Fore.' not in block)

new_s = s
for m in pattern.finditer(s):
    block = m.group(0)
    if should_replace(block):
        new_block = block.replace('print(', 'print_event(', 1)
        new_s = new_s.replace(block, new_block, 1)
        replacements += 1

if replacements:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(new_s)
print(f"Feito: {replacements} substituições")
