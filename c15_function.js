function checkNumber(number){

    if(number<0){
        console.log('Negative Number')
    } 
    else 
        if (number===0){
            console.log('Neutral Number')
        }
        else {
        console.log('Positive Number')
    }

};

checkNumber(-1);
checkNumber(13243);
checkNumber(0);
