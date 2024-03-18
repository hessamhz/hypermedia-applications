
# hypermedia-applications


## **Table of Contents**

1. [Introduction](#introduction)
2. [Development Guidelines](#development-guidelines)
	2.1. [Pre Commit](#pre-commit)
	2.2. [Commit Message Conventions](#commit-message-conventions)
3. [Usability Evaluation](#usability-evaluation)


## **Introduction**
This repository is dedicated to the Web and Hypermedia Application courses which is offered at Politecnico di Milano.

## **Development Guidelines**
This guideline will be followed during the development.
### **Pre-commit**
Pre-commit is a tool that helps to keep the whole repository clean and prevents unnecessary conflicts.
1. Install pre-commit and the dependancies (Check how to install for other OS):

```
brew install pre-commit
```

2. Check if it is installed properly:

```
$ pre-commit --version

pre-commit 3.6.2
```

3. Install the hook (Do it whenever it changes):

```
pre-commit install
```

4. You can run the hook even when you are not committing with:

```
pre-commit run --all-files
```

5. To update the pre-commit you can use

```
pre-commit autoupdate
```
## **Commit Message Conventions**
Use this schema to do the commits.
```
feat: msg. // For features
hotfix: msg. // For fixes
chore: msg. // For general chores that are nor a feat or feature
doc: msg. // To update or create documentations
```
For example:
```
doc: updated README with pre-commit guide.
```
## **Usability Evaluation**
Inspection is the first part of the project. All the resources regarding the first part is available [here](https://github.com/hessamhz/hypermedia-applications/tree/main/usabality_evaluation).
