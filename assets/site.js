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
