#!/usr/bin/env node

const fs = require('fs');
var argv = require('minimist')(process.argv.slice(2));

const getNotebook = (filename) => {
  let fileBuffer = fs.readFileSync(filename)
  let fileData = Buffer.from(fileBuffer).toString('UTF-8')
  return JSON.parse(fileData)
}

const getNotebookScore = (nb) => {
  let sum = 0;
  let min = 999999999999;
  let max = 0;
  let results = [];

  for (cell of nb.cells) {
    if (cell.cell_type === 'code') {
      results.push(cell.execution_count)
    }
  }

  // REMOVE EMPTY CELLS
  results = results.filter((result)=>{
    return result
  })

  for (result of results) {
    sum += result
    if (result < min) {
      min = result
    }
    if (result > max) {
      max = result
    }
  }

  return {
    total_cells: nb.cells.length,
    code_cells: results.length,
    exec_sum: sum,
    exec_min: min,
    exec_max: max,
    exec_avg: (sum / results.length).toFixed(2),
  }
}


const printNbScore = ({
  total_cells,
  code_cells,
  exec_sum,
  exec_min,
  exec_max,
  exec_avg,
}) => {
  console.log(`User: ${userId}`);
  console.log('-----------------------');
  console.log(`Total Cells: ${total_cells}`);
  console.log(`Code Cells: ${code_cells}`);
  console.log(`Exec Sum : ${exec_sum}`);
  console.log(`Exec Min : ${exec_min}`);
  console.log(`Exec Max : ${exec_max}`);
  console.log(`Exec Avg : ${exec_avg}`);
  console.log();
}


const writeNbScoreFile = ({outputFile, outputPath, userId, score}) => {
  const header_row = [
    'userId',
    'nb_effort',
  ].join(',')

  const data_row = [
    userId,
    score,
  ].join(',');


  !fs.existsSync(outputPath) && fs.mkdirSync(outputPath, { recursive: true })

  const output = [header_row, data_row, ''].join('\n')

  fs.writeFileSync([outputPath, outputFile].join('/'), output)
}


// PROCESS ENV
const parse_options = () => {
  var defaults = {
    input: false,
    dry_run: false,
    output: 'nb-effort.csv',
    verbose: false,
    userId: null,
  };

  var options = Object.assign({}, defaults, argv);

  if (options.verbose) {
    console.log(argv);
    console.log('current options', options );
  }

  if (options.user) {
    userId = options.user
  }

  if (options.hack) {
    hackId = options.hack
  }

  if (options.submission) {
    submissionId = options.submission
  }

  return options
}

const main = () => {
  let notebook_file    = `./data/${hackId}/submissions/${submissionId}/${userId}/submission_prediction_output.ipynb`
  let result_path      = `./data/${hackId}/results/${submissionId}/notebook-effort`
  let result_filename  = `${userId}.csv`

  let nb = getNotebook(notebook_file)
  let result = getNotebookScore(nb)

  printNbScore(result)

  writeNbScoreFile({
    userId: userId,
    outputFile: result_filename,
    outputPath: result_path,
    score: result.exec_avg,
  })
}

let hackId
let submissionId
let userId

let options = parse_options()

if (!userId) {
  console.log('Please set the userId --user <USER_ID>')
  return false
}

if (!hackId) {
  console.log('Please set the hackId --hack <HACK_ID>')
  return false
}

if (!submissionId) {
  console.log('Please set the submissionId --submission <SUBMISSION_ID>')
  return false
}

main()
