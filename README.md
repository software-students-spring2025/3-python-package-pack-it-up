![Python build & test](https://github.com/software-students-spring2025/3-python-package-pack-it-up/actions/build.yaml/badge.svg)

# Python Package Example

A fun and lighthearted package for generating random and styled Git commit messages.

# Team Members

Jasmeen Kaur
Sophia Schlichting
Preston Lee
Julia Ahn

# Function Documentation

## random_commit_message()

Generates a randomly selected commit message from the database

### Parameters:

- None

### Return:

- `str`: A randomly selected commit message

---

## generate_commit_message(style)

Generates a randomly selected commit message that has the style the user specified

### Parameters:

- `style` (`str`): the style of message the user wants

### Return:

- `str`: A randomly selected commit message from the user's desired style

---

## git_blame_excuse()

Generates a randomly selected excuse

### Parameters:

- None

### Return:

- `str`: A randomly selected excuse

---

## generate_haiku()

Generates a randomly selected haiku

### Parameters:

- None

### Return:

- `str`: A randomly selected excuse

---

## add_commit_message(style, message)

Allows a user to create a new commit message

### Parameters:

- `style` (`str`): the style of message the user wants to add
- `message` (`str`): the message the user wants to add

### Return:

- `str`: if the message was successfully saved to the database, a confirmation str will be displayed
- `str`: if the message already exists in the database, a str outlining that will be displayed
- `str`: if there are issues with saving the message, and error message will be displayed

---

## add_excuse(message)

Allows a user to create a new excuse

### Parameters:

- `message` (`str`): the excuse the user wants to add

### Return:

- `str`: if the excuse was successfully saved to the database, a confirmation str will be displayed
- `str`: if the excuse already exists in the database a str outlining that will be displayed
- `str`: if there are issues with saving the excuse an error message will be displayed

---

## add_haiku(message)

Allows a user to create a new haiku

### Parameters:

- `message` (`str`): the haiku the user wants to add

### Return:

- `str`: if the haiku was successfully saved to the database, a confirmation str will be displayed
- `str`: if the haiku already exists in the database, a message outlining that will be displayed
- `str`: if there are issues with saving the haiku an error message will be displayed
