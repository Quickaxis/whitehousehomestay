import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_marker = "  <!-- ROOMS -->"
end_marker = '  <!-- locations -->'
# Let's inspect the HTML
# The next section is : <section class="py-24 px-6 bg-off-white" id="locations">
end_marker = '  <section class="py-24 px-6 bg-off-white" id="locations">'

new_rooms = """  <!-- ROOMS -->
  <section class="py-[60px] px-[60px]" style="background-color: #1B3D2F;" id="rooms">
    <div class="max-w-7xl mx-auto">

      <div class="text-center mb-16">
        <h4 style="color: #C9A84C; text-transform: uppercase; font-size: 14px; font-weight: 700; letter-spacing: 0.15em; margin-bottom: 12px;">OUR SANCTUARY</h4>
        <h2 style="font-family: 'Cormorant Garamond', serif; color: #C9A84C; font-size: 52px; font-weight: 700;">Our Rooms</h2>
      </div>

      <!-- Masonry Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-start">
        
        <!-- Column 1 -->
        <div class="flex flex-col gap-4">
          <!-- The Cherryblossom -->
          <div class="group relative overflow-hidden rounded-lg w-full h-[380px] bg-[#FBCFE8] flex items-center justify-center cursor-pointer">
            <span class="material-symbols-outlined absolute z-0 text-[#1B3D2F]/20" style="font-size: 64px;">bed</span>
            <img src="" class="absolute inset-0 w-full h-full object-cover transition-transform duration-300 ease-in-out group-hover:scale-[1.04] opacity-0" alt="The Cherryblossom">
            
            <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent transition-colors duration-300 group-hover:bg-black/40 z-10"></div>
            
            <h3 class="absolute bottom-4 left-4 text-white font-bold z-20" style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">The Cherryblossom</h3>
            
            <div class="absolute bottom-4 right-4 bg-[#C9A84C] text-[#1B3D2F] px-3 py-1 rounded-full font-bold text-[12px] z-20">₹1,800 / night</div>
            
            <button class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#C9A84C]/90 text-[#1B3D2F] font-bold px-6 py-3 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-30 backdrop-blur-[4px]">
              Book Now &rarr;
            </button>
          </div>
          
          <!-- The Ocean Blue -->
          <div class="group relative overflow-hidden rounded-lg w-full h-[280px] bg-[#BFDBFE] flex items-center justify-center cursor-pointer">
            <span class="material-symbols-outlined absolute z-0 text-[#1B3D2F]/20" style="font-size: 64px;">waves</span>
            <img src="" class="absolute inset-0 w-full h-full object-cover transition-transform duration-300 ease-in-out group-hover:scale-[1.04] opacity-0" alt="The Ocean Blue">
            
            <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent transition-colors duration-300 group-hover:bg-black/40 z-10"></div>
            
            <h3 class="absolute bottom-4 left-4 text-white font-bold z-20" style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">The Ocean Blue</h3>
            
            <div class="absolute bottom-4 right-4 bg-[#C9A84C] text-[#1B3D2F] px-3 py-1 rounded-full font-bold text-[12px] z-20">₹4,700 / night</div>
            
            <button class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#C9A84C]/90 text-[#1B3D2F] font-bold px-6 py-3 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-30 backdrop-blur-[4px]">
              Book Now &rarr;
            </button>
          </div>
        </div>

        <!-- Column 2 -->
        <div class="flex flex-col gap-4">
          <!-- The Brown Brick -->
          <div class="group relative overflow-hidden rounded-lg w-full h-[260px] bg-[#DEB887] flex items-center justify-center cursor-pointer">
            <span class="material-symbols-outlined absolute z-0 text-[#1B3D2F]/20" style="font-size: 64px;">foundation</span>
            <img src="" class="absolute inset-0 w-full h-full object-cover transition-transform duration-300 ease-in-out group-hover:scale-[1.04] opacity-0" alt="The Brown Brick">
            
            <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent transition-colors duration-300 group-hover:bg-black/40 z-10"></div>
            
            <h3 class="absolute bottom-4 left-4 text-white font-bold z-20" style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">The Brown Brick</h3>
            
            <div class="absolute bottom-4 right-4 bg-[#C9A84C] text-[#1B3D2F] px-3 py-1 rounded-full font-bold text-[12px] z-20">₹1,800 / night</div>
            
            <button class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#C9A84C]/90 text-[#1B3D2F] font-bold px-6 py-3 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-30 backdrop-blur-[4px]">
              Book Now &rarr;
            </button>
          </div>

          <!-- The Orange Delight -->
          <div class="group relative overflow-hidden rounded-lg w-full h-[400px] bg-[#FDE68A] flex items-center justify-center cursor-pointer">
            <span class="material-symbols-outlined absolute z-0 text-[#1B3D2F]/20" style="font-size: 64px;">wb_sunny</span>
            <img src="" class="absolute inset-0 w-full h-full object-cover transition-transform duration-300 ease-in-out group-hover:scale-[1.04] opacity-0" alt="The Orange Delight">
            
            <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent transition-colors duration-300 group-hover:bg-black/40 z-10"></div>
            
            <h3 class="absolute bottom-4 left-4 text-white font-bold z-20" style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">The Orange Delight</h3>
            
            <div class="absolute bottom-4 right-4 bg-[#C9A84C] text-[#1B3D2F] px-3 py-1 rounded-full font-bold text-[12px] z-20">₹2,800 / night</div>
            
            <button class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#C9A84C]/90 text-[#1B3D2F] font-bold px-6 py-3 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-30 backdrop-blur-[4px]">
              Book Now &rarr;
            </button>
          </div>
        </div>

        <!-- Column 3 -->
        <div class="flex flex-col gap-4">
          <!-- The Green Monaco -->
          <div class="group relative overflow-hidden rounded-lg w-full h-[320px] bg-[#A7F3D0] flex items-center justify-center cursor-pointer">
            <span class="material-symbols-outlined absolute z-0 text-[#1B3D2F]/20" style="font-size: 64px;">park</span>
            <img src="" class="absolute inset-0 w-full h-full object-cover transition-transform duration-300 ease-in-out group-hover:scale-[1.04] opacity-0" alt="The Green Monaco">
            
            <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent transition-colors duration-300 group-hover:bg-black/40 z-10"></div>
            
            <h3 class="absolute bottom-4 left-4 text-white font-bold z-20" style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">The Green Monaco</h3>
            
            <div class="absolute bottom-4 right-4 bg-[#C9A84C] text-[#1B3D2F] px-3 py-1 rounded-full font-bold text-[12px] z-20">₹1,800 / night</div>
            
            <button class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#C9A84C]/90 text-[#1B3D2F] font-bold px-6 py-3 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-30 backdrop-blur-[4px]">
              Book Now &rarr;
            </button>
          </div>

          <!-- The Amazon -->
          <div class="group relative overflow-hidden rounded-lg w-full h-[340px] bg-[#6EE7B7] flex items-center justify-center cursor-pointer">
            <span class="material-symbols-outlined absolute z-0 text-[#1B3D2F]/20" style="font-size: 64px;">forest</span>
            <img src="" class="absolute inset-0 w-full h-full object-cover transition-transform duration-300 ease-in-out group-hover:scale-[1.04] opacity-0" alt="The Amazon">
            
            <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent transition-colors duration-300 group-hover:bg-black/40 z-10"></div>
            
            <h3 class="absolute bottom-4 left-4 text-white font-bold z-20" style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">The Amazon</h3>
            
            <div class="absolute bottom-4 right-4 bg-[#C9A84C] text-[#1B3D2F] px-3 py-1 rounded-full font-bold text-[12px] z-20">₹6,000 / night</div>
            
            <button class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#C9A84C]/90 text-[#1B3D2F] font-bold px-6 py-3 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-30 backdrop-blur-[4px]">
              Book Now &rarr;
            </button>
          </div>
        </div>

      </div>

      <!-- Pricing Note -->
      <div class="text-center mt-12 mb-8">
        <p style="color: #C9A84C; font-size: 14px; font-style: italic; letter-spacing: 0.05em;">
          2 BHK for birthdays &amp; parties from ₹3,300 &middot; 4 BHK group stays from ₹6,000 &middot; Call us for
          custom bookings.
        </p>
      </div>

    </div>
  </section>
"""

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_rooms + html[end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Success")
else:
    print(f"Failed. Start: {start_idx}, End: {end_idx}")
