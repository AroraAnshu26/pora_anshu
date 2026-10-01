#!/usr/bin/sh
# Cleanup for CS237A sections.
# WARNING: this deletes the local workspace. Push to GitHub before running.

# 1. Log out of GitHub
git config --global --unset AroraAnshu26
git config --global --unset anshuarora2604@gmail.com
gh auth logout

# 2. Remove the workspace. This MUST be the last line - see below.
rm -rf "~/autonomy_ws"