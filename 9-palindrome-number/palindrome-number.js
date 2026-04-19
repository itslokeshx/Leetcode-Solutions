/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  let str = String(x);
  let reversed = "";
  for (let j = str.length - 1; j >= 0; j--) {
    reversed += str[j];
  }

  if (str === reversed) {
    return true;
  }
  return false;
};
console.log(isPalindrome(1221));
