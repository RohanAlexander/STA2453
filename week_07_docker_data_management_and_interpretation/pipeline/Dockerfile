# A container for the ward forecast pipeline, following the ten rules in Nüst et al. (2020).
# Official, versioned base image; environment pinned from the lock file and built before the code is copied,
# so that editing a script does not reinstall the packages; data mounted at run time; one command runs it all.

FROM ghcr.io/astral-sh/uv:0.11.7-python3.12-trixie-slim

WORKDIR /project

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY scripts/ scripts/

ENTRYPOINT ["/bin/sh", "-c", \
  "for s in scripts/*.py; do uv run --frozen $s || exit 1; done"]
