'use strict';

function (window, document) {
  function colorizeTexts() {
    var colors = [
      'red',
      'grey',
      'black',
      'orange'
    ];

    var color = colors [
      Math.floor(Math.random() * colors.length)
    ];

    var texts = document.querySelector('.texts');    // compare with querySelectorAll
    texts.style['background-color'] = color;
  }

  function setStatus(status) {
    var statusAlert = document.getElementById('status');
    var successColor = statusAlert.getAttribute('data-success-color');
    var failureColor = statusAlert.getAttribute('data-failure-color');

    var textStatus = status ? 'Success' : 'Failure';

    var element = document.createElement('p');

    element.style.backgroundColor = status ? successColor : failureColor
    element.innerText = textStatus;
    statusAlert.appendChild(element);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var control = document.getElementById('toggle');
    // control.oneclick = function (event) {
    // console.log(event);
    // colorizeTexts();
    // setStatus(Math.round(Math.random()));
    // };

    // or:
    control.addEventListener('click', function(event) {
      console.log(this, event);
      colorizeTexts();
      setStatus(Math.round(Math.random()));
    });
    // control.addEventListener('click', function(event) {
    //  collectStatistics();
    // });
  });
})(window, document);
