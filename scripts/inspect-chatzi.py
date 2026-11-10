from pathlib import Path
s=Path("index.html").read_text()
for term in ["chatziZuzAwards","pendingChatzi","chatziEarned","chatziZuzDistributed","function settings","function settingsPage","page==='settings'","const defaults=","function renderSettings","case 'settings'","chatziZuz"]:
 print("\nTERM",term)
 start=0
 for i in range(40):
  k=s.find(term,start)
  if k<0:break
  if k>9000000:print(k,repr(s[max(0,k-200):k+300]))
  start=k+len(term)
