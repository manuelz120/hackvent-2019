const fs = require("fs");
const { decode } = require("@yaas/bacon-cipher");

const markup = fs.readFileSync("./input.html").toString();
const charsToSkip = [" ", "\r", "\n", ".", ",", "-"];

const cleanedUpMarkup = markup
  .split("")
  .filter(c => !charsToSkip.some(v => v === c))
  .join("");

const baconSequence = cleanedUpMarkup
  .replace(/<em>(\w+)<\/em>/gm, (_, firstMatch) =>
    "_".repeat(firstMatch.length)
  )
  .split("")
  .map(c => (c === "_" ? "B" : "A"))
  .join("");

const formattedBacon = baconSequence
  .replace(/(\w{5})/g, "$1 ")
  .replace(/(^\s+|\s+$)/, "");

console.log(`Bacon sequence: \n${formattedBacon}`);
console.log("-----------------------------------------------------");

const decoded = decode(baconSequence);
console.log(decoded);
