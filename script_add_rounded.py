filepath = r"c:\Users\chitr\Downloads\my websites\Whitehouse homstay\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the closing of the class string before data-carousel with the rounded class
html = html.replace(' cursor-pointer" data-carousel="true"', ' cursor-pointer rounded-[16px]" data-carousel="true"')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
