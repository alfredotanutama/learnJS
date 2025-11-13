const usernames = ['yandy','dimas','mita'];
// console.log("Ada total "+ usernames.length+ " username.");

const newUserName = 'yandy';

const isUserNameAvailable = usernames.includes(newUserName);

if (isUserNameAvailable){
    console.log("Username sudah digunakan")
}else{
    console.log("Username tersedia")
}
