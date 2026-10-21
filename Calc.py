
const readline = require('node:readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter number 1: ", (num1) => {
  const x = Number(num1);

  rl.question("Enter number 2: ", (num2) => {
    const y = Number(num2);

    rl.question("Enter the desired operation (+, -, *, /): ", (z) => {
      switch (z) {
        case "+":
          console.log(x + y);
          break;

        case "-":
          console.log(x - y);
          break;

        case "*":
          console.log(x * y);
          break;

        case "/":
          if (y !== 0) {
            console.log(x / y);
          } else {
            console.log("Cannot divide by zero");
          }
          break;

        default:
          console.log("Invalid operator");
      }

      rl.close();
    });
  });
});
