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