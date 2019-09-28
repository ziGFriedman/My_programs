function someFunction (a, b) {
  return a + b
}

someFunction(1, 2)    // 3
someFunction(1)    // NaN
someFunction(1, 2, 3, 4)    // 3

// Анонимная функция, работающая рекурсивно
var nfe = function namedFunctionalExpression (i) {
  if (i == 0) {
    return 0;
  }
  // namedFunctionalExpression = null;
  return i + namedFunctionalExpression(i-1);    // i-- or
};


// Objects

var MyClass = function (title) {
  this.title = title;
  var privateValue = 'secret';

  this.tellTitle = function () {
    console.log(this.title);
    console.log(this);
  };

  function privateFunction() {
    console.log(privateValue);
    console.log('This is:', this);
  }

  privateFunction();
}
