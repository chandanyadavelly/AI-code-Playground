function runCode() {

    let html = document.getElementById("htmlCode").value;
    let css = document.getElementById("cssCode").value;
    let js = document.getElementById("jsCode").value;

    let output = document.getElementById("output");

    output.srcdoc = `
        <html>
        <head>
            <style>${css}</style>
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

    document.getElementById("htmlCode").value = "";
    document.getElementById("cssCode").value = "";
    document.getElementById("jsCode").value = "";

    document.getElementById("output").srcdoc = "";
}