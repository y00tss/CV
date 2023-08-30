const phoneNumberElement = document.getElementById('phone-number');

  phoneNumberElement.addEventListener('click', function () {
    const tempTextArea = document.createElement('textarea');

    tempTextArea.value = phoneNumberElement.textContent;

    document.body.appendChild(tempTextArea);

    tempTextArea.select();

    document.execCommand('copy');

    document.body.removeChild(tempTextArea);

    phoneNumberElement.style.backgroundColor = 'yellow';

    setTimeout(function () {
      phoneNumberElement.style.backgroundColor = 'initial';
    }, 1000);
  });