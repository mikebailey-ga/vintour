$(document).ready(function(){
    $('.mobile-nav-trigger').click(function(){
        $('.mobile-nav').toggleClass('active');
    });
    $('.mobile-nav-close').click(function(){
        $('.mobile-nav').toggleClass('active');
    })

    //Smooth Scroll
    $("a").on('click', function(event) {
        if (this.hash !== "") {
          event.preventDefault();
          var hash = this.hash;
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function(){
            window.location.hash = hash;
          });
        } 
      });

      //landing page slider
      $('.slider').owlCarousel({
          loop:true,
          margin:10,
          nav:false,
          autoplay: true,
          items:1,
          mouseDrag: false,
          touchDrag: false,
          freeDrag: false,
          dots: true,
      });

    
});