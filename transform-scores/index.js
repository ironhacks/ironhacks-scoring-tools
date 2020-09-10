// data = [...]
results = {};
data.map((item,index)=>{
  let result = [];
  result.push({
    name: 'mspe',
    label: 'MSPE',
    value: item.mspe,
  })

  result.push({
    name: 'mape',
    label: 'MAPE',
    value: item.mape,
  })

  result.push({
    name: 'nb_effort',
    label: 'Notebook Effort',
    value: item.nb_effort,
  })

  result.push({
    name: 'bq_jobs',
    label: 'BigQuery Effort',
    value: item.bq_jobs,
  })

  results[item.user] = result;
})

console.log(JSON.stringify(results, null, '  '))
