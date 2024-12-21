import fs from "fs";

const multiply = (str) => {
  const x = str.search(/\(/);
  const y = str.search(/\)/);
  const expression = str.substring(x + 1, y);
  const [a, b] = expression.split(",");
  return a * b;
};

const partOne = (input) => {
  let ans = 0;

  let str = input;

  let i = str.search(/mul\(\d+,\d+\)/);
  str = str.substring(i + 3);
  while (i > 0) {
    const product = multiply(str);
    ans += product;
    // console.log(str.substring(x + 1, y));

    i = str.search(/mul\(\d+,\d+\)/);
    str = str.substring(i + 3);
  }

  return ans;
};

const search = (input) => {
  let objIdx = {};
  objIdx.mul = input.search(/mul\(\d+,\d+\)/);
  objIdx._do = input.search(/do\(\)/);
  objIdx.dnt = input.search(/don't\(\)/);

  let nxtObj = Object.keys(obj)[0];
  let nxtIdx = obj[smallestKey];
  for (let key in objIdx) {
    if (objIdx[key] < nxtIdx) {
      nxtIdx = key;
      nxtObj = objIdx[key];
    }
  }
  return [nxtIdx, nxtObj];
};

const partTwo = (input) => {
  let ans = 0;

  let mul = input.search(/mul\(\d+,\d+\)/);
  console.log("  mul", mul, input.substring(mul));
  input = input.substring(mul + 3);

  let _do = input.search(/do\(\)/);
  let _dont = input.search(/don't\(\)/);
  console.log("   do", _do, input.substring(_do));
  console.log("don't", _dont, input.substring(_dont));

  while (mul > 0) {
    if (_do > _dont) mul = input.search(/mul\(\d+,\d+\)/);
    input = input.substring(mul + 3);
  }

  // while (mul > 0) {
  //   // let _do = input.search(/do\(\)/);
  //   // let _dont = input.search(/don't\(\)/);
  // }

  return ans;
};

const read = () => {
  const stdinBuffer = fs.readFileSync(0);
  const stdin = stdinBuffer.toString().trim().replaceAll(/\s/g, "");
  return stdin;
};

(() => {
  const input = read();
  const ansOne = partOne(input);
  console.log("ansOne:", ansOne);
  const ansTwo = partTwo(input);
  console.log("ansTwo:", ansTwo);
})();
