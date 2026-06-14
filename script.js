let htmlEditor;
let cssEditor;
let jsEditor;

require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(["vs/editor/editor.main"], function () {

    htmlEditor = monaco.editor.create(
        document.getElementById("htmlEditor"),
        {
            value: "<h1>Hello World</h1>",
            language: "html",
            theme: "vs-dark",
            automaticLayout: true
        }
    );

    cssEditor = monaco.editor.create(
        document.getElementById("cssEditor"),
        {
            value: "h1 {\n  color: red;\n}",
            language: "css",
            theme: "vs-dark",
            automaticLayout: true
        }
    );

    jsEditor = monaco.editor.create(
        document.getElementById("jsEditor"),
        {
            value: "console.log('Hello');",
            language: "javascript",
            theme: "vs-dark",
            automaticLayout: true
        }
    );

});
function runCode() {

    let html = htmlEditor.getValue();
    let css = cssEditor.getValue();
    let js = jsEditor.getValue();

    let output = document.getElementById("output");

    output.srcdoc = `
    <html>
    <head>
        <style>
        ${css}
        </style>
    </head>

    <body>

        ${html}

        <script>
        ${js}
        <\/script>

    </body>
    </html>
    `;
}

function clearCode() {

    htmlEditor.setValue("");
    cssEditor.setValue("");
    jsEditor.setValue("");

    document.getElementById("output").srcdoc = "";
}

async function checkErrors() {

    let html = htmlEditor.getValue();
    let css = cssEditor.getValue();
    let js = jsEditor.getValue();

    let code = html + "\n" + css + "\n" + js;

    let response = await fetch(
        "https://ai-code-playground.onrender.com/predict",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        }
    );

    let result = await response.json();

   if (result.prediction === "error") {

    let resultBox = document.getElementById("predictionResult");

    resultBox.innerText = "❌ Code Contains Errors";
    resultBox.style.color = "red";

} else {

    let resultBox = document.getElementById("predictionResult");

    resultBox.innerText = "✅ Error-Free Code";
    resultBox.style.color = "green";
}
}

async function debugWithAI() {

    let html = htmlEditor.getValue();
    let css = cssEditor.getValue();
    let js = jsEditor.getValue();

    let code = html + "\n" + css + "\n" + js;

    document.getElementById("aiSuggestion").innerHTML =
    "🤖 AI is analyzing your code...";

    let response = await fetch(
        "https://ai-code-playground.onrender.com/debug",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        }
    );

    let result = await response.json();

    document.getElementById("aiSuggestion").innerText =
        result.suggestion;
}

async function explainCode() {

    let html = htmlEditor.getValue();
    let css = cssEditor.getValue();
    let js = jsEditor.getValue();

    let code = html + "\n" + css + "\n" + js;

    document.getElementById("codeExplanation").innerHTML =
        "📖 AI is explaining your code...";

    let response = await fetch(
        "https://ai-code-playground.onrender.com/explain",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        }
    );

    let result = await response.json();

    document.getElementById("codeExplanation").innerText =
        result.explanation;
}