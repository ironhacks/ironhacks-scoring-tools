function getMetrics(data) {
  let metrics = [];
  [...new Set(
    Object.values(data).map((item,index)=>{
      return item.map((key,i)=>{
        return key.name
      })
      .join(',')
    })
  )]
  .map((list)=>{
    return list.split(',')
  })
  .map((metric)=>{
    metrics= [...new Set([...metrics, ...metric])]
  })

  return metrics;
}

function getStats(list) {
  var delta = [];
  var sum = 0;
  var deltaSum = 0;

  list.sort((a,b)=>{ return a - b})

  var median = list[Math.floor(list.length / 2)];
  var range = [Math.min(...list), Math.max(...list)];

  list.forEach((item)=>{sum = sum + item});
  var mean = (sum / list.length);

  list.forEach((item)=>{delta.push(Math.abs(item - mean))});
  delta.forEach((item)=>{deltaSum = deltaSum + item});
  deltaMean = (deltaSum / delta.length);

  var stdRange = [
    (mean - deltaMean - deltaMean),
    (mean + deltaMean + deltaMean),
  ]

  return {
    sum,
    range,
    mean,
    median,
    deltaMean,
    stdRange
  }
}



metrics = getMetrics(data);
values = {};
metrics.forEach ((metric)=>{
  values[metric] = [];
})

// CONVERT LIST OF RESULTS TO SET OF KEYS AND ARRAY OF VALUES
Object.values(data).forEach((user)=>{
  user.forEach((item)=>{
    values[item.name].push(item.value)
  })
})

// FILTER NULL (AND/OR FALSE) VALUES FROM THE VALUE LIST
Object.keys(values).map((key)=>{
  values[key] = values[key].filter((item)=> {return item})
})

// >values
// ---
// bq_jobs: (10) [23, 520, 29, 12, 40, 3, 118, 40, 23, 103]
// mape: (6) [4019.66, 1010.13, 927.73, 4019.66, 788.78, 1405.3]
// mspe: (6) [156486643.9, 1620130.2, 6568186.9, 156486643.9, 4161677.29, 13640016.03]
// nb_effort: (6) [28.67, 3.8, 6.58, 392.6, 110, 159.97]

stats = {};
Object.keys(values).forEach((key)=>{
  stats[key] = getStats(values[key])
})
