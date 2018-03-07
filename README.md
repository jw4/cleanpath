# Cleanpath

Simple tool to clean up PATH like strings by removing redundant and
incorrect entries but keeping the relative order of the paths that
remain.

## For example

```sh
$ export FAKEPATH=/usr/bin:/usr/local/bin:/usr/bin:/usr/sbin:.
$ export FAKEPATH=$(cleanpath $FAKEPATH)
$ echo $FAKEPATH
/usr/bin:/usr/local/bin:/usr/sbin
```

See [this .bashrc](https://github.com/johnweldon/tiny-profile/blob/3166eabe36b16acc9ba0c3631c4b504c0447fc7e/.bashrc#L163-L176) for a real life example of usage.

### Notice:
  1. Redundant paths removed, but relative order of first occurence is maintained.
  1. Relative (unsafe) paths removed.
  1. The separator char defaults to `:` for posix paths, but can be specified as `;` for windows paths.


## Usage

```
usage: cleanpath [-h] [-separator <sep>] [<pathvar> [<pathvar> ...]]

Clean PATH like strings

positional arguments:
  <pathvar>         PATH values

optional arguments:
  -h, --help        show this help message and exit
  -separator <sep>  path separator char
```


## Development

Run unit tests with `python -m unittest`

