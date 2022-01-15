Wordle Toolbox
==============

A decision tree based [Wordle](https://www.powerlanguage.co.uk/wordle/) solver.

See also: [Tonguess Toolbox](https://github.com/blueset/tonguess-toolbox)

## Files
* `build_mapping.py`: Build guess-feedback mappings.
* `dict_query`: Words that can be a query but not an answer
* `dict_ans`: Words that can be an answer
* `entropy_tree.py`: Build the entropy trees
* `entropy_tree`: Pickle of entropy tree
* `entropy_tree.json`: JSON of entropy tree
* `guess.py`: Word guessing helper functions
* `mapping`: Mapping for all words (need to build)
* `std_dev.py`: Standard deviation helper functions
* `translate.py`: Translate the pickled tree to JSON
* `tree_stats.py`: Statistics about trees built
* Web interface
  * `index.html`: Landing page
  * `interactive.html`: The solver
  * `lookup.html`: The filter
  * `data.js`: Data of the entropy tree


## Build and run

```sh
# Build mappings
python3 build_mappings.py

# Build entropy tree
python3 entropy_tree.py

# Translate the trees to JSON
python3 translate.py entropy_tree
```


# License

```
MIT License

Copyright (c) 2022 Eana Hufwe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
