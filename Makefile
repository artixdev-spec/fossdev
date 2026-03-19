help:
 @echo "This makefile for repo-level activity"

create-prcatice:
 mkdir demo-prcatice

create-structure:
 mkdir src tests docs
 touch README.md setup.py requirements.txt
 touch docs/DOMAIN.md
 touch src/.gitkeep tests/.gitkeep


remove-prcatice:
 rm -rf demo-prcatice

#mkdir demo-prcatice
#mkdir demo-prcatice/src
#mkdir demo-prcatice/tests
#mkdir demo-prcatice/docs
#mkdir demo-prcatice/README.md
