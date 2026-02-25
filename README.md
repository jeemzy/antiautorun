# antiautorun

A custom JavaScript snippet for VS Code that automatically clicks the "Run" button (e.g., in AI chat panels) when it becomes available.

## Installation

Because standard VS Code extensions cannot access the UI DOM directly, this script must be loaded using a UI customization extension.

### Installation Steps

0. Download the [script.js](https://github.com/jeemzy/antiautorun/blob/f1138afb49dc245e99f91849ff057bc9a23dff80/script.js)
1. Install the [Custom CSS and JS](https://github.com/jeemzy/antiautorun/blob/d8ab5274dc5beeb3244314ada3b652de4f409504/vscode-custom-css-7.5.0.vsix) extension.
2. Open your VS Code `settings.json`.
3. Add the absolute path to `script.js` with the `file:///` prefix:

```json
{
    "vscode_custom_css.imports": [
        "file:///C:/path/to/script.js"
    ]
}
```
*(Make sure to use the absolute path to `script.js` with the `file:///` prefix and forward slashes).*
4. **CRITICAL:** You must run VS Code **as Administrator** for the next step.
5. Open the Command Palette (`Ctrl+Shift+P`) and run **"Reload Custom CSS and JS"**.
6. Restart VS Code (you don't need to run as Administrator anymore after it's installed).

## How it works

The script runs a recurring check (`setInterval`) every 1 second. It looks for a `<button>` element that:
- Contains the text "Run"
- Contains the text "Alt+⏎"
- Has the specific CSS classes `bg-primary` and `text-primary-foreground`
- Is **not** `disabled`

If it finds a matching button that is enabled, it clicks it.
