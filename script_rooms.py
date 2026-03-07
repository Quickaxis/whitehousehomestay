import re

html_file = r"c:\Users\chitr\Downloads\my websites\Whitehouse homstay\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

rooms = [
    {
        "name": "The Cherryblossom",
        "bg_color": "#FBCFE8",
        "icon": "bed",
        "tagline_height": "h-[380px]",
        "images": [
            "gallery/CHEERY COLOUR - CHERRY BLOOSOM/94a41c2e-9aa7-4642-9a7f-2f199d821c1a.jpg",
            "gallery/CHEERY COLOUR - CHERRY BLOOSOM/86112cd9-29ff-42bd-b35b-9fb11b75abf3.jpg",
            "gallery/CHEERY COLOUR - CHERRY BLOOSOM/bbe2e2d3-7b35-4b65-a1f6-55cce451bd99.jpg"
        ]
    },
    {
        "name": "The Ocean Blue",
        "bg_color": "#BFDBFE",
        "icon": "waves",
        "tagline_height": "h-[280px]",
        "images": [
            "gallery/BLUE ROOM - THE OCEAN BLUE/4243ec0c-aba4-42bc-babc-f983d4773909.jpg",
            "gallery/BLUE ROOM - THE OCEAN BLUE/c8731749-c277-45a3-abad-66f4fd890366.jpg",
            "gallery/BLUE ROOM - THE OCEAN BLUE/e1fbd6cc-43f4-4f47-b04a-f59d5c2166d8.jpg"
        ]
    },
    {
        "name": "The Brown Brick",
        "bg_color": "#DEB887",
        "icon": "foundation",
        "tagline_height": "h-[260px]",
        "images": [
            "gallery/BROWN ROOM - THE BROWN BRICK/c26d0fa4-2a56-4246-a980-018cd4058f68.jpg",
            "gallery/BROWN ROOM - THE BROWN BRICK/255b06dd-bdd4-4691-98c4-930208884226.jpg",
            "gallery/BROWN ROOM - THE BROWN BRICK/6ad40a8a-9ea5-4568-9ace-06e1ad8d5cca.jpg"
        ]
    },
    {
        "name": "The Orange Delight",
        "bg_color": "#FDE68A",
        "icon": "wb_sunny",
        "tagline_height": "h-[400px]",
        "images": [
            "gallery/ORANGE ROOM - THE ORANGE DELIGHT/c99a2f77-2163-4a78-9523-3cf737eade08.jpg",
            "gallery/ORANGE ROOM - THE ORANGE DELIGHT/5ffa2c65-ee1e-49ae-87e7-6c058481707e.jpg",
            "gallery/ORANGE ROOM - THE ORANGE DELIGHT/4d553072-ed31-4386-9ef7-53d0b7474645.jpg"
        ]
    },
    {
        "name": "The Green Monaco",
        "bg_color": "#A7F3D0",
        "icon": "park",
        "tagline_height": "h-[320px]",
        "images": [
            "gallery/GREEN ROOM - THE  GREEN MONACO/604e242f-08b9-44b8-97a3-ecccf167a8fc.jpg",
            "gallery/GREEN ROOM - THE  GREEN MONACO/76e844fd-a4dc-4469-bb24-e03ffafb670c.jpg",
            "gallery/GREEN ROOM - THE  GREEN MONACO/ae7f943e-f562-47aa-a836-c0717d7080d9.jpg"
        ]
    },
    {
        "name": "The Amazon",
        "bg_color": "#6EE7B7",
        "icon": "forest",
        "tagline_height": "h-[340px]",
        "images": [
            "gallery/GREEN AND BADGE  - THE AMAZON/d6a40c8a-ec87-4ec4-a5e8-084f8f0ad5e3.jpg",
            "gallery/GREEN AND BADGE  - THE AMAZON/1d3a2091-54c0-4080-856f-0797136fc036.jpg",
            "gallery/GREEN AND BADGE  - THE AMAZON/34cc6179-d5bf-4971-be6d-606b58f4c566.jpg"
        ]
    }
]

for room in rooms:
    # Pattern to match the existing container for the room
    # We are looking to replace the height and the inner img tag
    
    room_pattern = re.compile(
        rf'<div\s+class="group relative overflow-hidden w-full {re.escape(room["tagline_height"])} bg-\[{room["bg_color"]}\] flex items-center justify-center cursor-pointer">(.*?)<img src=""\s*.*?alt="{room["name"]}">(.*?)</div>\s*<!--',
        re.DOTALL
    )
    
    # Alternatively, just search and replace explicitly based on the text block
    old_start = f"""          <div
            class="group relative overflow-hidden w-full {room['tagline_height']} bg-[{room['bg_color']}] flex items-center justify-center cursor-pointer">
            <span class="material-symbols-outlined absolute z-0 text-[#1B3D2F]/20" style="font-size: 64px;">{room['icon']}</span>
            <img src=""
              class="absolute inset-0 w-full h-full object-cover transition-transform duration-300 ease-in-out group-hover:scale-[1.04] opacity-0"
              alt="{room['name']}">"""
    
    new_start = f"""          <div
            class="group relative overflow-hidden w-full bg-[{room['bg_color']}] cursor-pointer">
            <span class="material-symbols-outlined absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-0 text-[#1B3D2F]/20" style="font-size: 64px; pointer-events:none;">{room['icon']}</span>
            
            <div class="w-full flex flex-col gap-[3px] transition-transform duration-300 ease-in-out group-hover:scale-[1.04] relative z-10 pointer-events-none">
              <img src="{room['images'][0]}" class="w-full h-[220px] object-cover block" style="background-color: {room['bg_color']};" alt="{room['name']} 1">
              <img src="{room['images'][1]}" class="w-full h-[180px] object-cover block" style="background-color: {room['bg_color']};" alt="{room['name']} 2">
              <img src="{room['images'][2]}" class="w-full h-[160px] object-cover block" style="background-color: {room['bg_color']};" alt="{room['name']} 3">
            </div>"""
    
    # We need to find the exact old_start but whitespace may vary, let's just use re
    pattern = rf'<div[^>]*class="group relative overflow-hidden w-full {re.escape(room["tagline_height"])} bg-\[{room["bg_color"]}\] flex items-center justify-center cursor-pointer">\s*<span class="material-symbols-outlined absolute z-0 text-\[#1B3D2F\]/20"[^>]*>{room["icon"]}</span>\s*<img src=""[^>]*alt="{room["name"]}">\s*'
    
    def repl(m):
        return new_start + "\n\n"
        
    html = re.sub(pattern, repl, html)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Rooms updated")
