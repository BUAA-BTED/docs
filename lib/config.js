document$.subscribe(() => { hljs.highlightAll() })
document$.subscribe(() => {
    renderMathInElement(document.body, {
        delimiters: [
            { left: '\\[', right: '\\]', display: true },
            { left: '\\(', right: '\\)', display: false }
        ]
    })
})