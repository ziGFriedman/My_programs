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

!!'a';    // Отрицание НЕ'a'

Number('14');    // Приводит строку к числу

Boolean(x && x.length);    // Приведение к булевому типу

String(123);    // Приведение к строке

// Конструкции языка

var x = 1 === 1 ? 'true' : 'false'    // Проверка условия, х=1 == 1 ?

// Условие if всегда в скобках
if (true) {
  console.log('123')
}

var (!flag) {
  console.log('if');
} else if (flag && 1 < 2) {    // || - or. && - and
  console.log('elseif');
} else {
  // do nothing
}

var ternary = 40 > 13 ? 'yes' : 'no';
console.log(ternary);

// Проверка входного значения
var value = '123';

switch (value) {
  case '321':
    console.log('1');
    break;
  case '123':
    console.log('2');
    break;
  default:
    console.log('other');
    break;
}

// Цикл
for (var i = 0; i < 10; i++) {    // ++i, i++ - приоритет операций: +1 +i, i + 1
  console.log(i);
}

var iterable = ['a', 2, 'b', 4, 5];
for (var item in iterable) {
  console.log(item, iterable[item]);
}
