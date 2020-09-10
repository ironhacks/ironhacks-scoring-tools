// EXAMPLE DEMONSTRATES THE INTENDED FUNCTIONALITY
// OF THIS PROJECT

var userIds = [
  ['userId'],
  ['0x1z05senFY8At3MiQHOt7h2lZc2'],
  ['1mgmIUZ4M5g5FY8MGXTE8F2exvy2'],
  ['2aELYTW66iRhGpLCkX0fd8tdEtD2'],
  ['2wYuTLMHABXIEEPYRtqX2zGCirH2'],
  ['3T7cnvLuoSM01LanPUJxF6sDjbQ2'],
  ['3vfHuCU4fwcfXKAwRrpVb5vHZuE3'],
  ['7mdwV1BifAZFKfBq2vyyjS8IXue2'],
  ['9KruitMi6pUwSntebnC8xBRmagx2'],
  ['AtW4lqSTt9UNOis99TfN4ap6hnE3'],
  ['Bue7QNqfBfRMtOYbfLdewldemH92'],
  ['cLJPSFtchzfKWLyjWzLlhdQXh1H2'],
  ['CMt1WTwhNFZtiYJ80egQvvaKgJE3'],
  ['cqrunqefnTMOW49Y8hXuRydVRhW2'],
  ['E8in2Z3aEoUOAt2pEfRBOcoNR9P2'],
  ['EFzcd8TnBYPQkfX2y1AV8EZApnB2'],
  ['etqiWsONH4eC0R31T43l2cynEOB2'],
  ['HQ1fWFo6CodYhUjyek7YPVNx8TE2'],
  ['I0qlSYrZkhMjRL7U4f86IKYddlg1'],
  ['IalaaFKB4yQIEGnIfoMLtrJLUgw1'],
  ['imJSv0QGdLMbXgEU8UamqBvBIWB3'],
  ['iVmw3Hz0wiT40q7yNDr6buTRMPG2'],
  ['K71tM8OaluPW0EaIVpw1Cx0MWxz2'],
  ['lE7EbmVZwIPcfQcKHgr2BrUpVkm1'],
  ['LqjSZRINDXTxqrm9406eA2k6Iad2'],
  ['MJlJJoMZwsUBz2oO7CSt9UlwQYG2'],
  ['nXWMuInTYJeVS6MnynxrumAvblj2'],
  ['NztJLzmRp1dv6P9vDcUm1AoB27M2'],
  ['QAMMs56aMYVocqkhd45zwn8g3zp1'],
  ['qdMbrEjOWHhuSI9mTqE0M7PgcyB2'],
  ['qXrIn5b06aTbZj0295lWbxQ6Iib2'],
  ['R9OrQub194S8mTt1EQ5VjQiqI2u1'],
  ['Rna3ShtUlyegX3coIK8ofcyH5hA3'],
  ['shWYwSNUTbTm7JZIPsnBlvpXNdZ2'],
  ['T6ZZsXDjk3cJM0RmMHbk8DiqlD82'],
  ['tiGv8rov2ed2BQ6MK94fJSoFsgh1'],
  ['U3y7f6AhMMR49Vqu5eUZhXdzNiV2'],
  ['u7YR0CtA29RLtFCrkyaUJmLIgmC3'],
  ['UyIEKM8sA7RYH8XvPyEubsnIQpF3'],
  ['V0w4yxlnOoW8TIfkIsepITZSxd33'],
  ['w0waWVfg6xSVd1VtCDvRHVLli0L2'],
  ['welXkvO98JbifcASj9Ds76GRH3F2'],
  ['wqT9Faa6nTWwJgV4KD8j3txe9fD3'],
  ['xcxlaVzGCxZxpqJ3qtt4tToGgBe2'],
  ['XOlPt2gCOlOQUvo7DQ3qAVgHcMz2'],
  ['ykmAvXrc6fTQPlrGFcc1kmSQSB83'],
  ['YpEF2x709hVagQwZ5NHBAtqsbvs2'],
]

