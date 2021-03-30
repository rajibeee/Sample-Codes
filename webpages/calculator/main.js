function backspace(str) {
  str = str.substring(0,str.length-1); 
  return str;
  }

function square(str) {
    str = str*str;
    return str; }


function root(str) {
    str = Math.sqrt(str); 
    return str; }

function inverse(str) {
    str = 1/str;
    return str; }

function facto(str) {
    
    var result = str;
    if (str === 0 || str === 1) 
      return 1; 
    while (str > 1) { 
      str--;
      result *= str;
    }
    return result;
}