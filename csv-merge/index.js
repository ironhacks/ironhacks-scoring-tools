
const readCsv = async () => {
  let data;

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
      data[row.uuid] = row.sum_visit_counts
    })
    .on('end', function (data) {
      return data
    });
}


const readFiles = () => {

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
  readFiles();
}

let userId;
parse_options();

let submissionId = 'submission-3';
let result_filename = `./results/${submissionId}/${userId}.csv`;

if (!userId) {
  console.log(userId);
  console.log('Please set the userId --user <USER_ID>');
  return false;
}

main();
