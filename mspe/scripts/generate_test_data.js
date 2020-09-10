// data = '<read_csv_file_or_array>';

const MAX_VARIATION = .25;

let result = [];

for (let row of data.split('\n')){
  let cols = row.split(',')
  let count = parseInt(cols[2])

  let value;
  // ADD OR SUBTRACT RANDOMLY
  if (Math.random() >.4999) {
    value = Math.floor(count + (Math.random() * (count * MAX_VARIATION)))
  } else {
    value = Math.floor(count - (Math.random() * (count * MAX_VARIATION)))
  }

  result.push([cols[0], cols[1], value].join(','))
}

console.log(result.join('\n'))
