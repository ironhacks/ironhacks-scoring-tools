var participantsDoc = await window.firebase.firestore()
  .collection('hacks')
  .doc(this.props.hackId)
  .collection('registration')
  .doc('participants')
  .get()

var participantsData = participantsDoc.data();

var participants = [];

for (let participant of Object.keys(participantsData)){
  participants.push({
    userId: participant,
    alias: participantsData[participant].alias,
  })
}

JSON.stringify(participants, null, '  ')
