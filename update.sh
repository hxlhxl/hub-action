#!/usr/bin/env bash

git add .
git commit -m 'update'
git tag `cat serial`
git push origin master --tags
