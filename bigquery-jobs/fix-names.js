var userIds = [
  'USER_ID',
]

var job_count = {
  'user_id': 1,
}

result = {}

Object.keys(job_count).forEach(key=>{
  for (userId of userIds) {
    if (key.toLowerCase() === userId.toLowerCase()) {
      result[userId] = job_count[key]
    }
  }
})

console.log(JSON.stringify(result, null, 2))
