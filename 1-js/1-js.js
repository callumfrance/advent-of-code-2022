import { readline } from 'https://deno.land/x/readline@v1.1.0/mod.ts';

let maxElfCalories = [0, 0, 0];
let currentElfCalories = 0;

function checkMaxCalories(currentCalories) {
  if (currentCalories > maxElfCalories[0]) {
    maxElfCalories = [currentCalories].concat(maxElfCalories.slice(0, 2));
  } else if (currentCalories > maxElfCalories[1]) {
    maxElfCalories = [maxElfCalories[0]]
      .concat([currentCalories])
      .concat(maxElfCalories[1]);
  } else if (currentCalories > maxElfCalories[2]) {
    maxElfCalories = maxElfCalories.slice(0, 2).concat([currentCalories]);
  }
}

const f = await Deno.open('./input.txt');

for await (const rawLine of readline(f)) {
  const line = new TextDecoder().decode(rawLine);

  if (line) {
    currentElfCalories += parseInt(line);
  } else {
    checkMaxCalories(currentElfCalories);
    currentElfCalories = 0;
  }
}
f.close();

checkMaxCalories(currentElfCalories);

console.log(maxElfCalories);
console.log(maxElfCalories.reduce((total, current) => total + current));
