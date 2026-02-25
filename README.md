# antiautorun

A custom JavaScript snippet for VS Code that automatically clicks the "Run" button (e.g., in AI chat panels) when it becomes available.

## Installation

Because standard VS Code extensions cannot access the UI DOM directly, this script must be loaded using a UI customization extension.

### Installation Steps

1. Install the [Custom CSS and JS Loader](https://marketplace.visualstudio.com/items?itemName=be5invis.vscode-custom-css) extension.
2. Open your VS Code `settings.json`.
3. Add the absolute path to `script.js` with the `file:///` prefix:

```json
{
    "vscode_custom_css.imports": [
        "file:///g:/projects/autoantirun/script.js"
    ]
}
```
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