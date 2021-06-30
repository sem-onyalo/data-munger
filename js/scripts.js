/*!
* Start Bootstrap - Bare v5.0.2 (https://startbootstrap.com/template/bare)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.getElementById('export').onclick = function exportImages() {
    urls = [];
    elements = document.getElementsByClassName('form-check-input');
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].checked) {
            imgElement = document.getElementById('image-' + elements[i].id.replace('include-', ''));
            urls.push(imgElement.src);
            
        }
    }

    window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));
 }