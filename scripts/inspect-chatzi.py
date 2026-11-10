from pathlib import Path
s=Path("index.html").read_text(encoding="utf-8")
for term in ["Chatzi","chatzi","zuz","Zuz","function settings","page==='settings'","const defaults="]:
 print("\n=== ",term," count ",s.lower().count(term.lower()))
 pos=0
 for i in range(min(s.lower().count(term.lower()),12)):
  j=s.lower().find(term.lower(),pos)
  print("MATCH",i,"OFFSET",j,"CONTEXT",repr(s[max(0,j-380):j+480]))
  pos=j+len(term)
