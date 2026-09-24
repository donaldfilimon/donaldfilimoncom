# Self-hosted macOS runner

The `test_and_lint` job in `.github/workflows/jekyll-gh-pages.yml` runs on a macOS arm64 runner registered to this repository. GitHub-hosted jobs can't start while the account's Actions billing is locked, but self-hosted jobs still run.

## Registration

| Field | Value |
|-------|-------|
| Labels | `self-hosted`, `macOS`, `ARM64`, `donaldfilimoncom` |
| Register at | [Settings → Actions → Runners → New self-hosted runner](https://github.com/donaldfilimon/donaldfilimoncom/settings/actions/runners/new?arch=arm64) (choose macOS, ARM64) |

A runner is registered to one repository. If the same Mac already runs a runner for another repository (for example `abi`), install a second runner in its own directory, such as `~/actions-runner-donaldfilimoncom`. Pass the custom label when you configure it (`./config.sh --url https://github.com/donaldfilimon/donaldfilimoncom --token <token> --labels donaldfilimoncom`), then run `./svc.sh install && ./svc.sh start`.

Until a runner with these labels is online, `test_and_lint` waits in the queue. While it waits, the workflow run stays in progress and holds the workflow's `pages` concurrency group, so later pushes queue behind it.

## Host requirements

- Homebrew at `/opt/homebrew`, with `python` installed (`brew install python`). The job puts `$(brew --prefix python)/libexec/bin` on `PATH`, so `python` is Homebrew's current Python 3, the same "latest 3.x" that `actions/setup-python` with `python-version: '3.x'` picked. The job doesn't install Python itself: it fails with a clear error if Homebrew Python is missing.
- `actions/setup-python` isn't used on this runner. On a self-hosted Mac it installs a `.pkg` with `sudo installer` into `/Library/Frameworks` and needs a writable `/Users/runner/hostedtoolcache`.
- The runner account needs network access to PyPI. Every package in `requirements.txt` (TensorFlow, `tensorflow-io`, Keras, NumPy, Matplotlib, Django, `opencv-python`, `django-environ`) publishes macOS arm64 wheels, but only for some Python versions. `tensorflow-io` 0.37.1 has wheels for CPython 3.9 to 3.12, and TensorFlow 2.21 for 3.10 to 3.13. The same limit applies to the Ubuntu job.
- `pytest` and `flake8` aren't in `requirements.txt`. The job runs them after activating the venv, so if they're missing there, the shell falls back to the runner's `PATH`. Keep them out of the runner's `PATH` (for example, don't `brew install flake8`) so the job can't pass by using tools from the host. The better fix is to add them to the requirements.

The job checks out with `actions/checkout`, whose default `clean: true` deletes the untracked `venv/` from the previous run. Each run builds a fresh environment.

## Security

This repository is public. The workflow's only triggers are `push` to `main` and `workflow_dispatch`, and both need write access. The self-hosted job also has a gate: `github.repository == 'donaldfilimon/donaldfilimoncom'` and the event must be `push` or `workflow_dispatch`. The job is skipped for any other event, including a `pull_request` trigger added later, so fork code never runs on this machine. Adding pull request coverage later needs a `test_and_lint-hosted` fallback job for fork PRs, like the one in `donaldfilimon/mlai-website-app`.

The checkout uses `persist-credentials: false`. The job's token is narrowed to `contents: read`, and the workflow's `pages: write` and `id-token: write` scopes stay with the hosted Pages jobs.

Where you can, use a dedicated macOS user for the runner rather than your daily account. Keep no production secrets on the host.

## Jobs that stay GitHub-hosted

- `build` uses `actions/jekyll-build-pages@v1`, a Docker container action (`runs.using: docker`). Container actions only run on Linux runners, so it can't move to macOS without a rewrite to `ruby/setup-ruby` and `bundle exec jekyll build`.
- `deploy` (`actions/deploy-pages@v4`) needs `build` and `test_and_lint`. Since `build` must stay hosted, moving `deploy` alone wouldn't let a deployment finish.

Both stay blocked until the billing lock is cleared.
