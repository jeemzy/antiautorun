# antiautorun

A custom JavaScript snippet for VS Code that automatically clicks the "Run" button (e.g., in AI chat panels) when it becomes available.

## Installation

Because standard VS Code extensions cannot access the UI DOM directly, this script must be loaded using a UI customization extension.

If you encounter errors with one method, please try the other.

### Method 1: Using Custom CSS and JS Loader (Recommended Fallback)

If APC Customize UI++ gives you command errors, use this extension instead.

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

---

### Method 2: Using APC Customize UI++

*Note: If you see `command 'apc.extension.enable' not found`, it usually means the extension failed to activate because VS Code was not run as Administrator, or the extension is incompatible with your current VS Code version.*

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

4. Run VS Code **as Administrator** (required for the first time).
5. Open the Command Palette (`Ctrl+Shift+P`) and choose **"Enable Apc extension"**.
6. Restart VS Code.

## How it works

The script runs a recurring check (`setInterval`) every 1 second. It looks for a `<button>` element that:
- Contains the text "Run"
- Contains the text "Alt+⏎"
- Has the specific CSS classes `bg-primary` and `text-primary-foreground`
- Is **not** `disabled`

If it finds a matching button that is enabled, it clicks it.