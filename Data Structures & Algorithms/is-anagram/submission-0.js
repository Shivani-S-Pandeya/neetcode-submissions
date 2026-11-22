class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        //optimizing on space
        
//         let sSorted = s.split("").sort().join("");
//         let tSorted = t.split("").sort().join("");

//   if (sSorted.length === tSorted.length && sSorted === tSorted) {
//     return true;
//   } else {
//     return false;
//   }

 // ***** Optimizing on time *******

  // check the length
  if (s.length !== t.length) return false;

  //build a character hashmap i.e. object and increment or decrement it based on the characters found in each string input
  let character = {};
  for (let i = 0; i < s.length; i++) {
    //if character is present in 1st string, then increment the value or initialize it with 1
    character[s[i]] = character[s[i]] ? character[s[i]] + 1 : 1;
    //if character is present in 2nd string, then decrement the value in char object or set it -1
    character[t[i]] = character[t[i]] ? character[t[i]] - 1 : -1;
  }

  for (let j = 0; j < s.length; j++) {
    console.log(character[s[j]]);
    if (character[s[j]] !== 0) {
      return false;
    } 
  } return true;

    }
}
