import firebase from 'firebase/app'
import 'firebase/firestore'
import 'firebase/auth'

// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyAX4aA3GILFoey_vyvN6kGJBAcer7HQIuM",
    authDomain: "chess-app-2e1e9.firebaseapp.com",
    databaseURL: "https://chess-app-2e1e9.firebaseio.com",
    projectId: "chess-app-2e1e9",
    storageBucket: "",
    messagingSenderId: "655282327550",
    appId: "1:655282327550:web:cdc77b90dac60f5d"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.firestore().settings({ timestampsInSnapshots: true});

// export default firebase;

const firestore = new firebase.firestore()

export { firestore }