# Security Policy

text-to-animated-html generates self-contained HTML files. The security model is simple: the output must never make network requests.

## Security design

- All CSS, JS, and content is inlined in a single `.html` file.
- No `<script src>`, `<link href>`, or `@import url()` pointing to external resources.
- No `fetch()`, `XMLHttpRequest`, or WebSocket calls.
- No `eval()` or `Function()` constructor.
- Files work fully offline and are safe to open from `file://` protocol.

## Reporting

If you find a generated output that makes external network requests or executes unexpected code, open an issue with the prompt and HTML output that triggered it.
