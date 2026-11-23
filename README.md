# Nacho Barrios - oliv4s - personal website (v10)

Source for [oliv4s.github.io](https://oliv4s.github.io/), a static English-language personal website with three pages: Home, CV, and Blog. Version 10 includes a personalized avatar, a fast-to-scan career timeline, a continuous research/learning thread, and a card-based CV. The intro, "Always learning", and "Notes & research" are retained.

## Update the existing GitHub Pages site

Use the existing public repository `oliv4s/oliv4s.github.io` — **do not create a new repository**.

1. Extract the ZIP archive. Copy the **contents** into your local repository root, replacing files with the same names. Be sure to include the hidden `.github` folder and `assets/nacho-avatar.webp`.
2. If your checkout uses Git, from its root run:

   ```sh
   git add -A
   git commit -m "Fix company logos, uniform certifications and portrait label"
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


## Version 9 updates

- Evolve timeline node is solely about teaching, independent of vulnerability research.
- NTT DATA logo on the Penetration Tester role; everis on the previous internship.
- Employer marks refreshed using simplified locally drawn SVGs. These are not official corporate vector assets.
- Certification cards have a consistent background and styling.
- Avatar frame no longer repeats the site handle on both borders.
- Visible middle-dot and long-dash punctuation normalized to standard hyphens.
- Research and continuous learning is shown as an always-on thread throughout the journey, not as something that started at Evolve.


## Brand assets (v10)

- S2GRUPO: official blue corporate logo hosted by `s2grupo.es`, following the 2024 rebrand.
- NTT DATA: global blue logo from Wikimedia Commons (attributed to NTT DATA).
- Evolve: simple black leaf wordmark treatment based on its own learning platform, **not an original brand file**; replace `assets/logos/evolve.svg` with an official asset if Evolve provides one.
- The source includes local fallback graphics so logos do not disappear when a hosted image is unavailable.
- Certification cards intentionally use one consistent background, regardless of `featured` (which only controls the four shown on the homepage).
- The portrait module has one `OLIV4S` heading and a separate `OFFENSIVE SECURITY` descriptor, no `PORTRAIT` label.
