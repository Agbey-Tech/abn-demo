# Deploy to GitHub Pages

The demo is entirely static. No Node installation, npm dependencies, API keys, backend, custom domain, or repository-name configuration is needed. Relative URLs support both `https://USERNAME.github.io/REPOSITORY/` and a user-site repository at `https://USERNAME.github.io/`.

## First deployment

1. Create an **empty GitHub repository** for this demo. Do not pre-create its README or .gitignore if following the commands below. A public repository is the simplest option with GitHub Free.
2. In the repository, open **Settings → Pages → Build and deployment → Source**, and select **GitHub Actions**. Do this before pushing so the first workflow can configure Pages.
3. Open a terminal in the `demo` directory and run the following, replacing the example remote with your repository URL:

```powershell
git init -b main
git add .
git commit -m "Add Ascend redesign demo"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

If this directory is already a Git repository, skip `git init`. If `origin` already exists, use its existing URL or update it with `git remote set-url origin YOUR-REPOSITORY-URL` instead of adding it again.

4. In **Actions**, open **Deploy demo to GitHub Pages**. The workflow builds the demo, checks every local link and asset, and deploys the resulting `_site` directory.
5. The deployed URL appears in the `github-pages` environment and **Settings → Pages**. It is usually `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`.

The workflow runs on pushes to `main` and can also be started manually through **Actions → Deploy demo to GitHub Pages → Run workflow**. If you use a different default branch, update `.github/workflows/deploy.yml` accordingly. Repository environment protection rules may require an approval in GitHub before deployment.

## Later changes

```powershell
git add .
git commit -m "Refine demo"
git push
```

## Edit and preview locally

The homepage source is `src/home.html`. Shared content/components live in `scripts/content.py`, supporting pages in `scripts/pages.py`, and generation in `scripts/build.py`. The active styles are in `design.css`; interactions are in `site.js`.

```powershell
python scripts/build.py
python scripts/check_site.py
python -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173/`. Use a local HTTP server for folder URLs and cross-page navigation. No application build server is needed. Stop the server with Ctrl+C.

To reproduce the deploy artifact locally:

```powershell
python scripts/build.py --output _site
python scripts/check_site.py _site
python -m http.server 4173 --bind 127.0.0.1 --directory _site
```

## Demo scope

The homepage leads with the broader company offer. Work features six curated original projects. Supporting pages demonstrate services, audience solutions, About, Contact, and the secondary Network area. Original page routes remain valid.

The deployment artifact includes only active CSS/JS and the images referenced by the demo. The complete content inventory remains in the source repository for reference. Contact forms validate locally and never send or store enquiries. Planned events and unpublished resources retain their status.

## If a deployment fails

- Verify that Pages **Source** is **GitHub Actions**.
- Verify that the push went to `main` or adjust the workflow branch.
- Read the failed workflow step in Actions. Link-check errors identify the source page and destination.
- If repository rules block `github-pages`, approve the deployment or adjust the environment rules in GitHub.
- Do not add a `CNAME` file unless you are actually configuring a custom domain.

This workflow follows [GitHub’s official custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), using the configure, artifact-upload, and deployment actions with the required Pages and OIDC permissions.
