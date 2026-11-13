from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
def one(a,b):
 global s
 assert s.count(a)==1,(a[:90],s.count(a))
 s=s.replace(a,b,1)
one('<button class="roster-delete" data-action="rosterDelete:${s.id}" title="Delete ${esc(name(s))}">✕ Remove</button>','')
one("${button('Delete Student','deleteStudent','danger')}",'')
one("${button('Add Student','addStudent','')}${button('Import / Replace Roster CSV','importRoster')}","${button('Add Student','addStudent','')}${button('Manage / Remove Students','manageStudents','secondary')}${button('Import / Replace Roster CSV','importRoster')}")
needle="function action(a){if(a.startsWith('rosterDelete:'))"
insert="""function action(a){/* STUDENT_DELETE_SETTINGS_V1 */if(a==='manageStudents'){show(`<h2>Manage / Remove Students</h2><p class="muted">Deleting a student permanently removes their current-year progress. Each removal requires confirmation.</p><div class="student-management-list">${[...active()].sort(byName).map(s=>`<div class="row"><strong>${esc(name(s))}</strong><button class="btn danger" data-action="rosterDelete:${s.id}">Remove</button></div>`).join('')||'<p>No students in the roster.</p>'}</div><p>${button('Close','close','secondary')}</p>`);return}if(a.startsWith('rosterDelete:'))"""
one(needle,insert)
p.write_text(s,encoding='utf-8')
print('Moved student removal into Settings > Students.')
