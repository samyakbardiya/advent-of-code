import fs from "fs";

function read() {
  const stdinBuffer = fs.readFileSync(0);
  const stdin = stdinBuffer.toString().trim();
  return stdin.split("\n").map((line) => line.split(/\s+/).map(Number));
}

function partOne(data) {
  let ans = 0;
  for (let i = 0; i < data.length; i++) {
    const report = data[i];

    if (report[0] == report[1]) continue;

    let isSafe = true;

    if (report[0] < report[1]) {
      for (let j = 1; j < report.length; j++) {
        const diff = report[j] - report[j - 1];
        if (diff < 1 || diff > 3) {
          isSafe = false;
          break;
        }
      }
    } else {
      for (let j = 1; j < report.length; j++) {
        const diff = report[j - 1] - report[j];
        if (diff < 1 || diff > 3) {
          isSafe = false;
          break;
        }
      }
    }

    if (isSafe) {
      ans++;
    }
  }
  return ans;
}

// function partTwo(data) {
//   function calcAvgDiff(report) {
//     const diff = [];
//     let totalDifference = 0;
//     for (let i = 1; i < report.length; i++) {
//       const difference = report[i] - report[i - 1];
//       diff.push(difference);
//       totalDifference += difference;
//     }
//     const averageDifference = totalDifference / (report.length - 1);
//     console.log("avgDiff", averageDifference, diff);
//     return averageDifference;
//   }
//   let ans = 0;
//   for (let i = 0; i < data.length; i++) {
//     console.log();
//     const report = data[i];
//     let isFirst = true;
//     let isSafe = true;
//     const avgDiff = calcAvgDiff(report);
//     if (avgDiff > 0) {
//       // increasing
//       for (let j = 1; j < report.length; j++) {
//         let diff = report[j] - report[j - 1];
//         if (diff < 1 || diff > 3) {
//           console.log("diff", diff, report[j], report[j - 1]);
//           if (!isFirst) {
//             isSafe = false;
//             break;
//           }
//           if (j == report.length - 1) {
//             diff = report[j - 1] - report[j - 2];
//             if (diff < 1 || diff > 3) {
//               console.log("diff", diff, report[j + 1], report[j - 1]);
//               isSafe = false;
//               break;
//             }
//           } else {
//             diff = report[j + 1] - report[j - 1];
//             if (diff < 1 || diff > 3) {
//               console.log("diff", diff, report[j + 1], report[j - 1]);
//               isSafe = false;
//               break;
//             }
//           }
//           isFirst = false;
//           j++;
//         }
//       }
//     } else {
//       // decreasing
//       for (let j = 1; j < report.length; j++) {
//         let diff = report[j - 1] - report[j];
//         if (diff < 1 || diff > 3) {
//           console.log("diff", diff, report[j - 1], report[j]);
//           if (!isFirst) {
//             isSafe = false;
//             break;
//           }
//           if (j == report.length - 1) {
//             diff = report[j - 2] - report[j - 1];
//             if (diff < 1 || diff > 3) {
//               console.log("diff", diff, report[j - 1], report[j + 1]);
//               isSafe = false;
//               break;
//             }
//           } else {
//             diff = report[j - 1] - report[j + 1];
//             if (diff < 1 || diff > 3) {
//               console.log("diff", diff, report[j - 1], report[j + 1]);
//               isSafe = false;
//               break;
//             }
//           }
//           isFirst = false;
//           j++;
//         }
//       }
//     }
//     console.log(isSafe, report);
//     if (isSafe) {
//       ans++;
//     }
//   }
//   return ans;
// }

function partTwo(data) {
  for (let i = 0; i < data.length; i++) {
    console.log();

    const report = data[i];
    console.log("===>", report);

    const delta = [];
    for (let d = 1; d < report.length; d++)
      delta.push(report[d] - report[d - 1]);
    const avgDelta =
      delta.reduce((partSum, a) => partSum + a, 0) / delta.length;
    console.log(avgDelta, delta);

    const prefixSum = report.map(
      function (val) {
        return (this.acc += val);
      },
      { acc: 0 },
    );
    console.log(prefixSum);
  }
}

function main() {
  const input = read();
  const ansOne = partOne(input);
  console.log("ansOne", ansOne);
  const ansTwo = partTwo(input);
  console.log("ansTwo", ansTwo);
}

main();
