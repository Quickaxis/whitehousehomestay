import re

reviews_1_6 = [
    {"text": "The most peaceful stay I've had in years. Woke up to birdsong and fresh tea every morning.", "name": "Priya Nath", "loc": "Guwahati, Assam"},
    {"text": "Came for a weekend, wished I could stay a month. The garden terrace is divine.", "name": "Arjun Hazarika", "loc": "Jorhat, Assam"},
    {"text": "Best homestay in Dibrugarh, no contest. The colonial architecture is breathtaking.", "name": "Ananya Das", "loc": "Silchar, Assam"},
    {"text": "Our family of 5 stayed in the 4BHK — spacious, clean, and felt like home.", "name": "Sunita Gogoi", "loc": "Tezpur, Assam"},
    {"text": "The Brown Brick room had the most beautiful morning light. Slept better than ever.", "name": "Pooja Kalita", "loc": "Nagaon, Assam"},
    {"text": "Every corner is Instagram-worthy. But more importantly, genuinely comfortable.", "name": "Shreya Baruah", "loc": "Dibrugarh, Assam"},
]

reviews_7_11 = [
    {"text": "Clean, beautiful, affordable luxury. Sets the standard for homestays in Assam.", "name": "Dipankar Dutta", "loc": "Tinsukia, Assam"},
    {"text": "The hosts treated us like family from the moment we arrived.", "name": "Fatima Begum", "loc": "Guwahati, Assam"},
    {"text": "Felt like staying at a heritage home — warm, beautiful, full of character.", "name": "Rahul Bora", "loc": "Kolkata, West Bengal"},
    {"text": "A truly unique experience. You don't just stay here — you live here for a while.", "name": "Supriya Mohapatra", "loc": "Bhubaneswar, Odisha"},
    {"text": "A gem hidden in plain sight. Perfect for anyone looking for heritage and luxury.", "name": "Vikram Singh", "loc": "Delhi"},
]

def make_card(r):
    return f"""
        <div class="glass-card p-10 rounded-xl bg-white/60 border border-accent/20 w-[400px] flex-shrink-0">
          <div class="flex text-accent mb-4">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1">star</span>
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1">star</span>
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1">star</span>
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1">star</span>
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1">star</span>
          </div>
          <p class="text-primary text-lg font-display italic mb-6 leading-relaxed">"{r['text']}"</p>
          <div>
            <h4 class="font-bold text-primary">{r['name']}</h4>
            <p class="text-accent uppercase text-[10px] tracking-widest font-bold">{r['loc']}</p>
          </div>
        </div>"""

row1_cards = "".join(make_card(r) for r in reviews_1_6)
row1_html = f"""<div class="flex gap-8 animate-marquee-left w-max">
    <div class="flex gap-8">{row1_cards}</div>
    <div class="flex gap-8">{row1_cards}</div>
</div>"""

row2_cards = "".join(make_card(r) for r in reviews_7_11)
row2_html = f"""<div class="flex gap-8 animate-marquee-right w-max mt-8">
    <div class="flex gap-8">{row2_cards}</div>
    <div class="flex gap-8">{row2_cards}</div>
</div>"""

replacement = f"""  <!-- REVIEWS -->
  <section class="py-24 bg-off-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <h2 class="text-primary text-4xl md:text-5xl font-bold md:text-6xl">What Our Guests Say</h2>
      </div>
    </div>
    <div class="marquee-container relative w-full flex flex-col pt-4 pb-12">
      {row1_html}
      {row2_html}
    </div>
  </section>"""


with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# find REVIEWS section
start_marker = "  <!-- REVIEWS -->"
end_marker = "  <!-- BOOKING CTA -->"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + replacement + "\n" + html[end_idx:]
    
    # Also add styles
    style_idx = new_html.find("</style>")
    marquee_styles = """
    @keyframes marquee-left {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }
    @keyframes marquee-right {
      0% { transform: translateX(-50%); }
      100% { transform: translateX(0); }
    }
    .animate-marquee-left {
      animation: marquee-left 40s linear infinite;
    }
    .animate-marquee-right {
      animation: marquee-right 40s linear infinite;
    }
    .marquee-container:hover .animate-marquee-left,
    .marquee-container:hover .animate-marquee-right {
      animation-play-state: paused;
    }
"""
    new_html = new_html[:style_idx] + marquee_styles + new_html[style_idx:]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Review section replaced with marquee!")
else:
    print("Could not find section markers")
