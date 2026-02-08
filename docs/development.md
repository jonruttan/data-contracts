# Development

## Install (Editable)

```sh
python -m pip install -e '.[dev]'
```

## Run Tests

```sh
python -m pytest
```

## Build / Publish

```sh
python -m pip install -U build twine
python -m build
python -m twine check dist/*
```

