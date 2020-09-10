// data = '...'
// userIds = '...'

var events = [];
var users = {}
var userEventCount = {};

rows = data.split('\n');

for (row of rows) {
  if (row) {
    let event = row.split(',');
    events.push({
      timestamp: event[0].trim(),
      userId: event[1].trim(),
      eventId: event[2].trim(),
      pathname: event[3].trim(),
    })
  }
}

var userList = events.map((item, index)=>{
  return item.userId;
})

var users = new Set(userList);

for (user of users) {
  userEventCount[user] = 0;
}

for (event of events) {
  let user = event.userId
  userEventCount[user] += 1
}

// JSON.stringify(userEventCount, null, '  ')
var sorted = Object.keys(userEventCount).sort((a,b)=>{return userEventCount[b] - userEventCount[a]});
var filtered = sorted.filter((item,index)=>{ return userIds.includes(item) });

var printRow = [];
for (user of filtered) {
  printRow.push([user, userEventCount[user]].join(','))
}

console.log(printRow.join('\n'))

