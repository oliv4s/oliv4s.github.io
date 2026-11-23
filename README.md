# Nacho Barrios · oliv4s — personal website (v5)

Minimal English-language portfolio for GitHub Pages: Home with a career journey, detailed CV, and a Markdown blog for public disclosures. No real CVEs or unpublished research are included.

## Publish to GitHub Pages

1. Use the public GitHub repository `oliv4s/oliv4s.github.io`.
2. Copy all project source files into the repository root, including `.github/workflows/deploy.yml`. **Do not upload this README by itself.**
3. Under Settings → Pages, set Source to **GitHub Actions**.
4. Push to `main`; the existing workflow generates `dist/` and publishes that directory.
5. Visit `https://oliv4s.github.io/`.

For an existing local checkout, replace the existing project files with these and commit/push. The `dist/` folder is generated and ignored by Git.

## Local preview

```sh
python -m pip install -r requirements.txt
python build.py
python -m http.server 8000 --directory dist
```

Then open `http://localhost:8000/`.

## Personalise

- `site.yml`: journey paragraphs, work experience, certifications, courses, education, skill groups and public profile links.
- `assets/avatar.svg`: **temporary generic illustration**; replace it later with a personalised portrait (you can use the same SVG file or modify the template reference).
- `content/posts/`: publish only markdown articles you are authorised to disclose. The included sample is unpublished and ignored.
- `templates/` and `assets/styles.css`: layout and visual design.

Privacy: the uploaded source CV PDFs, telephone number and personal email are not part of the site. Do not place unreleased vulnerability details, credentials, internal work materials or private files in the public repository.
