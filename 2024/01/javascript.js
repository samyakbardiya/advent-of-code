import fs from "fs";

function readInput() {
  const stdinBuffer = fs.readFileSync(0);
  const stdin = stdinBuffer.toString();

  const pairs = stdin
    .trim()
    .split("\n")
    .map((line) => line.split(/\s+/).map(Number));

  const [left, right] = pairs.reduce(
    ([left, right], [l, r]) => {
      left.push(l);
      right.push(r);
      return [left, right];
    },
    [[], []],
  );

  return [left, right];
}

function partOne(left, right) {
  left.sort();
  right.sort();

  let ans = 0;
  for (let i = 0; i < left.length; i++) {
    ans += Math.abs(left[i] - right[i]);
  }
  return ans;
}

function partTwo(left, right) {
  left.sort();
  right.sort();

  let ans = 0;
  for (let i = 0; i < left.length; i++) {
    if (left[i] < right[0]) continue;

    for (let j = 0; j < right.length; j++) {
      if (right[j] > left[i]) continue;

      let times = 0;
      while (left[i] == right[j] && j < right.length) {
        j++;
        times++;
      }

      ans += left[i] * times;
    }
  }

  return ans;
}

function main() {
  const [left, right] = readInput();

  const ansOne = partOne(left, right);
  console.log("ansOne", ansOne);

  const ansTwo = partTwo(left, right);
  console.log("ansTwo", ansTwo);
}

main();
