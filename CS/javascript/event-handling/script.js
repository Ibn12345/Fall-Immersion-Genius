document.getElementById('myButton').addEventListener('click', function() {
    Image = document.createElement('img');
    Image.src = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png';
    document.body.appendChild(Image);
});