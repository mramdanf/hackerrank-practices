'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the pageCount function below.
 */
function pageCount(n, p) {
    /*
     * Write your code here.
     */
    let fromFront = 0;
    for (let i = 0; i < n; i += 2) {
        if (i === p || i + 1 === p) {
            break;
        }
        fromFront++;
    }
    let fromTail = 0;
    for (let j = n; j > 0; j -= 2) {
        if (n % 2 === 0) {
            if (j === n && j === p) {
                break;
            } else if (j === p || j + 1 === p) {
                break;
            }
        } else {
            if (j === p || j - 1 === p) {
                break;
            }
        }
        
        fromTail++;
    }
    return fromFront < fromTail ? fromFront : fromTail;


}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const p = parseInt(readLine(), 10);

    let result = pageCount(n, p);

    ws.write(result + "\n");

    ws.end();
}
