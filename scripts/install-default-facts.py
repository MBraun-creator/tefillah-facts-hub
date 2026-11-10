from pathlib import Path
p=Path("index.html")
s=p.read_text(encoding="utf-8")
marker="/* TEFILLAH_DEFAULT_FACTS_V1 */"
if marker in s:
    print("Already installed")
    raise SystemExit(0)
old="const defaults=()=>({title:'Jerusalem Tefillah',facts:[]"
new="const NEW_TEACHER_FACTS_INSTALL=!localStorage.getItem(KEY);const defaults=()=>({title:'Jerusalem Tefillah',facts:[]"
assert s.count(old)==1, "Initialization signature changed; refusing to patch"
s=s.replace(old,new,1)
old="render();requestAnimationFrame(fitLeaderboard);if(!localStorage.getItem('tefillahWelcomeV50')"
new="""render();requestAnimationFrame(fitLeaderboard);
/* TEFILLAH_DEFAULT_FACTS_V1 */
if(NEW_TEACHER_FACTS_INSTALL){
  fetch('./tefillah_facts_default_100.json',{cache:'no-store'})
    .then(r=>{if(!r.ok)throw Error('Default facts unavailable');return r.json()})
    .then(facts=>{
      if(!Array.isArray(facts)||facts.length!==100||!facts.every(f=>f.id&&typeof f.text==='string'))throw Error('Invalid default facts');
      const stored=localStorage.getItem(KEY);
      if(stored){try{const previous=JSON.parse(stored);if((previous.facts||[]).length||(previous.students||[]).length)return}catch{return}}
      if(db.facts.length||db.students.length)return;
      db.facts=facts.map(f=>({id:f.id,text:f.text,order:f.order,unlocked:false,archived:false}));
      save();render();
    }).catch(e=>console.warn('Default facts were not loaded:',e));
}
if(!localStorage.getItem('tefillahWelcomeV50')"""
assert s.count(old)==1, "Startup signature changed; refusing to patch"
s=s.replace(old,new,1)
p.write_text(s,encoding="utf-8")
print("Patched new-teacher defaults")
