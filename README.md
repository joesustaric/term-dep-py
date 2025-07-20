# term-dep-py

A simple CLI app to calculate term deposits.

>[!NOTE]
> I acknowledge this implementation may not have heeded the _hint_ however I did not look at any compound interest equations.
> This was me trying to figure it out.

## Decisions
1. Done basic input data validation for range checks. The `argparser` can do type checking, the input validator does value checking.
1. It's unclear how remainder interest is calculated. For instance a 3 year, 4 month term deposit paid yearly pays 3 yearly interest payments but how does the remainder get processed? I made an assumption that it's per month for the same interest rate. I know this isn't correct from the online calculator however it's not clear how its being done without more time reverse engineering the calculations. Apologies, in the real world I would ask for the rules from a subject matter expert.
1. Given more time I would have used `Decimal` types more thoroughly or a robust tested money library to ensure no rounding errors. Floats are used for simplicity.

## Setup

I use [`asdf`](https://github.com/asdf-vm/asdf) to manage versions of things.

This uses a `.tool-versions` file to define the versions of things used. Look there and install them.

You can use that or whichever way you use to manage your different python / poetry run time environments. For MacOS `brew` generally will have it.

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
For help menu run:
```bash
poetry run cli --help
```

Run an example
e.g. - Initial deposit of $28900, interest rate of 3.1% p.a over 2 years and 3 months, paid monthly - run:
Note frequency flag inputs are `m = monthly, a = annual q = quarterly, t = maturity`
```bash
poetry run cli --deposit 28900 --interest 0.031 --years 2 --months 3 --frequency m
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
