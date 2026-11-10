from pathlib import Path
s=Path("index.html").read_text()
for term in ["if(page==='settings')","if(a==='saveSettings')","if(a==='settings')","if(a==='toggle","function save()","function render()","if(a==='saveTitle')"]:
 k=s.find(term,9000000)
 print("\nTERM",term,"OFFSET",k,"\n",repr(s[k:k+5000] if k>=0 else ''))
