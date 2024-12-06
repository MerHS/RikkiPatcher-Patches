from pathlib import Path
import json

ext = Path('./extract')
chn = Path('./migration/dialogues')
if not ext.exists():
    ext.mkdir()

for f in chn.iterdir():
    j = json.loads(f.read_text('utf-8'))
    items = j['list']
    if items is None:
        continue
    lines = []
    for k in range(len(items)):
        item = items[str(k)]
        s, d = item['speaker'], item['dialogue']
        line = f'{s}: "{d}"' if s else d
        lines.append(line)

    fe = ext / (f.stem + '.txt')
    with fe.open('w', encoding='utf-8') as fx:
        fx.write('\n'.join(lines))