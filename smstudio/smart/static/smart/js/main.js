/* библиотека для закрытия модальных окон без гемора*/
!function(e){"function"!=typeof e.matches&&(e.matches=e.msMatchesSelector||e.mozMatchesSelector||e.webkitMatchesSelector||function(e){for(var t=this,o=(t.document||t.ownerDocument).querySelectorAll(e),n=0;o[n]&&o[n]!==t;)++n;return Boolean(o[n])}),"function"!=typeof e.closest&&(e.closest=function(e){for(var t=this;t&&1===t.nodeType;){if(t.matches(e))return t;t=t.parentNode}return null})}(window.Element.prototype);

document.addEventListener('DOMContentLoaded', function() {
  
    const swiper = new Swiper('.image-slider', {
        // Optional parameters
        // direction: 'vertical',
        loop: true,

        // If we need pagination
        pagination: {
          el: '.swiper-pagination',
          clickable:true,

        },

        grabCursor:true,

        mousewheel:{
          eventTarget:".swiper",
        },



        // Navigation arrows
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },



        // And if we need scrollbar
        scrollbar: {
          el: '.swiper-scrollbar',
        },
      });
    });

/* Модальное окно  галереи*/
document.addEventListener('DOMContentLoaded', function() {
if (document.querySelector('.item-gallery-link')){
  var openGallery = document.querySelectorAll('.item-gallery-link');
  }else {
     return
     }

if (document.querySelector('.gallery-close')){
  closeGallery = document.querySelectorAll('.gallery-close');
      }else {
    return
    }

  galleryOverlay =  document.querySelector('#gallery-overlay-modal');

      /* Перебираем массив кнопок */
      openGallery.forEach(function(item){
        /* Назначаем каждой кнопке обработчик клика */
        item.addEventListener('click', function(e) {
            e.preventDefault();
            /* ищем модальное окно по атрибуту кнопки */
            var modalId = this.getAttribute('data-gallery-link');

            modalElem = document.querySelector('.gallery-modal[data-gallery ="' + modalId + '"]');
            modalElem.classList.add('active');
            galleryOverlay.classList.add('active');
         });

        });
        
        closeGallery.forEach(function(item){
          item.addEventListener('click', function(e) {
             var parentModal = this.closest('.gallery-modal');
             parentModal.classList.remove('active');
             galleryOverlay.classList.remove('active');
          });
         
       });
        /* скрытие окна при клике на подложку */
      galleryOverlay.addEventListener('click', function() {
        if (document.querySelector('.gallery-modal.active')){
      document.querySelector('.gallery-modal.active').classList.remove('active');
    }
      this.classList.remove('active');
    });
  });

  document.addEventListener('DOMContentLoaded', function() {  
/* Получаем массив кнопок */
if (document.querySelector('.js-open-modal')){
  var modalButtons = document.querySelectorAll('.js-open-modal');
  }else {
     return
     }

    if (document.querySelector('.extra-close')){
      closeButtons = document.querySelectorAll('.extra-close');
      }else {
      return
      }
      modalButtons.forEach(function(item){
        /* Назначаем каждой кнопке обработчик клика */
        item.addEventListener('click', function(e) {
            e.preventDefault();
            /* ищем модальное окно по атрибуту кнопки */
            var modalId = this.getAttribute('data-modal');
            modalElem = document.querySelector('.extracontent-wrapper-modal[data-modal-div ="' + modalId + '"]');

            modalElem.classList.add('active');
            galleryOverlay.classList.add('active');
         });
         });
         closeButtons.forEach(function(item){
          item.addEventListener('click', function(e) {
             var parentModal = this.closest('.extracontent-wrapper-modal');
             parentModal.classList.remove('active');
             galleryOverlay.classList.remove('active');
          });
          });
          galleryOverlay.addEventListener('click', function() {
            openModalWindow = document.querySelector('.extracontent-wrapper-modal.active');
            this.classList.remove('active');
            if (document.querySelector('.extracontent-wrapper-modal.active')){
            openModalWindow.classList.remove('active');
            }

            console.log('overlay')
          });
          });
        
/* модальное окно для новости */


document.addEventListener('DOMContentLoaded', function() {
  const swiper2 = new Swiper('.post-modal-slider', {
    // Optional parameters
    // direction: 'vertical',
    loop: true,

    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable:true,

    },

    grabCursor:true,

    mousewheel:{
      eventTarget:".post-modal-slider",
    },



    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },


    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  }); 

if (document.querySelector('.post-modal__cross')){
    overlay      = document.querySelector('#post-overlay-modal'),
    closeButton = document.querySelector('.post-modal__cross');
    modalElem = document.querySelector('.post-modal');
    checkElem = sessionStorage.getItem("cookie-message");
    if (checkElem == undefined) {
        setTimeout(function(){
            modalElem.classList.add('active');
            overlay.classList.add('active');
        },500)

       }
    closeButton.addEventListener('click', function(e) {
        var parentModal = this.closest('.post-modal');
         sessionStorage.setItem("cookie-message", true);
         parentModal.classList.remove('active');
         overlay.classList.remove('active');
      });

       /* закрытие по ESC */
  document.body.addEventListener('keyup', function (e) {
    var key = e.keyCode;
    if (key == 27) {
        sessionStorage.setItem("cookie-message", true);
        document.querySelector('.post-modal.active').classList.remove('active');
        document.querySelector('.post-overlay.active').classList.remove('active');
    };
  }, false);
    /* скрытие окна при клике на подложку */
    overlay.addEventListener('click', function() {
        sessionStorage.setItem("cookie-message", true);
        document.querySelector('.post-modal.active').classList.remove('active');
        this.classList.remove('active');
      });
    }

});

