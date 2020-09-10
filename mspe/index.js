#!/usr/bin/env node

const fs = require('fs');
const CsvReadableStream = require('csv-reader');
const { version } = require('./package.json');
var argv = require('minimist')(process.argv.slice(2));

let solution = {};
let solutionLoaded = false;
let prediction = {};
let predictionLoaded = false;

let rows = [];
let rows_delta = [];
let rows_delta_squared = [];
let result_rows = [];

result_rows.push(`uuid,count_prediction,count_actual,delta,delta_squared`);

const readSolution = async () => {
  const csv_config = {
    skipEmptyLines: true,
    skipHeader: true,
    asObject: true,
    parseNumbers: true,
    trim: true,
  }

  let inputStreamKey = fs.createReadStream(solution_filename, 'utf8');

  inputStreamKey
    .pipe(new CsvReadableStream(csv_config))
    .on('data', function (row) {
      solution[row.uuid] = row.sum_visit_counts
    })
    .on('end', function (data) {
      solutionLoaded = true;
      if (predictionLoaded) {
        compareData()
      }
    });
}

const readPrediction = async () => {
  const csv_config = {
    // delimiter: ',',
    // multiline: false,
    // allowQuotes: true,
    skipEmptyLines: true,
    skipHeader: true,
    asObject: false,
    parseNumbers: true,
    // parseBooleans: false,
    // ltrim: false,
    // rtrim: false,
    trim: true,
  }

  let inputStreamTest = fs.createReadStream(submission_filename, 'utf8');

  inputStreamTest
    .pipe(new CsvReadableStream(csv_config))
    .on('data', function (row) {
      let uuid = row[0];
      let value = row[2];
      // SKIP NULL VALUES WHERE UUID EXISTS
      if (value) {
        if (typeof value === 'string') {
          value = parseFloat(value)
        }
        if (isNaN(value)){
          value = null
        }
        prediction[uuid] = value
      }
    })
    .on('end', function (data) {
      predictionLoaded = true;
      if (solutionLoaded) {
        compareData()
      }
    })
    .on('error', (error) => {
      console.log(error);
      writeScoreFile({
        userId: userId,
        mape: 'read_error',
        mspe: 'read_error',
      })
    })
}

const compareData = () => {
  let solution_sum = 0;
  let prediction_sum = 0;
  let error_sum = 0;
  let error_sq_sum = 0

  for (let uuid of Object.keys(solution)) {
    let actual = solution[uuid];
    let predict = prediction[uuid];

    if (!predict) {
      predict = 0;
    }

    let delta = Math.abs(predict - actual);
    let delta_squared = delta * delta;

    solution_sum += actual
    prediction_sum += predict
    error_sum += delta
    error_sq_sum += delta_squared

    result_rows.push([
      uuid,
      parseFloat(predict).toFixed(2),
      parseFloat(actual).toFixed(2),
      parseFloat(delta).toFixed(2),
      parseFloat(delta_squared).toFixed(2),
    ].join(','))
  }

  let solution_count = Object.keys(solution).length;

  printReport({
    solution_rows: solution_count.toString(),
    prediction_rows: Object.keys(prediction).length.toString(),
    solution_count_sum: solution_sum.toLocaleString('en-us'),
    prediction_count_sum: prediction_sum.toLocaleString('en-us'),
    prediction_error: error_sum.toLocaleString('en-us'),
    prediction_mean_error: (error_sum / solution_count).toFixed(2).toLocaleString('en-us'),
    prediction_square_error: error_sq_sum.toLocaleString('en-us'),
    prediction_mean_square_error: (error_sq_sum / solution_count).toFixed(2).toLocaleString('en-us'),
  })

  writeResultFile(result_rows)

  writeScoreFile({
    userId: userId,
    mape: (error_sum / solution_count).toFixed(2).toLocaleString('en-us'),
    mspe: (error_sq_sum / solution_count).toFixed(2).toLocaleString('en-us'),
  })
}


const printReport = (data) => {
  COLOR_BLUE = '\033[01;34m';
  COLOR_WHITE = '\033[01;37m';
  COLOR_RED = '\033[01;31m';
  COLOR_GREEN = '\033[01;32m';
  COLOR_YELOW = '\033[01;33m';
  COLOR_RESET = '\033[0m';

  console.log(`Submission:`, COLOR_WHITE, submissionId, COLOR_RESET);
  console.log(`User:`, COLOR_WHITE, userId, COLOR_RESET);
  console.log('==========================================');
  console.log('Predicted Rows: ', COLOR_RED, data.prediction_rows, COLOR_RESET)
  console.log('Solution Rows:  ', COLOR_RED, data.solution_rows,COLOR_RESET)
  console.log('----------------');
  console.log('Predicted Sum:  ', COLOR_BLUE, data.prediction_count_sum, COLOR_RESET)
  console.log('Solution Sum:   ', COLOR_BLUE, data.solution_count_sum, COLOR_RESET)
  console.log('----------------');
  console.log('Sum Err:        ', COLOR_GREEN, data.prediction_error, COLOR_RESET)
  console.log('Avg Err:        ', COLOR_GREEN, data.prediction_mean_error, COLOR_RESET)
  console.log('----------------');
  console.log('Sum Squared Err:', COLOR_GREEN, data.prediction_square_error, COLOR_RESET)
  console.log('Avg Squared Err:', COLOR_GREEN, data.prediction_mean_square_error, COLOR_RESET)
  console.log('\n');
}

const writeResultFile = (result_rows) => {
  fs.writeFileSync(
    submission_graded_filename,
    result_rows.join('\n')
  )
}

const writeScoreFile = ({userId, mape, mspe}) => {
  const header_row = [
    'userId',
    'mape',
    'mspe',
  ].join(',')

  const data_row = [
    userId,
    mape,
    mspe,
  ].join(',');

  const output = [header_row, data_row, ''].join('\n')
  fs.writeFileSync(result_filename, output)
}


// PROCESS ENV
const parse_options = () => {
  var defaults = {
    input: false,
    dry_run: false,
    output: 'results.csv',
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

  return options;
}

const main = () => {
  readSolution();
  readPrediction();
}

let userId;
parse_options();

let submissionId = 'submission-4';
let submission_filename = `../data/${submissionId}/${userId}/submission_prediction_output.csv`;
let submission_graded_filename = `../data/${submissionId}/${userId}/result.csv`;
let result_filename = `../results/${submissionId}/mspe/${userId}.csv`;
let solution_filename = `./solutions/${submissionId}.csv`;


if (!userId) {
  console.log(userId);
  console.log('Please set the userId --user <USER_ID>');
  return false;
}

main();
