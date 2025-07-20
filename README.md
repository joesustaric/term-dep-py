# term-dep-py

A simple CLI app to calculate term deposits.

## Decisions
1. Have left out input validation checking. e.eg asking for quarterly interest payments but only selecting a 3 month deposit term.
1. Have left out bounds checking on some of the inputs. e.g. max term deposit amount, interest checking, months should be less than 12 etc.
1. it's unclear how remainder interest is calculated for instance a 3 year 4 month term deposit paid yearly pays 3 yearly interest payments but how does the remainder get processed? I made an assumption that its per month. Except if its quarterly. Each 4 months pays interest then any month remainders are paid monthly. I know this isn't correct from the online calculator however it's not clear how its being done without more time reverse engineering the calculations. 

## Setup

I use `asdf` to manage versions of things.

This uses a `.tool-versions` file to define the versions of things used. Look there and install them.

You can use that or whichever way you use to manage your different python / poetry run time environments.

Then run:
```bash
poetry install
```

## Development Setup

Poetry virtual env ensures you're working in an isolated environment where dependencies won't conflict with other projects or the system Python.

To activate the virtual environment in your current shell, use:

```bash
poetry env activate
```

Or alternatively, you can install the shell plugin and use the classic command:
```bash
poetry self add poetry-plugin-shell
poetry shell
```

To run the main function:
```bash
poetry run cli
```

Run the tests.
```bash
poetry run pytest # -v for verbose
```

>[!NOTE]
> The test configuration setting are in the `project.toml` file.

This project uses [Ruff](https://docs.astral.sh/ruff/) as a Python linter and code formatter.

To use it run:
```bash
# Check code format
poetry run ruff check

# Check code format and fix
poetry run ruff check --fix

# Run the Linter
poetry run ruff format
```

### Debugging

You can use pythons `pdb` by inserting:

```python
import pdb; pdb.set_trace()
```

Refer to the docs [here](https://docs.python.org/3/library/pdb.html) on how to use the debugger.
