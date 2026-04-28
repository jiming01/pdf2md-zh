// ({
//   katexConfig: {
//   "macros": {}
// },
  
//   mathjaxConfig: {
//   "tex": {},
//   "options": {},
//   "loader": {}
// },
  
//   mermaidConfig: {
//   "startOnLoad": false
// },
// })

({
  "mathRenderingOption": "MathJax",
  "mathjaxConfig": {
    "tex": {
      "inlineMath": [["$", "$"], ["\\(", "\\)"]],
      "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
      "processEscapes": true
    },
    "options": {
      "ignoreHtmlClass": "no-mathjax",
      "processHtmlClass": ".*"
    },
    "loader": {
      "load": ["[tex]/html"]
    }
  },
  "katexConfig": {
    "macros": {}
  },
  "mermaidConfig": {
    "startOnLoad": false
  }
})