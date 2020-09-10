
# ironhacks-mspe


> IronHacks solutions scorer for MSPE

Version: 1.0.0

Topics: [statistics](https://github.com/topics/statistics),  [csv](https://github.com/topics/csv),  [data-science](https://github.com/topics/data-science),  


## About

[]()

### Author

Matt Harris <charrismatic@protonmail.com> (https://charrismatic.github.io/)

---


## Dependencies

-  csv-reader: "^1.0.6"

### Config Options

- `delimiter`     (Str)   []      - The character that separates between cells
- `multiline`     (Bool)  [true]  - Allow multiline cells, when the cell is wrapped with quotes ("...\n...")
- `allowQuotes`   (Bool)  [true]  - Should quotes be treated as a special character that wraps cells etc.
- `skipEmptyLines`(Bool)  [false] - Should empty lines be automatically skipped?
- `skipHeader`    (Bool)  [false] - Should the first header row be skipped?
- `asObject`      (Bool)  [false] - Convert each row automatically to object based on header. Implies skipHeader=true
- `parseNumbers`  (Bool)  [false] - Automatically parse numbers. Supports any format by `parseFloat`
- `parseBooleans` (Bool)  [false] - Automatically parse booleans (strictly lowercase true and false)
- `ltrim`         (Bool)  [false] - Automatically left-trims columns
- `rtrim`         (Bool)  [false] - Automatically right-trims columns
- `trim`          (Bool)  [false] - If true, then both 'ltrim' and 'rtrim' are set to true


## Usage

-  start: "node ."
-  test: "standard"

## Development

__TODO:__

- [ ] Check performance boosts for sort, preprocessing.
- [ ] Check performance implications for removing found rows from search set.
- [ ] Check for duplicate rows and/or missing values in solution set vs key.
- [ ] Ensure correct week number for each row.


### Issues


---

### License

ISC[ISC](https://opensource.org/licenses/undefined)
