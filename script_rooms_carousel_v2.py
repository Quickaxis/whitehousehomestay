import re

filepath = r'c:\Users\chitr\Downloads\my websites\Whitehouse homstay\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

heights = {
    "The Cherryblossom": "h-[380px]",
    "The Ocean Blue": "h-[280px]",
    "The Brown Brick": "h-[260px]",
    "The Orange Delight": "h-[400px]",
    "The Green Monaco": "h-[320px]",
    "The Amazon": "h-[340px]"
}

pattern = re.compile(r'<div class="group relative overflow-hidden w-full (bg-\[#[A-F0-9a-f]+\]) cursor-pointer">\s*<span class="material-symbols-outlined.*?>([^<]+)</span>\s*<div\s*class="w-full flex flex-col gap-\[3px\].*?">\s*<img src="([^"]+)"[^>]*alt="([^"]+) 1">\s*<img src="([^"]+)"[^>]*>\s*<img src="([^"]+)"[^>]*>\s*</div>', re.DOTALL)

def repl(match):
    bg_color_class = match.group(1)
    icon = match.group(2)
    img1 = match.group(3)
    name = match.group(4)
    img2 = match.group(5)
    img3 = match.group(6)
    
    height_class = heights.get(name, "h-[300px]")
    
    return f"""<div class="group relative overflow-hidden w-full {height_class} {bg_color_class} cursor-pointer" data-carousel="true" data-index="0">
            <span class="material-symbols-outlined absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-0 text-[#1B3D2F]/20" style="font-size: 64px; pointer-events:none;">{icon}</span>

            <div class="carousel-inner w-full h-full relative z-10 flex transition-transform duration-300 ease-in-out group-hover:scale-[1.04] pointer-events-none">
              <img src="{img1}" class="w-full h-full object-cover flex-shrink-0 block" alt="{name} 1">
              <img src="{img2}" class="w-full h-full object-cover flex-shrink-0 block" alt="{name} 2">
              <img src="{img3}" class="w-full h-full object-cover flex-shrink-0 block" alt="{name} 3">
            </div>

            <button class="prev-btn absolute left-2 top-1/2 -translate-y-1/2 z-40 text-white bg-black/20 hover:bg-black/40 rounded-full p-1 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center" onclick="moveCarousel(event, this, -1)">
              <span class="material-symbols-outlined" style="font-size: 20px;">chevron_left</span>
            </button>
            <button class="next-btn absolute right-2 top-1/2 -translate-y-1/2 z-40 text-white bg-black/20 hover:bg-black/40 rounded-full p-1 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center" onclick="moveCarousel(event, this, 1)">
              <span class="material-symbols-outlined" style="font-size: 20px;">chevron_right</span>
            </button>
            
            <div class="absolute bottom-[60px] left-0 right-0 z-40 flex justify-center gap-1.5 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
               <div class="dot w-1.5 h-1.5 rounded-full bg-[#C9A84C] transition-colors"></div>
               <div class="dot w-1.5 h-1.5 rounded-full bg-white/50 transition-colors"></div>
               <div class="dot w-1.5 h-1.5 rounded-full bg-white/50 transition-colors"></div>
            </div>"""

new_content = pattern.sub(repl, content)

script_html = """
  <!-- Carousel Script -->
  <script>
    function moveCarousel(e, btn, dir) {
      e.stopPropagation();
      e.preventDefault();
      const card = btn.closest('.group');
      const inner = card.querySelector('.carousel-inner');
      const dots = card.querySelectorAll('.dot');
      let idx = parseInt(card.getAttribute('data-index') || '0');
      idx += dir;
      if (idx < 0) idx = 2;
      if (idx > 2) idx = 0;
      card.setAttribute('data-index', idx);
      inner.style.transform = `translateX(-${idx * 100}%)`;
      dots.forEach((d, i) => {
        d.classList.toggle('bg-[#C9A84C]', i === idx);
        d.classList.toggle('bg-white/50', i !== idx);
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.group[data-carousel="true"]').forEach(card => {
        let startX = 0;
        card.addEventListener('touchstart', e => { startX = e.touches[0].clientX; }, {passive: true});
        card.addEventListener('touchend', e => {
          let endX = e.changedTouches[0].clientX;
          if (startX - endX > 30) moveCarousel(e, card.querySelector('.next-btn'), 1);
          else if (endX - startX > 30) moveCarousel(e, card.querySelector('.prev-btn'), -1);
        }, {passive: true});
      });
    });
  </script>
"""

if "<!-- Carousel Script -->" not in new_content:
    new_content = new_content.replace('</body>', script_html + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Carousel added successfully")
