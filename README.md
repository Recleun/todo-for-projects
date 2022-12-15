# Pylister

Pylister is a tool that you can use to manage your projects through the terminal.\
It is pretty simple to use. You add projects to Pylister (no directories needed, only a name is enough), you can also add descriptions to these projects, and the main objective of Pylister is to store and manage the tasks that you create for these projects.

## Installation

*Note: Python is required for installation*
```
pip install pylister
```

## Usage

Notes:
- You can use either `pylister` or `pyl`
- \<Option> is required, [Option] is optional
- For options that need more than one word, use quotation marks:\
    `--desc This is a description` (Wrong)\
    `--desc "This is a description"` (Right)


To see what commands you can use:
```
pylister
```
If you want help for a specific command:
```
pylister [COMMAND] --help
```
Example:
```
pyl addp --help
```

## 1 - Projects

#### 1.1 Listing Projects

```
pylister list
```

#### 1.2 Viewing Project info

*(Can be used to show tasks and their IDs for a specific project)*
```
pylister show <Project Name>
```

Example:

```
pyl show pylister
```

#### 1.3 Adding Projects

```
pylister addproject <Project Name> [--desc Description]
```

Example:

```
pyl addp pylister --desc "This is a description"
```

#### 1.4 Removing Projects

```
pylister rmproject <Project Name>
```

Example:

```
pyl rmp pylister
```

#### 1.5 Modifying Projects

```
pylister set <Project Name> <name|description> <new>
```

Examples:

*(For description)*
```
pyl set pylister description "This is a new description"
```

*(For name)*
```
pyl set pylister name "New Name"
```

## 2 - Tasks

#### 2.1 Adding Tasks

```
pylister addtask <Project Name> <Task>
```

Example:

```
pyl addt pylister "Improve the readme"
```

#### 2.2 Removing Tasks

```
pylister rmtask <Project Name> <Task ID>
```

Example:

```
pyl rmt pylister 1
```
