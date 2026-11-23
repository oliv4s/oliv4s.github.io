# Nacho Barrios · oliv4s — personal website (v8)

Source for [oliv4s.github.io](https://oliv4s.github.io/), a static English-language personal website with three pages: Home, CV, and Blog. Version 8 refines the light palette to olive, retains the dark background, adds social platform icons, illustrated company wordmarks on the interactive career path, and a sketch illustration in Always learning. The compact avatar, readable CV, and Notes & research are retained.

## Update the existing GitHub Pages site

Use the existing public repository `oliv4s/oliv4s.github.io` — **do not create a new repository**.

1. Extract the ZIP archive. Copy the **contents** into your local repository root, replacing files with the same names. Be sure to include the hidden `.github` folder, `assets/nacho-avatar.webp`, `assets/learning-sketch.webp`, and both `assets/logos/` and `assets/icons/`.
2. If your checkout uses Git, from its root run:

   ```sh
   git add -A
   git commit -m "Refine olive palette, social icons and journey logos"
   git push origin main
   ```

3. Under repository **Settings → Pages**, keep **Source: GitHub Actions**. The existing `.github/workflows/deploy.yml` builds the static site and publishes `dist/`.
4. Check **Actions → Publish to GitHub Pages** to see the result, then visit <https://oliv4s.github.io/>. Hard refresh (Ctrl+F5) if the browser displays cached styling.

The `README.md` file is only project documentation, **not** the public home page. Do not change Pages to "Deploy from a branch".

## Local preview

```sh
python -m pip install -r requirements.txt
python build.py
python -m http.server 8000 --directory dist
```

Open <http://localhost:8000/>.

## Edit content

- `site.yml`: experience, education, certifications, training, skills, journey milestone labels and professional links.
- `assets/nacho-avatar.webp`: the approved illustration used on the Home page.
- `assets/learning-sketch.webp`: the custom illustrated thinking-at-the-computer doodle for the learning section.
- `assets/logos/`: simplified local SVG wordmarks for the five career milestones (recognition marks, not official brand assets). Replace with approved company marks if desired.
- `assets/icons/`: local vector icons for social links.
- `templates/home.html`, `templates/cv.html`, `templates/blog.html`: page layouts.
- `assets/styles.css`: appearance and mobile styles.
- `content/posts/`: Markdown blog posts. The included example is **unpublished** (`published: false`); it is not generated as a public web page.

**Privacy & disclosure:** Uploaded CV PDFs and the private phone number/email do not appear in this project. Never put unpublished vulnerability details, embargoed writeups, confidential company materials, or credentials in the public repository — the `published: false` flag hides a post from the generated site but does **not** make the source private on GitHub.
