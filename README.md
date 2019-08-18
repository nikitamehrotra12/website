# Clone-Survey

## To start the server
`python app.py`

## Initial setup
1. Clone the repository.
2. Install virtualenv: `(sudo) pip install virtualenv` (sudo if required).
3. `cd <repository-path>`
4. `virtualenv venv`
5. `source venv/bin/activate`
6. `pip install -r requirements.txt`

## To start working
1. Activate virtual environment: `source venv/bin/activate`
2. `git checkout master`
3. `git pull`
4. Create a new working branch: `git checkout -tb <new-working-branch-name>`.

## To push your changes-
1. Make sure you are in the new branch you created. You can check the current working branch using `git branch`.
2. `git add .`
3. `git commit -m "<commit-message>"`
4. `git push origin <branch-name>`
5. Create a pull request.

### If you ever install a new python library, make sure to run this command
`pip freeze > requirements.txt`
