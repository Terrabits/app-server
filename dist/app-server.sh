#!/usr/bin/env bash
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


# exit on error
set -e


cd "$ROOT_DIR"


# start
app-server/app-server --open-browser apps
