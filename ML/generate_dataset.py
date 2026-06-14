import pandas as pd
import random

samples = []

# ---------- VALID HTML ----------
valid_html = [
    "<h1>Hello</h1>",
    "<p>Welcome</p>",
    "<div>Content</div>",
    "<span>Text</span>",
    "<h2>Heading</h2>",
    "<button>Click</button>",
    "<ul><li>Item</li></ul>",
    "<section><p>Paragraph</p></section>",
    "<table><tr><td>Data</td></tr></table>"
]

# ---------- INVALID HTML ----------
invalid_html = [
    "<h1>Hello",
    "<p>Welcome",
    "<div>Content",
    "<span>Text",
    "<h2>Heading",
    "<button>Click",
    "<ul><li>Item</ul>",
    "<section><p>Paragraph</section>",
    "<table><tr><td>Data</tr></table>"
]

# ---------- VALID JS ----------
valid_js = [
    "console.log('Hello');",
    "alert('Welcome');",
    "let x = 10;",
    "const name = 'John';",
    "function greet(){ return 'Hi'; }",
    "if(true){ console.log('ok'); }",
    "for(let i=0;i<5;i++){ console.log(i); }",
    "let arr=[1,2,3];",
    "document.write('Hello');"
]

# ---------- INVALID JS ----------
invalid_js = [
    "console.log('Hello'",
    "alert('Welcome'",
    "let x = ;",
    "const name = ",
    "function greet( { return 'Hi'; }",
    "if(true) console.log('ok'",
    "for(let i=0;i<5;i++ { console.log(i); }",
    "let arr=[1,2,3;",
    "document.write('Hello'"
]

# ---------- VALID CSS ----------
valid_css = [
    "h1{color:red;}",
    "body{background:white;}",
    "p{font-size:16px;}",
    ".box{padding:10px;}",
    "#title{text-align:center;}"
]

# ---------- INVALID CSS ----------
invalid_css = [
    "h1{color:red;",
    "body{background:white;",
    "p{font-size:16px;",
    ".box{padding:10px;",
    "#title{text-align:center;"
]

# Generate many samples
for _ in range(350):
    samples.append([random.choice(valid_html), "no_error"])

for _ in range(350):
    samples.append([random.choice(invalid_html), "error"])

for _ in range(150):
    samples.append([random.choice(valid_js), "no_error"])

for _ in range(150):
    samples.append([random.choice(invalid_js), "error"])

for _ in range(100):
    samples.append([random.choice(valid_css), "no_error"])

for _ in range(100):
    samples.append([random.choice(invalid_css), "error"])

random.shuffle(samples)

df = pd.DataFrame(samples, columns=["code", "label"])

df.to_csv("dataset.csv", index=False)

print("Dataset generated successfully!")
print("Total samples:", len(df))