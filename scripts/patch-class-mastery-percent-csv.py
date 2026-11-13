from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='/* CLASS_MASTERY_PERCENT_CSV_V1 */'
assert marker not in s
old="${button('Export Progress CSV','exportCSV')}"
assert s.count(old)==1,('settings export button',s.count(old))
s=s.replace(old,old+"${button('Export Mastery Percentages CSV','exportMasteryPercentCSV','secondary')}",1)
needle="if(a==='exportCSV'){"
assert s.count(needle)==1,('CSV action',s.count(needle))
insert="""/* CLASS_MASTERY_PERCENT_CSV_V1 */if(a==='exportMasteryPercentCSV'){const total=availableCount();const rows=[['First Name','Last Name','Facts Mastered','Total Active Facts','Percentage Mastered']];[...active()].sort(byName).forEach(s=>{const count=activeMasteryCount(s);rows.push([s.first,s.last,count,total,total?(count/total*100).toFixed(1)+'%':'N/A'])});const csv='\\uFEFF'+rows.map(r=>r.map(v=>'"'+String(v??'').replace(/"/g,'""')+'"').join(',')).join('\\r\\n');download('tefillah_class_mastery_percentages.csv',csv,'text/csv');return}"""
s=s.replace(needle,insert+needle,1)
p.write_text(s,encoding='utf-8')
assert s.count(marker)==1
print('Added class mastery percentage CSV export for active students, using active facts as denominator.')
