# antiautorun

A custom JavaScript snippet for VS Code that automatically clicks the "Run" button (e.g., in AI chat panels) when it becomes available.

## Installation

Because standard VS Code extensions cannot access the UI DOM directly, this script must be loaded using a UI customization extension.

### Method: Using APC Customize UI++

1. Install the [APC Customize UI++](https://marketplace.visualstudio.com/items?itemName=drcika.apc-extension) extension in VS Code.
2. Open your VS Code `settings.json`.
3. Add the absolute path to `script.js` in the `apc.imports` array:

```json
{
    "apc.imports": [
        "file:///g:/projects/autoantirun/script.js"
    ]
}
```
*(Make sure to adjust the path if you move this repository! Use `file:///` followed by the absolute path with forward slashes).*

4. Save `settings.json` and restart VS Code.

### How it works

The script runs a recurring check (`setInterval`) every 1 second. It looks for a `<button>` element that:
- Contains the text "Run"
- Contains the text "Alt+⏎"
- Has the specific CSS classes `bg-primary` and `text-primary-foreground`
- Is **not** `disabled`

If it finds a matching button that is enabled, it clicks it.