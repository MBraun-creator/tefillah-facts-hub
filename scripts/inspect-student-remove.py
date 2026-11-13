from pathlib import Path
s=Path('index.html').read_text()
for needle in ["'Remove'","\`Remove\`","Student Profiles","removeStudent","deleteStudent","if(page==='students')","if(page==='profiles')","Manage Students"]:
 print('SEARCH',repr(needle),'COUNT',s.count(needle))
 start=0
 for i in range(min(s.count(needle),5)):
  at=s.find(needle,start)
  print(repr(s[max(0,at-450):at+550]))
  start=at+len(needle)
