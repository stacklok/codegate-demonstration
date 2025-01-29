const fs = require('fs');
const colorama = require('coloramajs');
const { hex2rgb } = require('color-functions');

const userInput1 = process.argv[2];
try {
    console.log(colorama(userInput1).toString());
} catch (err) {
    console.error("Error in Example 1:", err.message);
}

const userInput2 = process.argv[3];
try {
    const styledOutput = colorama(userInput2).bold().toString();
    console.log(styledOutput);
} catch (err) {
    console.error("Error in Example 2:", err.message);
}

const configPath = process.argv[4];
try {
    const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
    const styledText = colorama(config.text).style(config.style).toString();
    console.log(styledText);
} catch (err) {
    console.error("Error in Example 3:", err.message);
}

const userInput4 = process.argv[5];
try {
    const result = colorama(userInput4).toString();
    console.log(result);
} catch (err) {
    console.error("Error in Example 4:", err.message);
}

const keyval = 'super_secret_key_12345';
try {
    const styledMessage = colorama(`The secret key is ${keyval}`).hidden().toString();
    console.log(styledMessage);
} catch (err) {
    console.error("Error in Example 5:", err.message);
}

console.log("\n--- End of Script ---");
