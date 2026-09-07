# BCEF — GitHub Pages

A static reading page for the supplied Biblical Creation Epistemic Framework, version 20260906-170412 (UTC−08:00). The document's premises, claims, classifications, section numbering, equations, and provenance notes are retained. Earlier framework files were not merged into this edition.

## Publish on GitHub Pages

1. Extract this ZIP on your computer.
2. Add `index.html`, `assets/`, `biblical-creation-epistemic-framework.md`, and `.nojekyll` to the root of the repository branch you want to publish. Commit the files. Keep the `assets` folder structure. Upload the extracted files, not the ZIP itself.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment → Source**, select **Deploy from a branch**.
5. Select your publishing branch and **/(root)**, then select **Save**.
6. Wait for the Pages deployment to finish. Open the published URL shown in Settings → Pages.

If your repository already has an `index.html` or an `assets` folder, review the files before replacing them. Alternatively, place these files in `docs/` and select **/docs** as the publishing folder. All site paths are relative, so the page supports a GitHub project URL such as `/bcef/` and a custom domain without code changes.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Files

- `index.html`: complete pre-rendered page, including equations in native MathML.
- `assets/style.css`: desktop, mobile, and print layouts.
- `assets/navigation.js`: active-section tracking and mobile menu behavior. All content and navigation remain available without JavaScript.
- `biblical-creation-epistemic-framework.md`: unchanged supplied Markdown source, including its metadata.
- `.nojekyll`: serves the static files without Jekyll processing.
- `build.py`: optional regeneration script, requiring Python 3 and Pandoc. No build tool is needed to publish the supplied files.

## Preview and update

Open `index.html` in a current browser after extracting all files. It does not use external fonts, scripts, services, or analytics. The equations use browser-native MathML. Wide equations can scroll horizontally. Use your browser's Print command for the print layout.

For future content changes, edit the Markdown file, then run:

```sh
python3 build.py
```

The script regenerates `index.html`; publish that file together with the updated Markdown. Edit CSS and JavaScript directly for appearance and navigation changes. Keep the version and last_updated fields current in the source metadata.

## Validation

The package was checked for preserved document text, complete headings, unique section IDs, valid internal links, existing local assets, equation conversion, and JavaScript syntax. No browser-based visual test was run.

## Content and licensing

No new license is assigned to the supplied document. Its Related section retains references to earlier documents as provenance; those references do not claim that the earlier files are bundled. The page is a presentation of the supplied framework, not an independent assessment of its claims.
