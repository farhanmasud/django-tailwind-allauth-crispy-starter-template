#!/bin/bash

echo "Enter git remote URL:"
read GITREMOTEURL

git remote remove origin
git remote add origin $GITREMOTEURL