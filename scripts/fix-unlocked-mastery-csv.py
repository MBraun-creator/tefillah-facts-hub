from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
old="if(a==='exportMasteryPercentCSV'){const total=availableCount();const rows="
new="if(a==='exportMasteryPercentCSV'){const total=db.facts.filter(f=>!f.archived&&f.unlocked).length;const rows="
assert s.count(old)==1,('export start',s.count(old))
s=s.replace(old,new,1)
old2="const count=activeMasteryCount(s);rows.push([s.first,s.last,count,total,total?(count/total*100).toFixed(1)+'%':'N/A'])"
new2="const count=db.facts.filter(f=>!f.archived&&f.unlocked&&mastered(s,f)).length;rows.push([s.first,s.last,count,total,total?(count/total*100).toFixed(1)+'%':'N/A'])"
assert s.count(old2)==1,('export count',s.count(old2))
s=s.replace(old2,new2,1)
p.write_text(s,encoding='utf-8')
print('CSV mastery percentage now uses only unlocked, nonarchived facts for numerator and denominator.')
