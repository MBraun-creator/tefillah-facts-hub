from pathlib import Path
p=Path("index.html")
s=p.read_text(encoding="utf-8")
start=s.index("const NEW_TEACHER_FACTS_INSTALL=!localStorage.getItem(KEY);")
s=s[:start]+s[start:].replace("const NEW_TEACHER_FACTS_INSTALL=!localStorage.getItem(KEY);","",1)
start=s.index("/* TEFILLAH_DEFAULT_FACTS_V1 */")
end=s.index("if(!localStorage.getItem('tefillahWelcomeV50')",start)
replacement="""/* TEFILLAH_DEFAULT_FACTS_V2 */
if(!db.facts.length && !localStorage.getItem('tefillahDefaultFactsImportedV2')){
  fetch('./tefillah_facts_default_100.json',{cache:'no-store'})
    .then(r=>{if(!r.ok)throw Error('Default facts unavailable');return r.json()})
    .then(facts=>{
      if(!Array.isArray(facts)||facts.length!==100||!facts.every(f=>f.id&&typeof f.text==='string'))throw Error('Invalid default facts');
      if(db.facts.length)return;
      db.facts=facts.map((f,i)=>({...f,order:Number.isFinite(Number(f.order))?Number(f.order):i+1,unlocked:false,archived:false}));
      localStorage.setItem('tefillahDefaultFactsImportedV2','1');
      save();render();
    }).catch(e=>console.warn('Default facts were not loaded:',e));
}
"""
s=s[:start]+replacement+s[end:]
p.write_text(s,encoding="utf-8")
print("Fixed loading for previously initialized empty fact libraries")
