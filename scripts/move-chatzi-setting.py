from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
block='''`<div class="panel"><h2>Chatzi Zuz Bonus</h2><p class="muted">Optional bonus for every three rank promotions. Default: Off. Switching off pauses new awards and hides bonus reminders; previously recorded bonuses are retained.</p><div class="actions">${button(db.chatziZuzEnabled?'Chatzi Zuz: ON — Turn Off':'Chatzi Zuz: OFF — Turn On','toggleChatziZuz',db.chatziZuzEnabled?'':'secondary')}</div></div>`'''
assert s.count(block)==1,('bonus panel count',s.count(block))
start=s.index("if(page==='settings'){")
end=s.index("\nhtml+='</main>",start)
section=s[start:end]
assert section.count(block)==1
assert section.count("New HTML versions retain them when opened in the same browser and storage context.")==1
section=section.replace("+"+block+"+","+",1)
tail="Local browser storage is not guaranteed permanent.</p></div>`;"
assert section.count(tail)==1
section=section.replace(tail,"Local browser storage is not guaranteed permanent.</p></div>`+"+block+";",1)
s=s[:start]+section+s[end:]
p.write_text(s,encoding='utf-8')
print('Moved Chatzi Zuz settings panel to bottom')
