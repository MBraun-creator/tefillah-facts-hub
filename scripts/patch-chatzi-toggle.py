from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
assert '/* CHATZI_ZUZ_TOGGLE_V1 */' not in s
def one(a,b):
 global s
 n=s.count(a)
 assert n==1,(a[:100],n)
 s=s.replace(a,b,1)
one("lastBackup:0});let db;try{","lastBackup:0,chatziZuzEnabled:false});let db;try{")
one("const chatziEarned=s=>[...new Set((s.chatziZuzAwards||[])","/* CHATZI_ZUZ_TOGGLE_V1 */const chatziEarned=s=>db.chatziZuzEnabled?[...new Set((s.chatziZuzAwards||[])")
one("].sort((a,b)=>a-b);const pendingRankPrizes=", "].sort((a,b)=>a-b):[];const pendingRankPrizes=")
one("if(now>0&&now%3===0){s.chatziZuzAwards=", "if(db.chatziZuzEnabled&&now>0&&now%3===0){s.chatziZuzAwards=")
one("<p>🪙 Chatzi Zuz earned: ${(s.chatziZuzAwards||[]).length}</p>"," ${db.chatziZuzEnabled?\`<p>🪙 Chatzi Zuz earned: ${(s.chatziZuzAwards||[]).length}</p>\`:''}")
one("if(page==='settings'){html+=\`<h1 class=\"heading\">Settings</h1>\`+", "if(page==='settings'){html+=\`<h1 class=\"heading\">Settings</h1>\`+\`<div class=\"panel\"><h2>Chatzi Zuz Bonus</h2><p class=\"muted\">Optional bonus for every three rank promotions. Default: Off. Switching off pauses new awards and hides bonus reminders; previously recorded bonuses are retained.</p><div class=\"actions\">${button(db.chatziZuzEnabled?'Chatzi Zuz: ON — Turn Off':'Chatzi Zuz: OFF — Turn On','toggleChatziZuz',db.chatziZuzEnabled?'':'secondary')}</div></div>\`+")
one("if(a==='saveTitle'){", "if(a==='toggleChatziZuz'){db.chatziZuzEnabled=!db.chatziZuzEnabled;save();render();return}if(a==='saveTitle'){")
p.write_text(s,encoding='utf-8')
print('Chatzi Zuz toggle patched; default off; old bonus records retained')
