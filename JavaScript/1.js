'use strict';    // Ставится в начале файла для строгово режима ввода Js

// Подключение файла со скриптами
<script src="/js/script1.js"></script>;
<script src="/js/script2.js"></script>;

// Primitives;
var str = "A string";
var alsoString = 'A string';    // Запись переменных

console.log(str == alsoString);    // != не равно
console.log(str === alsoString);    // Лучше использовать такую запись сравнения
console.log(typeof(str), typeof alsoString);

var num1 = 1;
var num2 = 2.0;

console.log(num1 * num2);
console.log(1 === 1.0);

var x;    // Объявление переменной
console.log(x);

x = null;
console.log(x);
