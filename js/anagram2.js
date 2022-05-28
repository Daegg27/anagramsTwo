exports.anagramsFor = function(word, listOfWords) {

    let sortedStrings = [];
    let anagramArray = [];
    let finalAnswer;

    for (let i = 0; i < listOfWords.length; i++){
        sortedStrings.push(listOfWords[i].toLowerCase().split("").sort().join(""));
    }
    finalAnswer = word.toLowerCase().split("").sort().join("");
    
    // console.log(sortedStrings);
    // console.log(finalAnswer);
    for (let k = 0; k < sortedStrings.length; k++){
        if (finalAnswer === sortedStrings[k]){
            anagramArray.push(listOfWords[k]);
        }
    }
   
    return anagramArray;
    




};
// exports.anagramsFor("hellojf", ["helEFEa", "DFfsAW", "DHAkedD", "AbdaAW"]);
