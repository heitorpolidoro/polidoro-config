# Loaders

`````{py:class} ConfigLoader
:canonical: pconfig.loaders.loader.ConfigLoader

```{autodoc2-docstring} pconfig.loaders.loader.ConfigLoader
```

````{py:attribute} order
:canonical: pconfig.loaders.loader.ConfigLoader.order
:type: int
:value: MAXINT

```{autodoc2-docstring} pconfig.loaders.loader.ConfigLoader.order
```

````


````{py:method} load(config_class: ConfigBase) -> dict[str, object]
:canonical: pconfig.loaders.loader.ConfigLoader.load
:staticmethod:

```{autodoc2-docstring} pconfig.loaders.loader.ConfigLoader.load
```

````

````{py:method} load_config(config_class: ConfigBase | None = None) -> dict[str, object]
:canonical: pconfig.loaders.loader.ConfigLoader.load_config
:abstractmethod:
:classmethod:

```{autodoc2-docstring} pconfig.loaders.loader.ConfigLoader.load_config
```

````
`````

```{toctree}
:maxdepth: 1
envvar_loader
```
