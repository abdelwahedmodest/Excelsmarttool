#!/bin/bash

cd  frontend
cd  reactfront
nvm use 14
set NODE_OPTIONS=--openssl-legacy-provider
npm  start
