# Nacho Barrios · oliv4s — personal website (v6)

Source for [oliv4s.github.io](https://oliv4s.github.io/), a static English-language personal website with three pages: Home, CV, and Blog. Version 6 introduces the personalised avatar, a fast-to-scan career timeline and a card-based CV. The intro, "Always learning", and "Notes & research" are retained.

## Update the existing GitHub Pages site

Use the existing public repository `oliv4s/oliv4s.github.io` — **do not create a new repository**.

1. Extract the ZIP archive. Copy the **contents** into your local repository root, replacing files with the same names. Be sure to include the hidden `.github` folder and `assets/nacho-avatar.webp`.
2. If your checkout uses Git, from its root run:

   ```sh
   git add -A
   git commit -m "Refresh avatar, journey and CV design"
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
- `assets/nacho-avatar.webp`: the approved illustration used on the Home page. If you replace it, keep the same path or update `templates/home.html`.
- `templates/home.html`, `templates/cv.html`, `templates/blog.html`: page layouts.
- `assets/styles.css`: appearance and mobile styles.
- `content/posts/`: Markdown blog posts. The included example is **unpublished** (`published: false`); it is not generated as a public web page.

**Privacy & disclosure:** Uploaded CV PDFs and the private phone number/email do not appear in this project. Never put unpublished vulnerability details, embargoed writeups, confidential company materials, or credentials in the public repository — the `published: false` flag hides a post from the generated site but does **not** make the source private on GitHub.
