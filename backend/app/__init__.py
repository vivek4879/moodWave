#this file tells python that this directory is a package
#allows us to import the app directory as a package
#and use the files in the app directory as modules
#it is required for python to be able to import the files in the app directory
#it is also required for python to be able to use the files in the app directory as modules
#Without it, imports and uvicorn app.main:app can behave inconsistently.