function* fibGenerator() {
  let a = 0, b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

// Example usage:
const gen = fibGenerator();
const result = [];
for (let i = 0; i < 5; i++) {
  result.push(gen.next().value);
}
console.log(result); // [0, 1, 1, 2, 3]
