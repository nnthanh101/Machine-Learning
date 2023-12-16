#!/usr/bin/env bash

clear
printf "\e[0;32mInternal Development Platform (IDP): $(basename $PWD)\e[0m\n"
# devcontainer-info

echo "[x] Verify Git client":        $(git --version)
echo "[x] Verify jq":                $(jq   --version)
echo "[x] Verify make":              $(make -v)

echo "[x] Verify AWS CLI version 2": $(aws --version)

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
echo "[x] Verify NVM":               $(nvm --version)
echo "[x] Verify Node.js":           $(node --version)
echo "[x] Verify npm":               $(npm --version)

echo "[x] Verify yarn":              $(yarn --version)
npm install -g yarn aws-cdk
echo "[x] Verify CDK":               $(cdk --version)

echo "[x] Verify Python":            $(python -V)
echo "[x] Verify Python3":           $(python3 -V)
echo "[x] Verify Pip3":              $(pip3 -V)
echo "[x] Verify Pip":               $(pip -V)

echo "[x] Verify jupyter lab":       $(jupyter lab --version)
echo "[x] Verify jupyter lab list":  $(jupyter lab list)

echo "[x] Verify Java":               $(java -version)

echo "[x] Verify ngrok":             $(ngrok --version)
echo "[x] Verify s3cmd":             $(s3cmd --version)

pip install --upgrade pip
if [ -f requirements.txt* ]; then pip install -r requirements.txt; else pip install pandas numpy scipy statsmodels matplotlib seaborn plotly scikit-learn; fi