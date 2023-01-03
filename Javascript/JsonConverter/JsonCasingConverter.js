// Converts all json object keys to camelCase or PascalCase
// Code for toCamel method is taken from this thread:
// https://exceptionshub.com/convert-returned-json-object-properties-to-lower-first-camelcase.html
// Could have made this my self but this saved me some time. Thank you admin at Exceptionshub.com!
// Usage:
// node JsonCamelCaseConverter([Json file to convert], [result destination], [convert to pascalcase true/false default false])
// If no destination is specified it will write result.json to script location.

const fs = require('fs');

const args = process.argv;

const transform = (o, p) => {
  var newO, origKey, newKey, value;
  if (o instanceof Array) {
    newO = [];
    for (origKey in o) {
      value = o[origKey];
      if (typeof value === 'object') {
        value = transform(value, p);
      }
      newO.push(value);
    }
  } else {
    newO = {};
    for (origKey in o) {
      if (o.hasOwnProperty(origKey)) {
        const theWay = p === false ? () => origKey.charAt(0).toLowerCase()
                                   : () => origKey.charAt(0).toUpperCase();
        newKey = (theWay() + origKey.slice(1) || origKey).toString();
        value = o[origKey];
        if (value instanceof Array || (value !== null && value.constructor === Object)) {
          value = transform(value, p);
        }
        newO[newKey] = value;
      }
    }
  }
  return newO;
};

function convert(src, dest, pascalCase) {
  let rawData = fs.readFileSync(src);
  let items = JSON.parse(rawData);
  let convertedItems = transform(items, pascalCase)
  if (dest == undefined) {
    fs.writeFileSync('./result.json', JSON.stringify(convertedItems));
  } else {
    fs.writeFileSync(dest, JSON.stringify(convertedItems));
    console.log('Json converted to ', dest);
  }
}

convert(args[2], args[3], args[4]);