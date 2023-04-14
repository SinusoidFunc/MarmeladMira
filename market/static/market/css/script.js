// TODO:
// 1)Автоматическое переключение слайдов
// 2)Перенос на слайд по нажатию кружочка
// 3)Стили кружочков
// 4) Плавное переключение с последнего и первого слайдов


// Nessecary data
const sliderImages = document.querySelectorAll('.slider-img'),
    sliderLine = document.querySelector('.slider-line'),
    sliderDots = document.querySelectorAll('.slider-dot'),
    sliderBtnNext = document.querySelector('.next'),
    sliderBtnPrev = document.querySelector('.prev');


// Vars
var sliderCount = 0,
    sliderWidth;
    timer = 0;




// Buttns for listing slides
sliderBtnNext.addEventListener('click', nextSlide);
sliderBtnPrev.addEventListener('click', prevSlide);


// Func
function showSlide() {
    if (sliderCount == sliderImages.length) {
        sliderCount = 0;
    }
    sliderWidth = document.querySelector('.text-center-slider').offsetWidth;
    sliderLine.style.width = sliderWidth * sliderImages.length + 'px';
    sliderImages.forEach(item => item.style.width = sliderWidth + 'px');
    rollSlider();
    // highliteDots();
}


// Locate Dots right at the bottom of images
function locateDots() {
    let dotHeight = sliderDots[0].offsetHeight;
    sliderDots.forEach(item => item.style.bottom = dotHeight  + 'px');
}
// locateDots();
// Change the current image dot
function highliteDots() {
    sliderDots[sliderCount].style.background = 'red';
    for (let i = 0; i < sliderImages.length; i++) {
        if (i != sliderCount) {
            sliderDots[i].style.background = 'blue'
        }
    }
}


// Shows next slide
function nextSlide() {
    console.log('work')
    sliderCount++;
    if (sliderCount >= sliderImages.length) {
        sliderCount = 0;
        sliderLine.style.transition = '0s';
    } else {
        sliderLine.style.transition = '2s';
    }
    rollSlider();
    // highliteDots();
}

// Shows next slide
function prevSlide() {
    sliderCount--;
    if (sliderCount < 0) {
        sliderCount = sliderImages.length - 1;
        sliderLine.style.transition = '0s';
    } else {
        sliderLine.style.transition = '2s';
    }
    rollSlider();
    // highliteDots();
}


//Задает шаг перемещения слайдов
function rollSlider() {
    sliderLine.style.transform = `translateX(${-sliderCount * sliderWidth}px)`;
}

// Создает таймер
setInterval(nextSlide(), 2000);

// locateDots();
showSlide();


