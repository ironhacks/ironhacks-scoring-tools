#!/usr/bin/env node

const fs = require('fs');
const CsvReadableStream = require('csv-reader');
const { version } = require('./package.json');
var argv = require('minimist')(process.argv.slice(2));

async function readCsv(submission) {
  let data = [];

  const csv_config = {
    skipEmptyLines: true,
    skipHeader: false,
    asObject: true,
    parseNumbers: true,
    trim: true,
  }

  let inputStreamKey = fs.createReadStream(`./${base_dir}/${submission}/${target_filename}`, 'utf8');

  inputStreamKey
    .pipe(new CsvReadableStream(csv_config))
    .on('data', function (row) {
      const { userId, ...rest } = row;
        data.push({
          [userId]: rest,
        })
    })
    .on('end', (()=>{
      console.log({
        submission: submission,
        data: JSON.stringify(data),
      })

      return {
        submission: submission,
        data: data,
      }
    }))
}


function getSubmissionDirs() {
  let result = {};

  fs.readdirSync(base_dir)
    .filter((dir)=>{
      return dir.includes('submission')
    })
    .sort((a,b)=>{
      return a.localeCompare(a)
    })
    .forEach((dir)=>{
      result[dir] = fs.readdirSync(`./${base_dir}/${dir}`);
    })
  return Object.keys(result).filter(submission=>{
    return result[submission].includes(target_filename)
  })
}


// PROCESS ENV
function parse_options() {
  var defaults = {
    dry_run: false,
    verbose: false,
    target_filename: null,
  };

  var options = Object.assign({}, defaults, argv);

  if (options.verbose) {
    console.log(argv);
    console.log('current options', options );
  }

  if (options.target) {
    target_filename = options.target
  }

  return options;
}

async function main() {
  let mergeDirs = getSubmissionDirs();
  let promised = [];
  for (dir of mergeDirs) {
    promised.push(await readCsv(dir));
  }

  Promise.all(promised).then(()=>{
    console.log('done', promised);
  })
}

let target_filename;
parse_options();

if (!target_filename) {
  console.log('Please set the target filename to merge --target <FILE_NAME>');
  return false;
}

const base_dir = '../results'
const result_filename = `./../results/summary/${target_filename}`;

main();
