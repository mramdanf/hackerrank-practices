'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the breakingRecords function below.
function breakingRecords(scores) {
    const firstRecord = scores[0];
    const heighests = [firstRecord];
    let maxRecord = firstRecord;
    let heighestBreakRecordCount = 0;

    const lowests = [firstRecord];
    let minRecord = firstRecord;
    let lowestBreakRecordCount = 0;

    scores.forEach(score => {
        if (score > maxRecord) {
            heighestBreakRecordCount++;
            maxRecord = score;
            heighests.push(score);
        } else {
            const lastHeighest = heighests[heighests.length - 1];
            heighests.push(lastHeighest);
        }

        if (score < minRecord) {
            lowestBreakRecordCount++;
            minRecord = score;
            lowests.push(score);
        } else {
            const lastLowes = lowests[lowests.length - 1];
            lowests.push(lastLowes);
        }
    });

    return [heighestBreakRecordCount, lowestBreakRecordCount];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const scores = readLine().split(' ').map(scoresTemp => parseInt(scoresTemp, 10));

    const result = breakingRecords(scores);

    ws.write(result.join(' ') + '\n');

    ws.end();
}
