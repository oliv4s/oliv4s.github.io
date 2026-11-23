(function(){
  const root = document.documentElement;
  const button = document.querySelector('.theme-switch');
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  function getTheme() { return root.dataset.theme || (media.matches ? 'dark' : 'light'); }
  function update() { if(button){const t=getTheme();button.setAttribute('aria-label','Switch to '+(t==='dark'?'light':'dark')+' theme');button.setAttribute('aria-pressed',String(t==='dark'));}}
  if(button) button.addEventListener('click',()=>{const t=getTheme()==='dark'?'light':'dark';root.dataset.theme=t;try{localStorage.setItem('nb-theme',t)}catch(e){}update()});
  if(media.addEventListener)media.addEventListener('change',update);
  update();
})();

(function(){
 const stages=[...document.querySelectorAll('.journey-node')];
 if(!stages.length)return;
 const number=document.getElementById('journey-active-index');
 const years=document.getElementById('journey-active-years');
 const title=document.getElementById('journey-active-title');
 const description=document.getElementById('journey-active-description');
 function choose(stage){
   stages.forEach(node=>{const active=node===stage;node.classList.toggle('is-active',active);node.setAttribute('aria-pressed',String(active));});
   number.innerHTML='';
   number.appendChild(document.createTextNode(stage.dataset.index));
   const suffix=document.createElement('span');suffix.textContent=' / 05';number.append(suffix);
   years.textContent=stage.dataset.years+' / '+stage.dataset.company;
   title.textContent=stage.dataset.title;
   description.textContent=stage.dataset.description;
 }
 if(window.matchMedia('(max-width: 780px)').matches) choose(stages[0]);
 stages.forEach((stage,i)=>{
   stage.addEventListener('click',()=>choose(stage));
   stage.addEventListener('keydown',(e)=>{
     let next=e.key==='ArrowRight'||e.key==='ArrowDown'?i+1:e.key==='ArrowLeft'||e.key==='ArrowUp'?i-1:null;
     if(next===null)return;
     e.preventDefault();const target=stages[(next+stages.length)%stages.length];choose(target);target.focus();
   });
 });
})();

// Use local wordmarks if a remote official asset is unreachable.
document.querySelectorAll('img.brand-img[data-fallback]').forEach((img)=>{
  img.addEventListener('error',()=>{
    const fallback=img.dataset.fallback;
    if(fallback && img.getAttribute('src')!==fallback){img.src=fallback;}
  });
  if (img.complete && img.naturalWidth === 0) {
    const fallback=img.dataset.fallback;
    if(fallback && img.getAttribute('src')!==fallback) img.src=fallback;
  }
});
