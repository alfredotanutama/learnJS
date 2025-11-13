const usernames = ['yandy','dimas','mita'];
// console.log("Ada total "+ usernames.length+ " username.");

const newUserName = 'edo';

const isTaken = usernames.includes(newUserName);

if (isTaken){
    console.log("Username sudah digunakan")
}else{
    console.log("Username tersedia")
}

console.log(usernames[0]);
console.log(usernames[1]);
console.log(usernames[2]);