'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the migratoryBirds function below.
function migratoryBirds(arr) {
    const types = [1, 2, 3, 4, 5];
    const result = [];
    types.forEach(type => {
        let count = 0;
        arr.forEach(item => {
            if (item === type) count++;
        })
        result.push({ type, count });
    })
    const sortedRes = result.sort((a, b) => a.count - b.count).reverse()
    let minimumType = sortedRes[0];
    sortedRes.forEach(res => {
        if (res.count === minimumType.count && res.type < minimumType.type) {
            minimumType = res;
        }
    })
    return minimumType.type;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const arrCount = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const result = migratoryBirds(arr);

    ws.write(result + '\n');

    ws.end();
}
