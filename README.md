# Nacho Barrios · oliv4s — CV-first website (v4)

A minimal personal website focused on your **professional profile and CV**, with a single **blog** for later CVE disclosures, bug bounty writeups and technical notes.

**Pages:** Home · CV · Blog. The CV now includes experience, education, certifications and courses taken from the supplied CV and LinkedIn export. It has **zero published posts** and no invented CVEs or credential dates. Hack The Box's *Pro Hacker* badge was visible on the provided public profile when prepared.

## Run locally

```bash
python -m pip install -r requirements.txt
python build.py
python -m http.server 8000 --directory dist
```

Open http://localhost:8000/.

## Deploy to GitHub Pages

1. Create a public repository named `oliv4s.github.io` on your account `oliv4s`.
2. Commit the **source files** from this folder (including `.github/workflows/deploy.yml`) to its default `main` branch.
3. In repository Settings → Pages, choose **GitHub Actions** under *Build and deployment*.
4. The included workflow builds and deploys the site on each push to `main`.

Target URL: `https://oliv4s.github.io/` after deployment. This project does not modify your account or publish anything automatically.

## Customize your real CV

Edit `site.yml` to update professional summary, employers, experience, the certifications list and training. Experience is drawn from the two supplied PDF documents (October 2026 CV and LinkedIn export), but review every detail before public release. The website **does not include** those PDF documents, private phone number or personal email address. LinkedIn's 2026 timeline can differ slightly from the October CV (e.g., internship end date); the October CV was preferred where possible.

Certifications (OSCP, BSCP, CRTL, CRTO, OSWP, CHMRTS, MCRTA, CEH v10, AZ-900 and Certified Purple Teaming Fundamentals) are listed without invented dates or badge URLs. Course completions are shown separately as training, not mixed with certifications. Add public verification URLs to an individual certification as `credential_url:` if available. The public Secur0 profile URL remains pending.

## Upload from Windows PowerShell

1. On GitHub, create a **public** repository called `oliv4s.github.io` under the `oliv4s` account. Leave README and `.gitignore` unchecked.
2. Extract the ZIP to a local folder, open PowerShell inside that folder (where `site.yml` and `build.py` are visible), and run:

```powershell
git init -b main
git add -A
git commit -m "Initial CV website"
git remote add origin https://github.com/oliv4s/oliv4s.github.io.git
git push -u origin main
```

3. GitHub repo **Settings → Pages → Build and deployment → Source: GitHub Actions**. The included `.github/workflows/deploy.yml` builds and publishes on push to `main`.
4. In **Actions**, check `Publish to GitHub Pages` has a green success indicator; open `https://oliv4s.github.io/`.

Do **not** upload the ZIP as a single file. Commit the extracted source files and folders, including the hidden `.github` directory. The `dist` folder is generated automatically and is deliberately excluded from source control.

## Publish a blog post

1. Duplicate `content/posts/sample-advisory-layout.md` under a new filename.
2. Choose `category: "Research Notes"`, `"CVE"` or `"Bug Bounty"`.
3. Write the public article in Markdown and set `published: true`.
4. For categories `CVE` and `Bug Bounty`, also explicitly set `approved_for_publication: true` **only after permission to publish**.
5. Commit and push; GitHub Actions creates `/blog/<slug>/`.

**Important:** Frontmatter `published: false` does not make content private on a public GitHub repository. Do not commit embargoed findings, privately shared client materials, confidential vendor reports, PoCs or any information covered by NDA. Maintain these in a separate secure private location, not in this repository, including git history.

## Implementation

Python + Jinja2 + Mistune + PyYAML generate static HTML; GitHub Actions hosts it on GitHub Pages. No backend, trackers or third-party fonts. The light/dark toggle persists in localStorage; otherwise the theme follows the operating system. All portfolio copy is in English, and the existing avatar is an abstract illustration rather than a likeness.

**Credential details:** The `credential_url` is optional; omit it if not available, rather than inventing a verification link. Never publish personal credential IDs or confidential enrollment details.
