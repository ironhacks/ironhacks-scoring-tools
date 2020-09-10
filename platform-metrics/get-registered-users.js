var hackId = 'DeKE13nHvqzolDUa0Fg9'; 

var fire2Date = (fireDate) => {
  if (!fireDate){
    return '';
  }
  
  let secs = fireDate.seconds || 0;
  let nsecs = fireDate.nanoseconds || 0;

  return new Date((secs * 1000) + (nsecs / 1000000)).toISOString();
}


var getRegisteredUsers = async () => {
  let users = [];
  let userIds = [];

  result = await window.firebase.firestore()
  .collection('hacks')
  .doc(hackId)
  .collection('registration')
  .doc('participants')
  .get()
  .then((docs)=>{
    let data = docs.data();

    Object.keys(data).forEach((id)=>{
      userIds.push(id);

      users.push(
        data[id].ref.get().then((user)=>{
          return {
            userId: user.id,
            ...user.data()
          }
        })
      )
    })

    return Promise.all(users).then((userList)=>{
      var list = userList.map((item, index)=>{
        return [item.userId, item.name, item.email].join(', ')
      })
      return list;
    }) 
  })

  console.log('\n\n')
  console.log(result.join('\n'))
  console.log('\n\n')

  return userIds
}

getRegisteredUsers();

