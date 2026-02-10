# Development

## Install (Editable)

```sh
python3 -m pip install -e '.[dev]'
```

## Run Tests

```sh
python -m pytest
```

## Build / Publish

```sh
python3 -m pip install -U build twine
python3 -m build
python3 -m twine check dist/*
```
