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

x = null;    // Инициализация переменной
console.log(x);

// Objects:
var obj = {property: 'value'};
console.log(obj.property);
console.log(obj['property']);
console.log(typeof(obj),obj);

var array = [obj, obj];
console.log(typeof(array), array);

// Mutability
var obj = {property: 'value'};
var newObject = obj;
newObject.newProperty = 'new value';
newObject.property = 'replace';

console.log(newObject, obj);

// Добавление переменных
var v = [];
v.push('1');
v.push('2');
console.log(v);