var bq_effort = [
  ['userId', 'bq_jobs', 'bq_bytes'],
  ['1mgmIUZ4M5g5FY8MGXTE8F2exvy2', 11, 30000],
  ['2aELYTW66iRhGpLCkX0fd8tdEtD2', 22, 20000],
  ['I0qlSYrZkhMjRL7U4f86IKYddlg1', 33, 10000],
  ['ykmAvXrc6fTQPlrGFcc1kmSQSB83', 0, 0],
  ['U3y7f6AhMMR49Vqu5eUZhXdzNiV2', 44, 0],
  ['qXrIn5b06aTbZj0295lWbxQ6Iib2', 0, 40000],
  ['MJlJJoMZwsUBz2oO7CSt9UlwQYG2', 0, 0],
  ['welXkvO98JbifcASj9Ds76GRH3F2', 0, 0],
  ['NztJLzmRp1dv6P9vDcUm1AoB27M2', 0, 0],
  ['qdMbrEjOWHhuSI9mTqE0M7PgcyB2', 0, 0],
]

var prediction = [
  ['userId', 'mape', 'mspe'],
  ['1mgmIUZ4M5g5FY8MGXTE8F2exvy2', 123123, 123123],
  ['2aELYTW66iRhGpLCkX0fd8tdEtD2', 231231, 231231],
  ['I0qlSYrZkhMjRL7U4f86IKYddlg1', 312312, 312312],
]

var nb_effort = [
  ['userId', 'nb_effort'],
  ['I0qlSYrZkhMjRL7U4f86IKYddlg1', 3],
  ['2aELYTW66iRhGpLCkX0fd8tdEtD2', 2],
  ['1mgmIUZ4M5g5FY8MGXTE8F2exvy2', 2],
]


var result = [];

var keys = userIds.shift();
userIds.forEach((row)=>{
  let record = {}
  row.forEach((col,index)=>{
    record[keys[index]] = col
  })
  result.push(record)
})


var keys = bq_effort.shift();
bq_effort.forEach((row)=>{
  let record = {}
  row.forEach((col,index)=>{
    record[keys[index]] = col
  })
  result.push(record)
})


var keys = prediction.shift();
prediction.forEach((row)=>{
  let record = {}
  row.forEach((col,index)=>{
    record[keys[index]] = col
  })
  result.push(record)
})

var keys = nb_effort.shift();
nb_effort.forEach((row)=>{
  let record = {}
  row.forEach((col,index)=>{
    record[keys[index]] = col
  })
  result.push(record)
})


var headers = [...new Set([...new Set(result.map((item,index)=>{
  return Object.keys(item).join(',')
}
))].join(',').split(','))]

var foreign_key = 'userId';

var output = {}

// MERGE RECORDS ON FOREIGN KEY
result.forEach((item)=>{
  let record = {};
  Object.keys(item).forEach((key)=>{
    record[key] = item[key]
  }
  )
  output[record[foreign_key]] = Object.assign({}, output[record[foreign_key]], record)
})

// BACKFILL EMPTY COLUMNS
Object.keys(output).forEach((row)=>{
  let user = output[row];

  headers.forEach((key)=>{
    user[key] = user[key] || null
  })
  output[user[foreign_key]] = user;
})


// OUTPUT TO CSV
var csvText = [];

var removeCol = headers.indexOf(foreign_key)
var dataCols = [...headers.slice(0, removeCol), ...headers.slice(removeCol+1, headers.length)]
dataCols.sort((a,b)=>{ return a.localeCompare(b)})

var headerRow = [
  foreign_key,
  ...dataCols,
]

csvText.push(headerRow)

Object.values(output).forEach((row)=>{
  let resultRow = [];

  dataCols.forEach(col=>{
    resultRow.push(row[col])
  })

  csvText.push([
    row[foreign_key],
    ...resultRow,
  ].join(',',))
})

console.log(csvText.join('\n'))

// OUTPUT TO JSON


data = Object.values(output).map(user=>{
  return {[user.userId]: user}
})

jsonOutput = {};

data.forEach((item)=>{
  let result = [];
  let user = Object.values(item).shift();

  result.push({
    name: 'mspe',
    label: 'MSPE',
    value: user.mspe,
  })

  result.push({
    name: 'mape',
    label: 'MAPE',
    value: user.mape,
  })

  result.push({
    name: 'nb_effort',
    label: 'Notebook Effort',
    value: user.nb_effort,
  })

  result.push({
    name: 'bq_jobs',
    label: 'BigQuery Effort',
    value: user.bq_jobs,
  })

  jsonOutput[user.userId] = result;

})

console.log(JSON.stringify(jsonOutput, null, '  '))
